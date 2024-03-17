# Business process project
## About the project
In this project, we will develop an asynchronous processing system using FastAPI. The system consists of two main components: a customer process for placing orders and a supplier process for managing order requests, generating quotes, and confirming orders.

## Dependencies
- Applications
  - Python
  - Docker compose
- Python packages
  - fastapi
  - pymysql
  - pika
  - pydantic
  - aiohttp
  - uvicorn
  - threading
 
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
