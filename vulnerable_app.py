import sqlite3

def get_user(username):
    # ⚠️ Intentionally vulnerable to SQL injection - for SAST demo purposes only
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

def safe_placeholder():
    # This function is intentionally insecure for security scanning demonstration
    password = "hardcoded_secret_123"
    return password