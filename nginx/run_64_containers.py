import subprocess

for x in range(8000, 8064):
    cmd = [
        "docker",
        "run",
        "-d",
        "-p",
        "%s:80" % x,
        "nginx"
    ]
    subprocess.check_call(cmd)

