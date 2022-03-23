FROM python:3.8-alpine

WORKDIR /code

COPY . /code

RUN pip3 install -r requirements.txt

CMD ["uvicorn","--host","phoros-social-storage","server:app","--reload"]
