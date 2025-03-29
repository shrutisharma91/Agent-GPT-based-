import io
from PyPDF2 import PdfReader
from fastapi import UploadFile

def process_file(file: UploadFile) -> str:
    """
    Process uploaded PDF or text files and extract their content.
    """
    try:
        file_content = file.file.read()

        if file.filename.endswith(".pdf"):
            reader = PdfReader(io.BytesIO(file_content))
            text = []
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
                else:
                    print(f"Warning: Could not extract text from a page in {file.filename}")
            return " ".join(text)

        elif file.filename.endswith(".txt"):
            return file_content.decode("utf-8")

        else:
            raise ValueError("Unsupported file type. Please upload a PDF or text file.")

    except Exception as e:
        raise ValueError(f"Error processing file: {str(e)}")
