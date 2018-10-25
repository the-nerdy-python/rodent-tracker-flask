#Dockerfile for flask containerization
FROM python:3.6
MAINTAINER Brian Hopkins "thenerdypython@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
