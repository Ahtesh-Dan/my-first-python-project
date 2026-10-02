import requests
response= requests.get("https://official-joke-api.appspot.com/random_joke")
if response.status_code == 200:
  print("✅ Connection Successful! Firewall bypassed.\n")
  live_data=response.json()
  print(f"🤖 Setup: {live_data['setup']}")
  print(f"💥 Punchline: {live_data['punchline']}")
else:
    print("❌ Connection Failed!")