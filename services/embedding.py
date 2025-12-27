'''GENai  create embbeding model (not free tier) '''
# from google import genai
# import config
#
# client = genai.Client(api_key=config.AI_API_KEY)
#
# model = "gemini-2.5-flash-lite"
#
# def embed_text(text: str):
#     response = client.models.embed_content(
#         model="models/embedding-001",
#         contents=text
#     )
#     return response["embeddings"]


# Local embedding for testing
from sentence_transformers import SentenceTransformer
model=SentenceTransformer("all-MiniLM-L6-v2")
def embed_text(text: str):
    response = model.encode(
        text,
        convert_to_tensor=True,
        normalize_embeddings=True,
    )
    return response
