FROM python:3.11-slim 
WORKDIR /app
RUN apt-get update && apt-get upgrade -y && apt-get clean
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt
COPY  app  /app/
COPY app_entrypoint.sh /app
CMD [ "./app_entrypoint.sh" ]
# python:3.11.3