#coding:utf-8
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from page import login_page,home_page
from public import setting
import unittest
import os


class Test(unittest.TestCase):
    def setUp(self):
        chromedriver = "D:\\Program Files (x86)\\Python\\chromedriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        #去掉ignore-certificate-errors
        options = webdriver.ChromeOptions()  #进入浏览器设置
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        #driver= webdriver.Chrome(chromedriver,chrome_options=options)
        #加载手机模式
        mobile_emulation = { "deviceMetrics": {"width": 375, "height": 667, "pixelRatio": 3.0}, #  定义设备高宽，像素比 
                    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) " # 通过ua来模拟 
                    "AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"} 
        chrome_options = Options() 
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(chromedriver,chrome_options = chrome_options)
        self.driver.maximize_window()
        #self.base_url = "http://m.bl.com/h5-web/member/view_login.html"
        
    def test_login(self):
        '''测试登录'''
        driver = self.driver
        driver.get(setting.data.home_url)
        home_page.First_page.click_my(self)
        login_page.index_page.input_username(self,setting.data.username)
        login_page.index_page.input_password(self,setting.data.password)
        login_page.index_page.click_submit(self)
        
    def tearDown(self):
        driver = self.driver
        driver.quit()

# if __name__ == '__main__':
#     unittest.main()        
        