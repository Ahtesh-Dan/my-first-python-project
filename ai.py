from google import genai
client=genai.Client(api_key="Mera Password")
print("AI se contact kiya ja rha hai......please wait.....")
response = client.models.generate_content(
    model="gemini-3.8-flash", 
    contents="Hello AI, main ek mechanical engineer hoon jo abhi cloud aur AI seekh raha hai. Mujhe Hindi mein ek choti si motivational line kaho!"
)
print("\n AI ka Jawab:")
print("--" * 50)
print(response.text)
print("--" * 50)