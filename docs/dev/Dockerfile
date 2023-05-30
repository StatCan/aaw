FROM python:3-alpine

RUN apk add \
      graphviz \
      font-noto \
      font-noto-emoji \
    && pip install diagrams

ARG USER=diagrams

# add new user
RUN adduser -D $USER

USER $USER
WORKDIR /tmp

# docker run -v $(pwd):/tmp/ <image> diagram.py
ENTRYPOINT ["python"]