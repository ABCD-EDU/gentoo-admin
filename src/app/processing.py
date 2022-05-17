# File used to process data from database

categ_dict = {
    "hate": "hate_score",
    "normal": "normal_score",
    "offensive": "offensive_score",
    "profanity": "profanity_score",
    "race": "race_score",
    "religion": "religion_score",
    "sex": "sex_score",
    "other": "other_score",
    "none": "none_score",
}

filters = {1:{"category":"HATE", "min":50, "max":100},
    2:{"category":"PRFN", "min":69, "max":100}}

def search_filtered_users(cursor, queryInfo):
    name = queryInfo["name"]
    filters = queryInfo["filters"]
    sorting = queryInfo["sorting"]
    pagination = queryInfo["pagination"]
    query = build_query(filters, name, sorting["category"],
     sorting["order"], pagination["offset"], pagination["limit"])
    print(query)
    cursor.execute(query)
    data = cursor.fetchall()
    data = format_user_data(data, cursor)
    data = get_total_reports(data, cursor)
    data = get_metrics(data, cursor)
    return data


def build_query(filters, name, sort_by, order, offset, limit):
    query = "SELECT users.user_id, users.username, users.email, users.google_photo " \
        "from users inner join posts using(user_id) inner join metrics on posts.post_id = metrics.post_id " \
            "where users.username like '%" +name+ "%'"
    # Add filters
    if len(filters) != 0:
        for x in filters:
            categ = categ_dict[x["category"].lower()]
            floor = str(x["minScore"]/100)
            ceil = str(x["maxScore"]/100)
            query += " and (select avg("+ categ +") from metrics inner join posts using(post_id) where " \
                "posts.user_id = users.user_id) between " + floor + " and " + ceil
    # Group by and order
    query += " group by users.user_id, users.username, users.email, users.google_photo"
    query += " order by avg(metrics." + categ_dict[sort_by.lower()] + ") " + order
    # Pagination
    query += " offset " + str(offset) + " rows limit " + str(limit) + ";"
    return query


def search_users(cursor, name):
    cursor.execute("SELECT * FROM users WHERE username LIKE '%" + name + "%'")
    data = cursor.fetchall()
    data = format_user_data(data, cursor)
    data = get_total_reports(data, cursor)
    data = get_metrics(data, cursor)
    return data


def get_all_users(cursor):
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    data = format_user_data(data, cursor)
    data = get_total_reports(data, cursor)
    data = get_metrics(data, cursor)
    return data

def get_all_users_capped(cursor, qty):
    cursor.execute("SELECT * FROM users LIMIT %s", [qty])
    data = cursor.fetchall()
    data = format_user_data(data, cursor)
    data = get_total_reports(data, cursor)
    data = get_metrics(data, cursor)
    return data


def format_user_data(data, cursor):
    columns = []
    for x in cursor.description:
        columns.append(x[0])
    to_return = []
    for x in data:
        user = {}
        for i,e in enumerate(columns):
            user[e] = x[i]
        to_return.append(user)
    return to_return
    

def get_total_reports(data, cursor):
    for x in data:
        user_id = x["user_id"]
        cursor.execute("select count(poster_id) from reports where poster_id = %s;", [user_id])
        total_posts = cursor.fetchone()
        x["reports"] = total_posts[0]
    return data


def get_metrics(data, cursor):
    columns = ["hate_score", "normal_score", "offensive_score", "profanity_score",
     "race_score", "religion_score", "sex_score", "other_score", "none_score"]
    for x in data:
        for c in columns:
            exec_string = "select avg(" + c + ") from metrics inner join posts using(post_id) where posts.user_id = %s;"
            cursor.execute(exec_string, [x["user_id"]])
            value = cursor.fetchone()
            x[c] = value[0]
    return data
