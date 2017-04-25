FROM python
ENV PYTHONBUFFERED 1

RUN mkdir /project
WORKDIR /project

ADD requirements.txt /project/requirements.txt
RUN pip install -r requirements.txt

ADD . /project

EXPOSE 8000

