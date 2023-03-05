FROM python:3.11

COPY . ./app

WORKDIR /app

RUN apt-get update -y && \
    apt-get upgrade -y 

RUN pip3 install -r requirements.txt

CMD pytest --alluredir=/app/allure_reports .
