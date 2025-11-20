import pdfplumber
import json
from pathlib import Path

def extract_pdf_to_json(pdf_path):
    pdf_path = Path(pdf_path)
    pages_data = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            pages_data.append({
                "page": i,
                "text": text
            })

    # output file: <name>_pages.json
    out_path = pdf_path.with_name(f"{pdf_path.stem}_pages.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, ensure_ascii=False, indent=2)

    print(f"[+] Extracted {len(pages_data)} pages → saved to: {out_path}")

# Example run
if __name__ == "__main__":
    extract_pdf_to_json("checklist.pdf")
