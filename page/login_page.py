#coding:utf-8
from selenium import webdriver
from public import common


class index_page:
    
    xpath_goregister = "//a[@class='new-login-right']" #注册按钮
    xpath_login_button = '//*[@id="loginButton"]' #H5登录LoginButton
    xpath_accountlogin= '//*[@id="normalLogin"]' #H5账户密码登录标签    
    id_codelogin = '//*[@id="codeLoin"]'  #H5手机动态密码登录标签
    id_mobile = '//*[@id="mobile"]' #手机动态密码登录-手机号请输入手机号码标签栏
    # id_rand = '//*[@id="rand"]' #手机动态密码登录下面-验证码
    id_rand = '//div[@class="new-login-item-right pr"]/input'
    id_loginname = '//*[@id="lgoinName"]' #输入账号的text框
    id_pwd = '//*[@id="pwd"]' #输入密码的text框
    id_isKeep = '//*[@id="isKeep"]'#两周内免登陆按钮
    '''在方法上必须加个@staticmethod 在其他地方调用的话可以直接 modul.f()'''
    @staticmethod
    def input_username(self,username):
        '''输入用户名'''
        driver = self.driver
        common.commom.time_out(self)
        driver.find_element_by_xpath(index_page.id_loginname).clear()
        driver.find_element_by_xpath(index_page.id_loginname).send_keys(username)
    
    @staticmethod
    def input_password(self,password):
        '''输入密码'''
        driver = self.driver
        driver.find_element_by_xpath(index_page.id_pwd).clear()
        driver.find_element_by_xpath(index_page.id_pwd).send_keys(password)
    
    @staticmethod
    def click_submit(self):
        '''点击登录按钮'''
        driver = self.driver
        common.commom.time_out(self)
        driver.find_element_by_xpath(index_page.xpath_login_button).click()
        
    @staticmethod
    def click_iskeep(self):
        '''点击保持2周登录'''
        driver = self.driver
        common.commom.time_out(self)
        driver.find_element_by_xpath(index_page.id_isKeep).click()
        
    @staticmethod
    def click_register(self):
        '''点击注册按钮'''
        driver = self.driver
        driver.find_element_by_xpath(index_page.xpath_goregister).click()
        
    @staticmethod
    def click_mobile_login(self):
        '''点击手机动态密码登录'''
        driver = self.driver
        driver.find_element_by_xpath(index_page.id_codelogin).click()
        
        
    
    
        
        
        
        
        
    