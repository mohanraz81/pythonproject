FROM centos:7
RUN yum -y update
RUN yum -y install python
RUN yum -y install  git curl wget httpd 
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"; python get-pip.py
RUN pip install flask boto3 ec2-metadata
RUN yum -y install mod_wsgi.x86_64
ADD config/archeplay.conf /etc/httpd/conf.d/archeplay.conf
RUN echo '200 Ok' > /var/www/html/status.html
ENV AWS_REGION=us-east-1
RUN echo 'export TableName=mytable' > /etc/environment
ADD code /var/www
CMD ["httpd", "-D", "FOREGROUND"]