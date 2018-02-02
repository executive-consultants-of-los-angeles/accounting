FROM alpine:3.7
RUN apk update
RUN apk add python3; ln -sf /usr/bin/python3 /usr/bin/python
RUN apk add wget
RUN wget https://bootstrap.pypa.io/get-pip.py; python get-pip.py; rm get-pip.py; ln -sf /usr/bin/pip3 /usr/bin/pip
RUN apk add git
RUN git clone https://github.com/gahan-corporation/newhart.git /srv/newhart
ENV DJANGO_SETTINGS_MODULE newhart.settings
RUN pip install -r /srv/newhart/.requirements
EXPOSE 8000
CMD /srv/newhart/newhart/manage.py runserver 0.0.0.0:8000
