cpu_metrics=[{"servers":"node_alpha","cpu":5},{"servers":"node-beta","cpu":45},{"servers":"node-gamma","cpu":8},{"servers":"node-delta","cpu":88}]
idle_count=0
shut_down_list=[]
for server_data in cpu_metrics:
    if server_data["cpu"] < 10:
        idle_count = idle_count + 1
        shut_down_list.append(server_data["servers"])
print(f"💰 OPTIMIZATION REPORT: Found {idle_count} idle servers wasting money!")
print(f"Initiating shutdown for: {shut_down_list}")

