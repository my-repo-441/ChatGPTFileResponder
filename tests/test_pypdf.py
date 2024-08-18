import PyPDF2

def extract_text_from_pdf(file_path):
    try:
        pdf_reader = PyPDF2.PdfReader(open(file_path, "rb"))
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error occurred: {e}")
        return ""

file_path = "../data/input/平成30年秋季_午後Ⅱ_問題.pdf"
text = extract_text_from_pdf(file_path)
print(text)
