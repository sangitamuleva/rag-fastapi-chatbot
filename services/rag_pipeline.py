from services.embedding import embed_text
from services.retriever import retrieve
from services.llm_service import generate_answer


# after build contex  generate answer from that context
def rag_pipeline_generate(query:str):
    # step 1 embed query
    query_embedding=embed_text(query)

    #step 2 retrieve relevant chunks
    retrieved_docs=retrieve(query_embedding,k=3)

    #step 3 Build context
    context = "\n\n".join([docs['content'] for docs in retrieved_docs])

    #step 4 Generate final Answer
    answer =generate_answer(query,context)

    return answer