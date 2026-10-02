cpu_metrics = [{"server": "node-alpha", "cpu": 5},{"server": "node-beta", "cpu": 45},{"server": "node-gamma", "cpu": 8},{"server": "node-delta", "cpu": 88}]
idle_count=0
shut_down_list=[]
for server_data in cpu_metrics:
    idle_count=idle_count+1
    shut_down_list.append(server_data["server"])
print(f"💰 OPTIMIZATION REPORT: Found {idle_count} idle servers wasting money!")
print(f"Initiating shutdown for: {shut_down_list}")