FROM python:3.11-alpine as base-image

ENV PYTHONUNBUFFERED 1

WORKDIR /project

RUN apk update && apk add --no-cache gcc g++ musl-dev make zlib-dev

RUN python -m pip install -U pip setuptools wheel pdm

COPY pyproject.toml pdm.lock ./
RUN pdm install --dev --no-lock --no-editable --no-self
COPY main.py Makefile ./

COPY src ./src

CMD ["make", "start"]
