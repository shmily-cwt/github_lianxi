#coding:utf-8
from selenium import webdriver
from public import common
class First_page:
    
    xpath_bailian_shopping = "//div[contains(text(),'逛百联')]" #逛百联按钮
    xpath_first_medicine = "//div[contains(text(),'第一医药')]"  #第一医药按钮
    xpath_gift_card = "//div[contains(text(),'礼品卡')]"       #礼品卡按钮
    xpath_digital = "//div[contains(text(),'电器城')]"         #电器城按钮
    xpath_chinese = "//div[contains(text(),'特色中国')]"        #特色中国
    xpath_recharge = "//div[contains(text(),'充值缴费')]"       #充值缴费
    xpath_parking = "//div[contains(text(),'停车')]"          #停车按钮
    xpath_free_collar = "//div[contains(text(),'免费领')]"     #免费领按钮
    xpath_coupons = "//div[contains(text(),'领券中心')]"        #领券中心
    xpath_basket = "//div[contains(text(),'精选篮筐')]"         #篮筐按钮
    xpath_classification = "//div[contains(text(),'分类')]"    #分类按钮
    xpath_shopingcart = "//div[contains(text(),'购物车')]"     #购物车按钮
    xpath_my = "//div[contains(text(),'我')]"                 #我
    xpath_come_home = "//div[@class='project-show-left']"    #快到家
    xpath_flash_purchase = "//div[@class='project-show-bt']" #精品闪购
    xpath_globle = "//div[@class='project-show-right']/div[2]"#全球购
    '''----------天天抢购--------------'''
    xpath_snap_everyday = "//span[@id='gotoSnapUp']"          #天天抢购
    '''----------生活馆--------------'''
    xpath_fresh1 = "//section[1]/div/div[1]/a[1]"              #生鲜集市1
    xpath_fresh2 = "//section[1]/div/div[1]/a[2]"              #生鲜集市2
    xpath_nursing = "//section[1]/div/div[2]/a[1]"             #个性清护
    xpath_furniture_life  = "//section[1]/div/div[2]/a[2]"     #家具生活 
    xpath_cloakroom  = "//section[1]/div/div[2]/a[3]"          #家庭衣帽间
    '''----------精品馆--------------'''
    xpath_overseas1 = "//section[2]/div/div[1]/a[1]"           #海外直采1
    xpath_overseas2 = "//section[2]/div/div[1]/a[2]"           #海外直采2
    xpath_preferential = "//section[2]/div/div[1]/a[3]"        #特惠精选
    xpath_taste_global = "//section[2]/div/div[2]/a"           #尝边全球
    '''----------数码馆--------------'''
    xpath_mobile = "//section[3]/div/div/a[1]"                 #手机
    xpath_air_conditioner = "//section[3]/div/div/a[2]"        #空调
    xpath_fashion = "//section[3]/div/div/a[3]"                #潮玩
    
    @staticmethod
    def click_bailian_shopping(self):
        '''点击逛百联'''
        driver = self.driver
        common.commom.time_out(self)
        driver.find_element_by_xpath(First_page.xpath_bailian_shopping).click()
    
    @staticmethod    
    def click_first_medicine(self):
        '''点击第一医药'''
        driver = self.driver
        common.commom.time_out(self)
        driver.find_element_by_xpath(First_page.xpath_first_medicine).click()
     
    @staticmethod   
    def click_gift_card(self):
        '''点击礼品卡'''
        driver = self.driver
        common.commom.time_out(self)
        driver.find_element_by_xpath(First_page.xpath_furniture_life).click()
    
    @staticmethod    
    def click_digital(self):
        '''点击电器城'''
        driver = self.driver
        common.commom.time_out(self)
        driver.find_element_by_xpath(First_page.xpath_digital).click()
    
    @staticmethod    
    def click_chinese(self):
        '''点击特色中国'''
        driver = self.driver
        common.commom.time_out(self)
        driver.find_element_by_xpath(First_page.xpath_chinese).click()    
    
    @staticmethod
    def click_recharge(self):
        '''点击充值缴费'''
        driver = self.driver
        common.commom.time_out(self)
        driver.find_element_by_xpath(First_page.xpath_recharge).click()
    
    @staticmethod 
    def click_parking(self):
        '''点击停车场'''
        driver = self.driver
        common.commom.time_out(self)
        driver.find_element_by_xpath(First_page.xpath_parking).click()  
    
    @staticmethod
    def click_free_collar(self):
        '''点击免费领按钮'''
        driver = self.driver
        common.commom.time_out(self)
        driver.find_element_by_xpath(First_page.free_collar).click() 
     
    @staticmethod
    def click_my(self):
        '''点击我'''
        driver = self.driver
        common.commom.time_out(self)
        driver.find_element_by_xpath(First_page.xpath_my).click()   
        
    @staticmethod
    def click_coupons(self):
        '''点击领取中心'''
        driver = self.driver
        common.commom.time_out(self)
        driver.find_element_by_xpath(First_page.xpath_coupons).click()
        
    @staticmethod
    def click_basket(self):
        '''点击篮筐按钮'''
        driver = self.driver
        common.commom.time_out(self)
        driver.find_element_by_xpath(First_page.xpath_basket).click()
    
        
              
    
    
    