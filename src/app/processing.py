# File used to process data from database

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
