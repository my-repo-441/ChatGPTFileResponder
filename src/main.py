import sys
from file_search import search_files
from chatgpt_api import summarize_text
from database import setup_database, get_file_content

def summarize_file(file_path, question):
    setup_database()  # データベースのセットアップ
    content = get_file_content(file_path)
    if content:  # Content is not empty
        summary = summarize_text(content, question)
        return summary
    return None

if __name__ == "__main__":
    file_path = input("ファイル名：")
    question = input("質問：")

    summary = summarize_file(file_path, question)
    
    if summary:
        print(f"File: {file_path}\nSummary: {summary}\n")
    else:
        print(f"No content found for file: {file_path}")
