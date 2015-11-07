# Demo for my OpenAlt 2015 OCI talk


## HAProxy setup

Build image and make it avaiable for `runc`:

```
$ docker build --tag=$USER/haproxy ./haproxy/
$ sudo mkdir -p /opt/containers/haproxy/rootfs
$ docker export $(docker create $USER/haproxy) | sudo tar -C /opt/containers/haproxy/rootfs -x
```

Let's create a proper runc container now:

```
$ sudo -c "cd /opt/containers/haproxy && runc spec"
```

set args in `config.json` to

```
"args": [
    "haproxy", "-d", "-f", "/ha.cfg"
],
```

Check HAProxy status

```
$ firefox http://localhost:1936/
```

## Spawn httpd containers

```
$ ./run.py
```

## Do some requests


```
$ ./bombard.py
```

Or with curl

```
for x in `seq 1 3` ; do (while true : ; do curl -s http://localhost/ >/dev/null ; done)& done
```
