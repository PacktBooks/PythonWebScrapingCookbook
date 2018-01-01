FROM registry.opensource.zalan.do/stups/python:3.5.2-38

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY ../09/01/app.py /
COPY ../09/01/swagger.yaml /

WORKDIR /data
CMD /app.py