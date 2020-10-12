FROM centos:7

MAINTAINER Siva Undavalli "prakashundavalli@gmail.com"

RUN yum update -y && \
    yum -y install epel-release && yum clean all && yum clean all && \
    yum install -y python-pip python-dev python3 &&\
    pip install --upgrade pip
    

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python"]

CMD ["get_metrics.py"]
