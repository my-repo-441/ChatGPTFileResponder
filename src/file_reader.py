import sys
import fitz  # PyMuPDF


def read_file(file_path):
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif file_path.endswith('.pdf'):
        return read_pdf(file_path)
    else:
        return ""

def read_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
            print(file_path,text)
        return text
    except Exception as e:
        print(f"Error occurred: {e}")
        return ""

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
    else:
        file_path = sys.argv[1]
        print(read_file(file_path))
