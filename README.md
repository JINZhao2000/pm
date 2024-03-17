# Business process project
## About the project
In this project, we will develop an asynchronous processing system using FastAPI. The system consists of two main components: a customer process for placing orders and a supplier process for managing order requests, generating quotes, and confirming orders.

## Dependencies
- Applications
  - Python
  - Docker and Docker compose
- Python packages
  - fastapi
  - pymysql
  - pika
  - pydantic
  - aiohttp
  - uvicorn
```bash
pip install --no-cache-dir -r requirements.txt
```
 
## Configurations
- In the file `./pm/utils/utils.py`, you can find 4 variables to configure the hosts and ports for client and provider. They are `localhost` and `8000`, `8001` by default.
- In the file `./pm/fournisseur/db.py`, there are configurations of MySQL database.
- In the file `./pm/fournisseur/mq.py`, there are configurations of RabbitMQ.
- In the file `./pm/tables.sql`, there are the instructions for tables.

 
## Run the project
First, start the RabbitMQ server:
```bash
docker compose create # first time
docker compose start
```
If you have GNU/make, use:
```
make run
```
or
```
python3 run.py
```
to start


## Build image
Before build the image, change the host in `./pm/utils/utils.py` to docker ip address, `172.17.0.2` for instance.
You can build docker image of this project with 
```bash
make build
```
or
```bash
docker build -t pm:v1 .
```
Then start the container
```bash
make docker-start 
```
or
```bash
docker run -it --publish=127.0.0.1:8000:8000 --publish=127.0.0.1:8001:8001 --name=pm pm:v1
 ```