from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv() 

client = OpenAI()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def summarize_text(text, question):
    print(text)
    messages = [
        {"role": "system", "content": "あなたは優秀なアシスタントです。次の文章に基づいてユーザーの質問に答えて。"},
        {"role": "user", "content": f"文章：{text} 質問：{question}"}
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=1000
    )
    summary = response.choices[0].message.content

    return summary
