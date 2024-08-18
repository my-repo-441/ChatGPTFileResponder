import sqlite3
import logging
import os

# ログの設定
log_dir = "../logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(filename=os.path.join(log_dir, 'app.log'),
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def setup_database():
    conn = sqlite3.connect('file_cache.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT UNIQUE,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_file_content(file_path):
    conn = sqlite3.connect('file_cache.db')
    cursor = conn.cursor()
    
    # ファイルがデータベースにあるか確認
    cursor.execute('SELECT content FROM files WHERE filename = ?', (file_path,))
    result = cursor.fetchone()
    
    if result:
        # ファイルが存在する場合、内容を返す
        conn.close()
        logging.info(f"Retrieved content from database for file: {file_path}")  # デバッグ用ログ
        return result[0]
    else:
        # ファイルが存在しない場合、読み取り
        from file_reader import read_file
        content = read_file(file_path)
        if content:
            # データベースに保存
            cursor.execute('INSERT INTO files (filename, content) VALUES (?, ?)', (file_path, content))
            conn.commit()
            logging.info(f"Saved content to database for file: {file_path}")  # デバッグ用ログ
        conn.close()
        return content
