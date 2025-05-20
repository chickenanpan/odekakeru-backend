import sqlite3

def get_posts():

    conn =sqlite3.connect('odekakeru.db')
    cur = conn.cursor()

    query = "SELECT * FROM posts"
    cur.execute(query)

    posts = []
    for row in cur.fetchall():
        post = {
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "image_url": row[3],
            "post_user_id": row[4],
            "created_at": row[5],
            "updated_at": row[6]
        }
        posts.append(post)
    
    conn.close()

    return posts