test

```
for x in `seq 1 3` ; do (while true : ; do curl -s http://192.168.0.11/ >/dev/null ; done)& done
```

run haproxy

```
docker run --rm --net=host haproxy
```

run nginx

```
docker build --tag=nginx .
python run_64_containers.py
```

run httpd

```
httpd -DFOREGROUND -c "Listen 8000"
```
