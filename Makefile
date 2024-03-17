run:
	python3 run.py

build:
	docker build -t pm:v1 .

docker-start:
	 docker run -it --publish=127.0.0.1:8000:8000 --publish=127.0.0.1:8001:8001 --name=pm pm:v1