FROM python:3.6

COPY . app/

WORKDIR app/

ENV TZ Europe/Moscow

ENV FLASK_APP=pasta_chat
ENV FLASK_DEBUG=1
ENV FLASK_PORT=80

ENV SQLALCHEMY_MAX_OVERFLOW=20
ENV SQLALCHEMY_POOL_SIZE=20

RUN pip install -r requirements.txt

ENTRYPOINT ["flask"]
CMD ["run", "-p", "80", "-h", "0.0.0.0"]