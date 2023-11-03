from database.db_connection import execute_query,

def add_likes_dislikes()
    query = """
            ALTER TABLE heroes
            ADD COLUMN likes VARCHAR(10)
            ADD COLUMN dislikes VARCHAR(10)
            """
    execute_query(query)

add_likes_dislikes()
