# Steps to setup E2E deployment using Jenkins, Ansible, Docker Swarm

- Clone the repo in the `/home` (make sure to clone it there, as we will be creating symlink assuming this) folder of the server and run `jenkins-setup.sh` 

```
cd scripts
chmod +x jenkins-setup.sh
./jenkins-setup.sh
```

- Go to localhost:8080 and follow the mentioned steps to create admin user and then install suggested plugins.

- Go to **Manage Jenkins -> Plugin Manager** and install **Copy Artifact**

- Run `jenkins-jobs-setup.sh`

```
cd scripts
chmod +x jenkins-job-setup.sh
./jenkins-job-setup.sh
```

- If the project is hosted on GitHub we would need ssh to connect to GitHub, in that case switch to jenkins user `su jenkins`
- Generate key-pair `ssh-keygen`
- Add private key to Jenkins and public key to GitHub
- Configure jobs to use the new credentials

- On the jenkins server setup a local registry

```
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```


- Run the following and add `jenkins ALL=(ALL) NOPASSWD: ALL` at the end
```
sudo visudo

```
