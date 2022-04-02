FROM python:3.8-alpine

WORKDIR /code

COPY . /code

# # uncomment If you want to start websockets mission
# # for the uvloop won't compile issue
# RUN apk add build-base
# RUN pip3 install fastapi "uvicorn[standard]"

RUN pip3 install -r requirements.txt

# ,"--ssl-keyfile","certificate.key","--ssl-certfile","certificate.crt"
CMD ["uvicorn","--host","0.0.0.0","server:app","--reload"]
