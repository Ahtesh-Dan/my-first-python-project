active_servers=["Alpha","Beta","Gama"]
print("Mere active servers ki list hai:",active_servers)
print("mera dusra server hai:",active_servers[1])
active_servers.append("omega")
print("mere activer servers ki list hai:",active_servers)
active_servers.remove("Alpha")
print("Alpha server crash! ho gya mere active server ki list hai:",active_servers)
print(len(active_servers))
for servers in active_servers:
    print("servers check:",servers,"is Running🟢")