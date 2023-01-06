FROM python:3.9-alpine

WORKDIR /usr/src/app

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1


RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \

    apk add --update --no-cache --virtual  build-dependencies \
    file make gcc g++ musl-dev libffi-dev openssl-dev curl gpgme && \
    apk add --update --no-cache --virtual run-dependencies \
    rm -rf /tmp &&

COPY requirements.txt requirements.txt

RUN \
    pip install --no-cache-dir -r requirements.txt && \
    # Delete packages needed only on build time
    apk del --update --no-cache build-dependencies

COPY . .

RUN \
    touch /usr/src/app/storage/app/database.sqlite

CMD ["python", "./main.py"]
