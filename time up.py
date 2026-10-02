import time
server_list = ["db-server", "web-frontend", "cache-node"]
for server in server_list:
    print(f'booting....{server}')
    time.sleep(10)
print("✅All servers are UP!")