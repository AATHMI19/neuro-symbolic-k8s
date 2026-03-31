def get_user_input():
    print("\n🔹 Enter Application Details 🔹")

    app_name = input("Enter application name: ").strip().lower().replace(" ", "-")
    num_services = int(input("Enter number of services: "))

    services = []

    for i in range(num_services):
        print(f"\n--- Service {i+1} ---")

        name = input("Service name: ")
        image = input("Docker image (e.g., nginx:latest): ")

        port = int(input("Port: "))
        if port < 1 or port > 65535:
            print("Invalid port. Defaulting to 80")
            port = 80

        replicas = int(input("Replicas: "))

        exposure = input("Exposure (ClusterIP/NodePort/LoadBalancer): ")
        if exposure not in ["ClusterIP", "NodePort", "LoadBalancer"]:
            print("Invalid exposure type. Defaulting to ClusterIP")
            exposure = "ClusterIP"

        service = {
            "name": name,
            "image": image,
            "port": port,
            "replicas": replicas,
            "exposure": exposure
        }

        services.append(service)

    config = {
        "application": app_name,
        "services": services
    }

    return config