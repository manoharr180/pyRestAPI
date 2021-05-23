# syntax=docker/dockerfile:1

FROM python:3.7

WORKDIR /app

COPY "C:/Users/Manohar R/PycharmProjects/Beginners/pyRestAPI/requirements.txt" .
RUN pip3 install -r requirements.txt

COPY "C:/Users/Manohar R/PycharmProjects/Beginners/pyRestAPI/src/" .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]