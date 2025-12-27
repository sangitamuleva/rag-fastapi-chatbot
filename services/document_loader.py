import pdfplumber, re

'''Load file and read text and tables.
tables are flattedned into textual rows so they can be embedded and indexed for RAG
'''


def load_pdf(path: str):
    page_data = []
    with pdfplumber.open(path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            p_text = page.extract_text() or ''
            p_table = page.extract_table() or []

            table_text = []
            if p_text:
                p_text = p_text.strip()
            if p_table:
                # for table in p_table:
                #     if not table:
                #         continue
                for row in p_table:
                    if not row:
                        continue
                    clean_row = [
                        normalize_pdf_cell(cell)
                        for cell in row
                        if cell and isinstance(cell, str)
                    ]

                    if clean_row:
                        table_text.append(" ".join(clean_row))

            page_data.append({
                "page": page_num,
                "text": p_text,
                "tables": table_text
            })
    return page_data

    return docs


def normalize_pdf_cell(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()

    # Fix spaced letters
    text = re.sub(
        r"(?:\b[A-Za-z]\b\s+){2,}\b[A-Za-z]\b",
        lambda m: m.group(0).replace(" ", ""),
        text
    )

    # Fix spaced digits
    text = re.sub(
        r"(?:\b\d\b\s+){2,}\b\d\b",
        lambda m: m.group(0).replace(" ", ""),
        text
    )

    return text
