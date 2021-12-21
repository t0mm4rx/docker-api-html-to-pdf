FROM ubuntu:20.04

ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update
RUN apt-get install -y wkhtmltopdf python3.9 python3-pip

COPY ./api /root/api

WORKDIR /root/api

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "api.py"]