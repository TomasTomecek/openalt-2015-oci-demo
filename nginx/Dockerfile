FROM fedora:22
RUN dnf install -y nginx
EXPOSE 80
# COPY ha.conf /etc/nginx/conf.d/
RUN printf "daemon off;\nhttp { error_log /dev/stdout debug;\naccess_log /dev/stdout;\n}" >>/etc/nginx/nginx.conf
CMD nginx
