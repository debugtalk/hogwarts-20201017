import time
import hashlib
import random


from httprunner import __version__
from httprunner.response import ResponseObject


def get_httprunner_version():
    return __version__


def gen_member_id():
    return "2753800615995680"


def gen_token(phone, password, timestamp):
    s = "".join([phone, password, str(timestamp)])
    token = hashlib.md5(s.encode("utf-8")).hexdigest()
    print(f"token: {token}")
    return token


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def get_folders_num(response: ResponseObject):
    resp_json = response.resp_obj.json()
    folders = resp_json["data"]["folders"]
    return len(folders)


def gen_random_title():
    return f"demo-{random.randint(1, 9999999)}"
