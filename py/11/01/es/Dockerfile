FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.4
ENV REGION us-west-2
ADD elasticsearch.yml /usr/share/elasticsearch/config/
USER root
RUN chown elasticsearch:elasticsearch config/elasticsearch.yml
USER elasticsearch
WORKDIR /usr/share/elasticsearch
RUN bin/elasticsearch-plugin install discovery-ec2 && bin/elasticsearch-plugin install repository-s3 && sed -e '/^-Xm/s/^/#/g' -i /usr/share/elasticsearch/config/jvm.options
