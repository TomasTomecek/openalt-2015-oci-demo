FROM fedora:22
RUN dnf install -y httpd
RUN sed -i -e "/^Listen.*/d" /etc/httpd/conf/httpd.conf
EXPOSE 8000
CMD httpd -DFOREGROUND -c "Listen 8000"
