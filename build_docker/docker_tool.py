import subprocess

REMOTE_IMAGE_NAME = "registry.cn-hangzhou.aliyuncs.com/face-service/basic-service"
version = "1.0.0"

LOGIN_USERNAME = ""
LOGIN_PASSWORD = ""
LOGIN_URL = "registry.cn-hangzhou.aliyuncs.com"


def call_shell(cmd):
    print(cmd)
    print(subprocess.call(cmd, shell=False))


def push_docker_image(ver):
    cmd1 = "docker build -t tempbuild:%s ." % ver
    call_shell(cmd1)

    cmd2 = "docker tag tempbuild:%s %s:%s" % (ver, REMOTE_IMAGE_NAME, ver)
    call_shell(cmd2)

    cmd3 = "docker push %s:%s" % (REMOTE_IMAGE_NAME, ver)
    call_shell(cmd3)


def login_docker(username, password, url):
    call_shell("docker login --username=%s %s --password=%s" % (username, url, password))


login_docker(LOGIN_USERNAME, LOGIN_PASSWORD, LOGIN_URL)
push_docker_image(version)
