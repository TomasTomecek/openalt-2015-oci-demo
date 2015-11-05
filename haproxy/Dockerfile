FROM fedora:22
RUN dnf install -y haproxy
COPY ha.cfg /
CMD haproxy -d -f /ha.cfg
