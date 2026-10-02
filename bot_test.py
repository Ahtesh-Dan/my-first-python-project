import time
def reboot_server(server_name):
    print(f'Bot:Initiating reboot for {server_name}')
    time.sleep(5)
    print(f"{server_name} is back Online..............")
(reboot_server("payment-gateway-01"))    
(reboot_server("database-02"))