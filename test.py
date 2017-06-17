#coding: utf-8
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import urllib2
import requests
import os
import re
import time
def test_url(url):
    website = urllib2.urlopen(url) #返回一个类文件对象,为指定的URL创建一个类似文件的对象 
    html = website.read()#读取整个文件
    links = re.findall('"((http|ftp)s?://.*?)"', html)
    num = len(links)
    for i in num:
        urls = links[i][0]
        file_object = open(r"C:\Users\CWT62\Desktop\url.txt", 'a')
        file_object.write(urls + "\n")
        file_object.close()
if __name__ == "__main__":
    url = "https://m.ut.bl.com/h5-web/together/goSpellGroup.html"
    test_url(url)
#此处增加备注
