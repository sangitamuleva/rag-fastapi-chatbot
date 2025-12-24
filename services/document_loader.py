import pdfplumber
'''Load file and read text and tables.
tables are flattedned into textual rows so they can be embedded and indexed for RAG
'''
def load_pdf(path:str):
    page_data=[]
    with pdfplumber.open(path) as pdf:
        for page_num , page in enumerate(pdf.pages,start=1):
            p_text = page.extract_text() or ''
            p_table=page.extract_table() or []

            table_text=[]
            for table in p_table:
                for row in table:
                    clean_row=[cell if cell else '' for cell in row]
                    table_text.append(" ".join(clean_row))

            page_data.append({
                "page":page_num,
                "text":p_text,
                "tables":table_text
            })
    return page_data


    return docs
