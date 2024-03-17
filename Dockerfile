FROM python:3.10
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update
RUN apt install net-tools

ENV NAME pm

EXPOSE 8000
EXPOSE 8001

CMD ["python", "./run.py"]