import docker

client = docker.from_env()

#run containers
client.containers.run("bfirsh/reticulate-splines", detach=True)