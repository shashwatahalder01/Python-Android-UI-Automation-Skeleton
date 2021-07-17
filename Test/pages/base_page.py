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
import textwrap


class BasePage(object):

    def __init__(self, driver, base_url="about:blank"):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, locator):
        element = self.driver.find_element_by_xpath(locator)
        # element = self.driver.find_element_by_accessibility_id('SomeAccessibilityID')
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

    # Status___________________________________________________________________

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

    # Execute Mobile Command___________________________________________________________________

    # Execute a native mobile command     # TODO: need to edit
    def execute_native_mobile_command(self):
        self.driver.execute_script("mobile: scroll", {'direction': 'down'})
        self.driver.execute_script('document.title')

    # Session___________________________________________________________________

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

    # Take Screenshot of the current viewport/window/page
    def take_screenshot(self):
        screenshotBase64 = self.driver.get_screenshot_as_base64()
        return screenshotBase64

    # Get current application hierarchy XML (app) or page source (web)
    def get_page_source(self):
        source = self.driver.page_source
        return source

    # Waits_________________________

    # Configure the amount of time that a particular type of operation can execute for before they are aborted
    def page_load_timeout(self, seconds):
        self.driver.set_page_load_timeout(seconds)

    # Set the amount of time, in milliseconds, that asynchronous scripts executed by execute async are permitted to run before they are aborted (Web context only)
    def script_timeout(self, seconds):
        self.driver.set_script_timeout(seconds)

    # Set the amount of time the driver should wait when searching for elements
    def implicit_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    # Orientation_________________________

    # Get Orientation
    def get_orientation(self):
        orientation = self.driver.orientation
        return orientation

    # Set Orientation
    def set_orientation_landscape(self):
        self.driver.orientation = "LANDSCAPE"

    def set_orientation_portrait(self):
        self.driver.orientation = "PORTRAIT"

    # Geolocation_________________________

    # Get current geo location
    def get_geolocation(self):
        location = self.driver.location()
        return location

    # Set current geo location
    def set_geolocation(self, latitude, longitude, altitude):
        self.driver.set_location(latitude, longitude, altitude)

    # Logs_________________________
    # Get log types
    def get_available_log_types(self):
        log_types = self.driver.log_types
        return log_types

    # Get the log for a given log type. Log buffer is reset after each request
    def get_logs(self, logType):
        logs = self.driver.get_log(logType)
        # logs = self.driver.get_log('driver')
        # logs = self.driver.get_log('logcat')
        return logs

    # Events_________________________

    # Store a custom event
    def log_a_event(self, event):
        self.driver.log_event('appium', 'funEvent')

    # Get events stored in appium server
    def get_events(self):
        events = self.driver.get_events()
        return events

    def get_multiple_events(self, eventList):
        events = self.driver.get_events(eventList)
        # self.driver.get_events(['event1', 'event2'])
        return events

    # Settings_________________________

    # Update the current setting on the device
    def update_device_settings(self):
        self.driver.update_settings({"sample": "value"})

    # Retrieve the current settings on the device
    def retrieve_device_settings(self):
        settings = self.driver.get_settings
        return settings

    # Execute Script_________________________
    # Run a WebdriverIO script against the current session, allowing execution of many commands in one Appium request.
    def execute_driver_script(self, script):
        # script = """
        #     const el = await driver.$('~foo');
        #     await el.click();
        # """
        self.driver.execute_driver(script=textwrap.dedent(script))

    # Device___________________________________________________________________

    # Activity_________________________

    # Start an Android activity by providing package name and activity name
    def start_activity(self, packageName, activityName):
        self.driver.start_activity(packageName, activityName)

    # Get the name of the current Android activity
    def get_current_activity(self):
        activity = self.driver.current_activity
        return activity

    # Get the name of the current Android package
    def get_current_package(self):
        package = self.driver.current_package
        return package

    # App_________________________

    # Install the given app onto the device
    def install_app(self, apkPath):
        self.driver.install_app(apkPath)

    # Check whether the specified app is installed on the device
    def is_app_installed(self, packageName):
        val = self.driver.is_app_installed(packageName)
        # val = self.driver.is_app_installed('com.example.AppName')
        return val

    # Launch the app-under-test on the device
    def launch_app(self):
        self.driver.launch_app()

    # Send the currently running app for this session to the background
    # {"seconds": secs},[-1 to deactivate app entirely] null
    def background_app(self, secondsObject):
        self.driver.background_app()

    # Close an app on device
    def close_app(self):
        self.driver.close_app()

    # Reset the currently running app for this session
    def reset_app(self):
        self.driver.reset()

    # Remove an app from the device
    def remove_app(self, packageName):
        self.driver.remove_app(packageName)
        # self.driver.remove_app('com.example.AppName')

    # Activate the given app onto the device
    def activate_app(self):
        self.driver.activate_app('com.apple.Preferences')
        self.driver.activate_app('io.appium.android.apis')

    # Terminate the given app on the device
    def terminate_app(self):
        self.driver.terminate_app('com.apple.Preferences')

    # Get the given app status on the device
    def get_app_state(self):
        self.driver.query_app_state('com.apple.Preferences')

    # Get app strings
    def get_app_strings(self):
        appStrings = self.driver.app_strings("en", "/path/to/file")
        return appStrings

    # Get test coverage data
    def end_test_coverage(self):
        self.driver.end_test_coverage("Intent", "/path")

    # Clipboard_________________________

    # Get the content of the system clipboard
    def get_clipboard(self):
        self.driver.get_clipboard()
        text = self.driver.get_clipboard_text()
        return text

    # Set the content of the system clipboard
    def set_clipboard(self, text):
        self.driver.set_clipboard('happy testing')
        self.driver.set_clipboard_text('happy testing')

    # Emulator_________________________

    # Emulate power state change on the connected emulator.
    def emulate_power_state(self):
        # TODO: edit parameter option
        self.driver.set_power_ac('Power.AC_OFF')
        self.driver.set_power_ac('Power.AC_ON')

    # Emulate power capacity change on the connected emulator.
    def emulate_power_capacity(self, powerPercentage):
        self.driver.set_power_capacity(powerPercentage)

    # Files_________________________
    # Interactions_________________________
    # Keys_________________________
    # NetWork_________________________
    # performance Data_________________________
    # screen Recording_________________________
    # Simulator_________________________
    # System_________________________
    # Authentication_________________________

    # Element___________________________________________________________________

    # Find Element_________________________
    # Find Elements_________________________
    # Actions_________________________
    # Attributes_________________________
    # Other_________________________

    # Context___________________________________________________________________

    # Get Context_________________________
    # Get All Context_________________________
    # Set Context_________________________

    # Interactions___________________________________________________________________

    # Mouse_________________________
    # Touch_________________________
    # W3c Actions_________________________

    # Web___________________________________________________________________

    # Window_________________________
    # Navigation_________________________
    # Storage_________________________
    # Frame_________________________
    # Execute Async_________________________
    # Execute_________________________

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
