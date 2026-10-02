server_fleets=[{"name":"aws-pord-01","region":"mumbai","cpu_usage":85},
{"name":"Azure-app-02","region":"singapore","cpu_usage":95},
{"name":"GCP-DB-03","region":"Frankfurt","cpu_usage":80}]
print("------cloud syestem INTIALIZED")
for server in server_fleets:
    server_name=server["name"]
    region=server["region"]
    usage=server["cpu_usage"]
    if usage>90:
        print(f"🚨 CRITICAL ALERT! Server: {server_name} ({region}) ka CPU load {usage}% hai! Immediate Action Required!")
    elif usage>70:
        print(f"⚠️ WARNING: Server: {server_name} ({region}) par load high hai ({usage}%).")
    else:
        print(f"🟢 HEALTHY: Server: {server_name} ({region}) smoothly chal raha hai ({usage}%).")
print("--- ✅ SCAN COMPLETE: All systems checked! ---")