FROM python:alpine

COPY . .

RUN pip install -r requirements.txt && \
     python manage.py makemigrations  && \
     python manage.py migrate

EXPOSE 8000/udp

CMD [ "python", "manage.py", "runserver" ,"0.0.0.0:8000" ]
