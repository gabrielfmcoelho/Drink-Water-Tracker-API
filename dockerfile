FROM python:3.10

WORKDIR /aplication

COPY requirements.txt /aplication/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /aplication/

EXPOSE 8001

CMD ["uvicorn", "app:api", "--reload", "--port", "8001", "--host", "0.0.0.0"]