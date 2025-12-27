import re
'''
Chunks document into 500 char segments with 100 character  overlap to preserve semantic context
With Overlap and chunks context will  preserved

'''
def clean_text(text:str):
    text=re.sub(r"\n+","\n",text)
    text=re.sub(r"\s+","",text)
    return text.strip()

def chunk_text(text:str,chunk_size=500,overlap=100):
    chunks=[]
    start=0
    text_length=len(text)
    while start<text_length:
        end=start+chunk_size
        chunk=text[start:end]
        chunks.append(chunk)
        start+=chunk_size - overlap
    return chunks
#
# def chunk_tables(table_rows):
#     return [f"Table Row:{row}" for row in table_rows if row.strip()]


def create_chunks_with_metadata(page_data):
    all_chunks = []
    for page in page_data:
        p_num=page["page"]
        p_text=clean_text(page["text"])
        if p_text:
            text_chunks=chunk_text(p_text)
            for c in text_chunks:
                all_chunks.append({
                    "content":c,
                    "page":p_num,
                    "type":"text"
                })

        for r in page["tables"]:
            if r.strip():
                all_chunks.append({
                    "content": f"Table Row:{r}",
                    "page": p_num,
                    "type": "table"
                })
    return all_chunks
