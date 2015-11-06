FROM fedora:22
RUN dnf install -y httpd
EXPOSE 8000
CMD httpd -DFOREGROUND -c "Listen 8000"
