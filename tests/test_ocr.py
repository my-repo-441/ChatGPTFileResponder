import pytesseract
from pdf2image import convert_from_path
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv() 

client = OpenAI()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def ocr_pdf(file_path):
    try:
        images = convert_from_path(file_path)
        text = ""
        for i, image in enumerate(images):
            text += pytesseract.image_to_string(image, lang='jpn')
        return text
    except Exception as e:
        print(f"Error occurred: {e}")
        return ""

def summarize_text(text):
    print(text)
    messages = [
        {"role": "system", "content": "あなたは優秀なアシスタントです。次の文章に基づいてユーザの質問に答えて。"},
        {"role": "user", "content": f"、ユーザーの質問：問1 設問2(1)の回答を教えて。、文章：{text}"}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1000
    )
    summary = response.choices[0].message.content

    return summary

file_path = "../data/input/平成30年秋季_午後Ⅱ_問題.pdf"
text = ocr_pdf(file_path)
print(text)

summary=summarize_text(text)
print(summary)

