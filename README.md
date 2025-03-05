# ELS MWAA 2025

## Please follow below steps for preparing your MWAA local runner environment

Launch Amazon Linux 2023 instance

- Architecture: 64-bit (x86)
- Instance type: t2.xlarge
- Storage: 100 GiB (gp3)

Connect to your Linux instance using an SSH client

```shell script
ssh -i key-pair.pem ec2-user@ec2-x-x-x-x.compute-1.amazonaws.com
```

Install docker and git package
```shell script
sudo yum update -y
sudo yum install -y docker git
sudo service docker start
sudo usermod -a -G docker ec2-user

DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.32.4/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
exit
```

Reconnect to your Linux instance

```shell script
ssh -i key-pair.pem ec2-user@ec2-x-x-x-x.compute-1.amazonaws.com
```

Verify that the ec2-user can run Docker commands without using sudo

```shell script
docker ps
docker compose version
```
Clone mwaa-local-runner project from github

```shell script
git clone -b v2.10.3 https://github.com/aws/aws-mwaa-local-runner.git
```

Build docker image

```shell script
cd aws-mwaa-local-runner/
./mwaa-local-env build-image (around 5 minutes)
docker images
```
Start mwaa local runner environment

```shell script
./mwaa-local-env start
```

Open Airflow UI

- http://ec2-x-x-x-x.compute-1.amazonaws.com:8080/
- Username: admin
- Password: test

![](https://github.com/frankie-wy/els_mwaa_2025/blob/main/Airflow_UI.png)
