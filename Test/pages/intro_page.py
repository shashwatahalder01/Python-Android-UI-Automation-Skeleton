from pages.base_page import BasePage
from data.locators import StartupPageLocator
from data.data import *
from utils.readUserData import email, message, seenOldBound
from utils.excelUtils import *
# from testconf.uitlsfunction import *
# from time import sleep
import allure
import re


class IntroPage(BasePage):

    def __init__(self, driver):
        self.locator = StartupPageLocator
        self.data = Data
        super().__init__(driver)

    @allure.step('test_send_message')
    def test_gChat_01_send_message(self):
        self.click(self.locator.ok)
        self.click(self.locator.changeProfile)
        self.click(self.locator.shQups)
        self.click(self.locator.ok)
        self.click(self.locator.searchbutton)
        print(email, message)
        seenBound = []
        # for i in range(len(email)):
        for i in range(1):
            self.send_data(email[i], self.locator.searchText)
            self.click(self.locator.selectPerson)
            val = self.get_attribute_value(self.data.boundsAttribute, self.locator.seenMessage)
            val = re.findall(r'[-\d]+', val)
            seenBound.append(val)
            self.send_data(message[i], self.locator.chatMessage)
            self.click(self.locator.postMessage)
            self.go_back()
            self.click(self.locator.newChat)

        writesinglecol(userData, emailUserNamesheetName, len(seenBound), 4, 1, seenBound)



    @allure.step('test_seen_message')
    def test_gChat_02_seen_message(self):
        self.click(self.locator.ok)
        self.click(self.locator.changeProfile)
        self.click(self.locator.shQups)
        self.click(self.locator.ok)
        self.click(self.locator.searchbutton)
        seenNewBound = []
        for i in range(len(email)):
            self.send_data(email[i], self.locator.searchText)
            self.click(self.locator.selectPerson)
            val = self.is_element_displayed(self.locator.seenMessage)
            print(val)
            val = self.get_attribute_value(self.data.boundsAttribute, self.locator.seenMessage)
            print(val)
            print(type(val))
            seenNewBound.append(val)

        result = []
        for i in range(len(seenOldBound)):
            if seenOldBound[i] < seenNewBound[i]:
                result.append('Seen')
            else:
                result.append('Not seen')
