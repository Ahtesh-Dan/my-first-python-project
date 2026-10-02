def cool_down(server_name,temperature):
    print(f"scanning server temperature {temperature}")
   # print(f"scanning server temperature is under control{server_name}")
    while temperature > 40:
        print(f"cooling server{server_name}...current temperature {temperature}")
        temperature=temperature-10
    print(f"server {server_name} is now stable!")
cool_down("aws-prod-01",90)
cool_down("azure-web",70)