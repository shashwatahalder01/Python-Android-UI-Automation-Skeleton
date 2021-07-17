# from telnetlib import EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
# from time import sleep

from selenium.webdriver.common.utils import is_connectable, is_url_connectable
from pathlib import Path
from appium import webdriver


class BasePage(object):

    def __init__(self, driver, base_url="about:blank"):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, locator):
        element = self.driver.find_element_by_xpath(locator)
        return element

    def click(self, locator):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(locator).click()

    def send_data(self, data, locator):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(locator).send_keys(data)

    def is_element_displayed(self, locator):
        val = self.driver.find_element_by_xpath(locator).is_displayed()
        return val

    def get_attribute_value(self, attributeName, locator):
        val = self.driver.find_element_by_xpath(locator).get_attribute(attributeName)
        return val

    def scroll(self):
        pass

    # get is port connectable
    @staticmethod
    def get_server_connctable(port, host='localhost'):
        val = is_connectable(port, host)
        return val

    # get server's current status
    @staticmethod
    def get_server_status(port):
        val = is_url_connectable(port)
        return val

    # TODO: need to edit
    # Execute Mobile Command
    def execute_native_mobile_command(self):
        self.driver.execute_script("mobile: scroll", {'direction': 'down'})
        self.driver.execute_script('document.title')


        # Session _______________________________________________

    def create_session(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'Android Emulator',
            'automationName': 'UiAutomator2',
            'app': Path('/path/to/app')
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return self.driver

    # End running session
    def end_session(self):
        self.driver.quit()

    # Get Session Capabilities
    def get_session_capabilities(self):
        desired_caps = self.driver.session
        return desired_caps

    # Navigate backwards in the browser history
    def go_back(self):
        self.driver.back()

    # Take Screenshot
    def take_screenshot(self):
        screenshotBase64 = self.driver.get_screenshot_as_base64()
        return screenshotBase64

    # Get Page Source
    def page_source(self):
        source = self.driver.page_source
        return source

    # Waits _________________________

    # Set Timeouts
    # Configure the amount of time that a particular type of operation can execute for before they are aborted
    def set_timeout(self, seconds):
        self.driver.set_page_load_timeout(seconds)
        self.driver.set_script_timeout(seconds)
        self.driver.set_implicit_timeout(seconds)

        # def find_element(self, *locator):
        #     return self.driver.find_element(*locator)

        # def find_elements(self, *locator):
        #     return self.driver.find_elements(*locator)
        #
        # def open(self, url):
        #     url = self.base_url + url
        #     self.driver.get(url)
        #
        # def get_title(self):
        #     return self.driver.title
        #
        # def get_url(self):
        #     return self.driver.current_url
        #
        # def refresh(self):
        #     return self.driver.refresh()

        #
        # def hover(self, *locator):
        #     element = self.find_element(*locator)
        #     hover = ActionChains(self.driver).move_to_element(element)
        #     hover.perform()
        #
        # def wait_element(self, *locator):
        #     try:
        #         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        #     except TimeoutException:
        #         print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
        #         self.driver.quit()
        #
        # def wait_element1(self, *locator):
        #     try:
        #         ignored_exceptions = (NoSuchElementException, StaleElementReferenceException )
        #         WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located(locator))
        #     except TimeoutException:
        #         print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
        #         self.driver.quit()
