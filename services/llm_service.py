from google import genai
import config


client = genai.Client(api_key=config.AI_API_KEY)

model = "gemini-2.5-flash-lite"



def generate_answer(query,context):
    prompt = f"""Answer the question using ONLY the context below.
                Context:{context}
                Question:{query}
        """
    response = client.models.generate_content(model=model,
                                              contents=prompt)
    return response.text

