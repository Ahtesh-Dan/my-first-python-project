server=["aws-prod-01","azure-app-02","gcp-db03","backup-srv-03"]
for s in server:
    if s=="maintenance_server":
        print(f"Maintenance chal rha server skip kar diya{s}....")
        continue
    print(f"scanning server:{s}")
server=[{"name":"aws-prod-01","status":"active","cpu":45},{"name":"azure-app-02","status":"maintenance","cpu":95},{"name":"gcp-db-03","status":"active","cpu":92},{"name":"back-up-server","status":"active","cpu":30}]
for s in server:
    if s["status"]=="maintenance":
        print(f"⚠️ {s['name']} maintenance par hai, skip kar diya!")
        continue
    if s["cpu"]>90:
        print(f"🚨 CRITICAL ALERT! {s['name']} ka CPU load {s['cpu']}% hai!")
    else:
        print(f"🟢 {s['name']} smoothly chal raha hai ({s['cpu']}%).")
print("--- ✅ SCAN COMPLETE ---") 