FROM python:3.10

WORKDIR /aplication

COPY requirements.txt /aplication/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /aplication/

ENV MONGODB_URI="45.79.205.185:27017"

EXPOSE 8000

CMD ["uvicorn", "app:api", "--port", "8000", "--host", "0.0.0.0"]