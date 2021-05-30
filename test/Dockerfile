# syntax=docker/dockerfile:1

FROM python:3.7.10

WORKDIR /code

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY  src/ .

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD [ "python", "startup.py", "--host=0.0.0.0"]