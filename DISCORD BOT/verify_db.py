import sqlite3
import os

db_paths = ['db/beartime.sqlite', 'db/settings.sqlite']

for db_path in db_paths:
    print(f"Checking {db_path}...")
    if not os.path.exists(db_path):
        print(f"Database file not found: {db_path}")
    else:
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("PRAGMA integrity_check;")
            result = cursor.fetchone()
            print(f"Integrity check result for {db_path}: {result}")
            conn.close()
        except Exception as e:
            print(f"Error checking database {db_path}: {e}")
