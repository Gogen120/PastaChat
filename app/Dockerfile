FROM python:3.6

COPY ./pasta_chat pasta_chat/

WORKDIR pasta_chat/

ENV TZ Europe/Moscow

ENV FLASK_APP=pasta_chat
ENV FLASK_DEBUG=1
ENV FLASK_PORT=80

ENV SQLALCHEMY_MAX_OVERFLOW=20
ENV SQLALCHEMY_POOL_SIZE=20

RUN pip install -r requirements.txt
RUN pip install --upgrade setuptools

ENTRYPOINT ["flask"]
CMD ["run", "-p", "80", "-h", "0.0.0.0"]