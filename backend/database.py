from psycopg2 import pool

db_pool = pool.SimpleConnectionPool(
    minconn=1, maxconn=10,
    user="user", password="password",
    host="localhost", database="logs"
)

def get_logs():
    conn = db_pool.getconn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs ORDER BY timestamp DESC LIMIT 100;")
    logs = cursor.fetchall()
    cursor.close()
    db_pool.putconn(conn)  # Release connection back to the pool
    return logs
