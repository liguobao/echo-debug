from logging import log
import requests
from loguru import logger
from urllib.parse import quote
import time


def user_login():
    url = "http://aoba.vip:8999/echo-api/user-info/login"
    payload = 'userName=admin&password=admin'
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'token': 'undefined',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://aoba.vip:8999',
        'Referer': 'http://aoba.vip:8999/sign-in',
        'Accept-Language': 'EN',
        'x_identify_user': 'test'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()["data"]["loginToken"]


def refresh_token(login_token):
    url = "http://aoba.vip:8999/echo-api/user-info/refreshToken"
    payload = {}
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'token': login_token,
        'Referer': 'http://aoba.vip:8999/dashboard',
        'Accept-Language': 'EN',
        'x_identify_user': 'test'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        logger.error(f"refresh_token fail,response:{response.text}")
        return None


def send_command_to_client(client_id, refresh_token, action="ShizukuReDial"):
    url = f"http://aoba.vip:4826/echo-api/nat-mapping-server/sendCommandToClient?clientId={quote(client_id)}&action={action}&additionParam=whoami&token={refresh_token}"
    response = requests.request("GET", url, headers={})
    logger.info(
        f"{action} finish,client_id:{client_id},response:{response.text}")


def get_connection_list():
    url = "http://aoba.vip:4826/echoNatApi/connectionList?serverId=echo-http-proxy-001"
    response = requests.request("GET", url, headers={})
    if response.status_code == 200:
        return response.json()["clients"]
    else:
        logger.error(f"get_connection_list fail,response:{response.text}")
        return []


def get_proxy_resources():
    url = "http://aoba.vip:8999/echo-api/proxy-resource/query?Token=401cf685-cccf-4819-a3a7-a0494847ce81&size=10&random=false&detail=true"
    response = requests.request("GET", url, headers={})
    if response.status_code == 200:
        return response.json()["data"]
    else:
        logger.error(f"get_connection_list fail,response:{response.text}")
        return []


def check_client_id(client_id, check_count=5):
    for index in range(0, check_count):
        connection_list = get_connection_list()
        connection_clients = [x["clientId"] for x in connection_list]
        if client_id in connection_clients:
            logger.error(f"connection_client:{client_id} offline fail")
        else:
            logger.warning(
                f"connection_client:{client_id} offline successfully.")
        proxy_resources = get_proxy_resources()
        proxy_clients = [x["clientId"] for x in proxy_resources]
        if client_id in proxy_clients:
            logger.error(f"proxy_client:{client_id} offline fail")
        else:
            logger.warning(f"proxy_client:{client_id} offline successfully.")
        time.sleep(1)
        logger.info(f"check_client_id finish,index:{index},sleep 1s finished")


client_id = "admin|@--@--@|353626072983559_1814"
login_token = user_login()


def sleep_seconds(second):
    logger.info(f"sleep {second}s start")
    for i in range(0, second):
        logger.info(f"sleep {i+1}s ...")
        time.sleep(1)


while True:
    admin_token = refresh_token(login_token)
    if not admin_token:
        logger.info("sleep 2s")
        time.sleep(2)
        continue
    send_command_to_client(client_id, admin_token)
    check_client_id(client_id, 5)
    sleep_seconds(10)
