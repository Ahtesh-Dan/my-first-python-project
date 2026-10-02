temp_data = [
    {"device": "router-1", "temp": 70},
    {"device": "core-switch", "temp": 92},
    {"device": "firewall", "temp": 65},
    {"device": "db-server", "temp": 89}]
danger_count=0
alert_list=[]
for temperature in temp_data:
    if temperature["temp"] >85:
        danger_count=danger_count+1
        alert_list.append (temperature["device"])
print(f'🔥 THERMAL ALERT: {danger_count} devices are overheating!')
print(f'🚨 Dispatching cooling team to: {alert_list}')