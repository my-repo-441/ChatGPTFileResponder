import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text("text")
        return text
    except Exception as e:
        print(f"Error occurred: {e}")
        return ""

file_path = "../data/input/1_514.pdf"
text = extract_text_from_pdf(file_path)
print(text)
