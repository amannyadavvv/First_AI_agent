import streamlit as st
import pdfplumber
import json
from pathlib import Path
import re

st.title("This is Your Personal Exam Buddy For Question Answering")
st.header("Upload Your Pdfs and You are good to Go") 
st.subheader("This is a subheader")
choice = st.radio("Navigation", ["Home", "Upload"])

file = st.file_uploader("Select your File",type=["pdf"])
if file is None:
    st.error("file is not Uploaded")
else:
    pass
def normalize_line(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())

def extract_pdf_to_json(pdf_path):
    pdf_path = Path(pdf_path)
    pages_data = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            text= text.strip()
            cleaned_text = normalize_line(text)
            pages_data.append({
                "page": i,
                "text": text,
                "Cleaned text": cleaned_text
            })
            
            with st.expander(f"page:{text}"):
                st.write(text)

    out_path = pdf_path.with_name(f"{pdf_path.stem}_pages.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, ensure_ascii=False, indent=2)

    print(f"[+] Extracted {len(pages_data)} pages -> saved to: {out_path}")
if choice =="Upload"
# Example run
# if __name__ == "__main__":
#     extract_pdf_to_json("Upload.pdf")
if file:
    save_path = Path(file.name)
    with open(save_path, "wb") as f:
        f.write(file.read())

    extract_pdf_to_json("Upload.pdf")