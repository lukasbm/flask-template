FROM python:3.8-alpine

WORKDIR /home/<APP_NAME>

# get python ready
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

# copy actual app
COPY app app
COPY server.py server.py

ENV FLASK_APP server.py

EXPOSE 5000
ENTRYPOINT gunicorn -b localhost:5000 --workers=3 --timeout=90 --graceful-timeout=30 --log-level=DEBUG --access-logfile - --error-logfile - server:app
