storage_data = [{"server": "db-01", "disk_usage": 85},{"server": "app-backend", "disk_usage": 45},{"server": "web-frontend", "disk_usage": 92},{"server": "cache-server", "disk_usage": 60}]
disk_space=0
full_storage=[]
for storage in storage_data:
    if  storage ["disk_usage"]>80:
        disk_space=disk_space+1
        full_storage.append(storage["server"])
print(f"🚨 WARNING: {disk_space} servers are critically full!")
print(f"🛠️ Please clear space in: {full_storage}")
        

   


