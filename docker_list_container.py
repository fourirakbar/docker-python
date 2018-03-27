import docker

client = docker.from_env()
print_client = client.containers.list()
print print_client