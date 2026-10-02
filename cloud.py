cloud_server={"name":"aws-prod-01","region":"Mumbai","cpu_usage":85}
print("Server ki details yeh hain:",cloud_server)
print(cloud_server["region"])
cloud_server["cpu_usage"]=90
cloud_server["status"]="Active"
print("Updated Server Status Report:",cloud_server)
