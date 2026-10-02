server="aws-prod-01"
temperature=80
while temperature<=100:
    print(f"server is scanning{temperature}")
    if   temperature== 95:
        print("warning! server heating ")
    elif temperature == 100:
        print("critical!server is shutdown")
        break
    temperature=temperature+5

    

