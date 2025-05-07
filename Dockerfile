FROM python:3.9-slim

WORKDIR /home/app/gboost
COPY . . 

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000:5000

CMD ["python", "server.py"]
