def server_ping(server_name,status):
    print(f"scanning server current status {status}")
    if status =="online":
        print(f"{server_name} running perfectly")
    else:
        print(f"{server_name} server is down")
server_data=[{"name":"aws-prod-01","status":"online"},{"name":"azure-db-01","status":"offline"},{"name":"gcp-web-02","status":"online"},{"name":"backup-srv","status":"offline"}]
down_count=0
broken_servers=[]
for server in server_data:
    server_ping(server["name"], server["status"])
    if server["status"]=="offline":
        down_count=down_count+1
        broken_servers.append(server["name"])
print(f"🚨 FINAL REPORT: Total {down_count} servers are DOWN!")
print(f"🛠️ Servers to fix: {broken_servers}")