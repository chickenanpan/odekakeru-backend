import sqlite3

def get_posts():

    conn = sqlite3.connect('odekakeru.db')
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
            "latitude": row[4],
            "longitude": row[5],
            "post_user_id": row[6],
            "created_at": row[7],
            "updated_at": row[8]
        }
        posts.append(post)
    
    conn.close()

    return posts

def get_post_by_id(post_id):

    conn = sqlite3.connect('odekakeru.db')
    cur = conn.cursor()

    query = "SELECT * FROM posts WHERE id = ?"
    cur.execute(query, (post_id,))

    post = None
    row = cur.fetchone()
    if row:
        post = {
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "image_url": row[3],
            "latitude": row[4],
            "longitude": row[5],
            "post_user_id": row[6],
            "created_at": row[7],
            "updated_at": row[8]
        }

    conn.close()

    return post