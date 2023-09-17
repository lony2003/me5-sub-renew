import os
import json
import time
from typing import Tuple
import requests
from bs4 import BeautifulSoup
from Crypto.Cipher import DES3
import base64
import binascii
from pysmx.SM3 import digest
import hashlib
import urllib.parse
import random
from requests.adapters import HTTPAdapter
import uuid

#snowland-smx
#pycryptodome

def getDES3Token(text, key):
    #PKCS5Padding
    #字符串长度需要是8的倍数
    BS = 8
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    unpad = lambda s : s[0:-ord(s[-1])]
    #注意3DES的MODE_CBC模式下只有前24位有意义
    #key和iv都需要是bytearray
    
    iv = b'01234567'
    #text也需要encode成bytearray
    plaintext = pad(text).encode()
    #使用MODE_CBC创建cipher
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    #加密
    result = cipher.encrypt(plaintext)
    result = binascii.b2a_hex(result)
    result = str(result, 'utf-8')
    return result.upper()
    
def getSM3Token(text):
    result = digest(text)
    result = binascii.b2a_hex(result)
    result = str(result, 'utf-8')
    return result
    
def getMD5Token(text):
    return hashlib.md5(text.encode(encoding="UTF-8")).hexdigest().upper()
    
def get_province_code(user_province):
    provinces = {}
    provinces["北京市"] = "110000"
    provinces["天津市"] = "120000"
    provinces["河北省"] = "130000"
    provinces["山西省"] = "140000"
    provinces["内蒙古自治区"] = "150000"
    provinces["辽宁省"] = "210000"
    provinces["吉林省"] = "220000"
    provinces["黑龙江省"] = "230000"
    provinces["上海市"] = "310000"
    provinces["江苏省"] = "320000"
    provinces["浙江省"] = "330000"
    provinces["安徽省"] = "340000"
    provinces["福建省"] = "350000"
    provinces["江西省"] = "360000"
    provinces["山东省"] = "370000"
    provinces["河南省"] = "410000"
    provinces["湖北省"] = "420000"
    provinces["湖南省"] = "430000"
    provinces["广东省"] = "440000"
    provinces["广西壮族自治区"] = "450000"
    provinces["海南省"] = "460000"
    provinces["重庆市"] = "500000"
    provinces["四川省"] = "510000"
    provinces["贵州省"] = "520000"
    provinces["云南省"] = "530000"
    provinces["西藏自治区"] = "540000"
    provinces["陕西省"] = "610000"
    provinces["甘肃省"] = "620000"
    provinces["青海省"] = "630000"
    provinces["宁夏回族自治区"] = "640000"
    provinces["新疆维吾尔自治区"] = "650000"
    provinces["台湾省"] = "710000"
    provinces["香港特别行政区"] = "810000"
    provinces["澳门特别行政区"] = "820000"
    return provinces[user_province]


if __name__ == "__main__":

    days = open("days", "w")
    days.write(str(uuid.uuid4()))
    days.close()

    print('*' * 30)
