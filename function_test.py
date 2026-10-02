def check_server(server_name):
    print(f"scanning {server_name}")
    print(f"{server_name} is running perfectly!")
    print("------------------------------------")
check_server("aws-prod-01")
check_server("gcp-database-03")
check_server("azure-app-02")    