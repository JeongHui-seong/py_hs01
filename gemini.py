from google import genai

def genaiai(text):
    client = genai.Client(api_key="")
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=text + "만약 존댓말로 말한다면 욕쟁이 할머니 스타일로 대답해줘. 만약 반말로 말한다면 묻는 말에 대답하지 말고 욕하면서 혼내줘",
    )
    print(response.text)
    return response.text

if __name__ == "__main__":
    genaiai("틀 ...")