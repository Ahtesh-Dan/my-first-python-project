#server_logs = [
 #   "System Booting...",
  #  "All services running normally.",
   #x "User login successful.",
    #"CRITICAL: Database Connection Lost!",
    #"System trying to restart...",
    #"Sending email to admin..."
#]
#for server in server_logs:
 #   print(f'{server}')
  #  if server == "CRITICAL: Database Connection Lost!":
   #     print("🚨 EMERGENCY BRAKE: Stopping process! AI fixing error...")
    #    break
server_logs = [
    "DEBUG: Checking memory...",
    "WARNING: High CPU usage at 95%!",
    "DEBUG: Pinging network...",
    "ERROR: Application crashed suddenly!",
    "DEBUG: Clearing cache..."
]
for server in server_logs:
    if "DEBUG" in server:
        continue
    print(server)
    
  