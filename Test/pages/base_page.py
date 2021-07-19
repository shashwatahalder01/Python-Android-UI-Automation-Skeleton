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
        # self.driver.set_power_capacity(50)

    # Files_________________________

    # Place a file onto the device in a particular place
    def push_file(self, filePath):
        dest_path = '/data/local/tmp/test_push_file.txt'
        data = bytes('This is the contents of the file to push to the device.', 'utf-8')
        self.driver.push_file(dest_path, base64.b64encode(data).decode('utf-8'))

    # Retrieve a file from the device's file system
    def pull_file(self, filePath):
        file_base64 = self.driver.pull_file('/path/to/device/foo.bar')

    # Retrieve a folder from the device's file system
    def pull_folder(self, folderPath):
        folder_base64 = self.driver.pull_folder('/path/to/device/foo.bar')

    # Interactions_________________________

    # Perform a shake action on the device
    def shake_device(self):
        self.driver.shake()

    # Lock the device
    def lock_device(self):
        self.driver.lock()

    # Unlock the device
    def unlock_device(self):
        self.driver.unlock()

    # Check whether the device is locked or not
    def is_device_locked(self):
        val = self.driver.is_locked()
        return val

    # Rotate the device in three dimensions
    # Not supported # use js method

    # Keys_________________________

    # Press a particular key on an Android Device
    def press_key(self, key):
        self.driver.press_keycode(10)

    # Press and hold a particular key code on an Android device
    def long_press_key(self):
        self.driver.long_press_keycode(10)
        self.driver.long_press_keycode(AndroidKeyCode.HOME)

    # Hide soft keyboard
    def hide_keyboard(self):
        self.driver.hide_keyboard()

    # Whether or not the soft keyboard is shown
    def is_keyboard_shown(self):
        self.driver.is_keyboard_shown()

    # NetWork_________________________

    # Toggle airplane mode on device
    def toggle_airplane(self):
        self.driver.toggleAirplaneMode()

    # Switch the state of data service
    def toggle_data(self):
        pass
        # Not supported

    # Switch the state of the WiFi service
    def toggle_wifi(self):
        self.driver.toggleWifi()

    #  Switch the state of the location service
    def toggle_location_services(self):
        self.driver.toggle_location_services()

    # Simulate an SMS message (Emulator only)
    def send_sms(self):
        self.driver.send_sms('555-123-4567', 'Hey lol')

    # Make GSM call (Emulator only)
    def make_call(self):
        self.driver.make_gsm_call('5551234567', GsmCallActions.CALL)

    # Set GSM signal strength (Emulator only)
    def set_signal(self):
        self.driver.set_gsm_signal(GsmSignalStrength.GOOD)

    # Set GSM voice state (Emulator only)
    def set_voice_state(self):
        self.driver.set_gsm_voice(GsmVoiceState.HOME)

    # Set network speed (Emulator only)
    def set_network_speed(self):
        self.driver.set_network_speed(NetSpeed.LTE)

    # performance Data_________________________

    # Returns the information of the system state which is supported to read as like cpu, memory, network traffic, and battery
    def get_performance_data(self):
        self.driver.get_performance_data('my.app.package', 'cpuinfo', 5)

    # Returns the information types of the system state which is supported to read as like cpu, memory, network traffic, and battery
    def get_performance_data_types(self):
        self.driver.get_performance_data_types()
        
    # screen Recording_________________________

    # Start recording screen
    def start_record_screen(self):
        self.driver.start_recording_screen()

    # Stop recording screen
    def stop_record_screen(self):
        self.driver.stop_recording_screen()

    # Simulator_________________________

    # Simulate a touch id event (iOS Simulator only)
    def perform_touch_id(self):
        self.driver.touch_id(False)  # Simulates a failed touch
        self.driver.touch_id(True)  # Simulates a passing touch

    # Toggle the simulator being enrolled to accept touchId (iOS Simulator only)
    def toggle_touch_id_enrollment(self):
        self.driver.toggle_touch_id_enrollment()

    # System_________________________

    # Open Android notifications (Emulator only)
    def open_notifications(self):
        self.driver.open_notifications()

    # Retrieve visibility and bounds information of the status and navigation bars
    def get_system_bars(self):
        sysInfo = self.driver.get_system_bars()
        return sysInfo

    # Get the time on the device
    def get_system_time(self):
        time = self.driver.device_time
        # time = self.driver.get_device_time()
        # time = self.driver.get_device_time("YYYY-MM-DD")
        return time

    # Retrieve display density(dpi) of the Android device
    def get_display_density(self):
        dpi = self.driver.get_display_density()
        return dpi

    # Authentication_________________________

    # Authenticate users by using their finger print scans on supported emulators.
    def authenticate_user_by_fingerprint(self):
        self.driver.finger_print(1)

    # Element___________________________________________________________________

    # Find Element_________________________

    # Search for an element on the page
    def find_element(self, locator):
        element = self.driver.find_element_by_accessibility_id(locator)
        element = self.driver.find_element_by_xpath(locator)
        return element

    # Find Elements_________________________

    # Search for multiple elements
    def find_elements(self, locator):
        elements = self.driver.find_elements_by_accessibility_id(locator)
        elements = self.driver.find_elements_by_xpath(locator)
        return elements

    # Actions_________________________

    # Click element at its center point.
    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    # Send a sequence of key strokes to an element
    def send_keys(self, data, locator):
        element = self.find_element(locator)
        element.send_keys(data)

    # Clear an element's value
    def clear(self, locator):
        element = self.find_element(locator)
        element.clear()

    # Attributes_________________________

    # Returns visible text for element
    def get_element_text(self, locator):
        element = self.find_element(locator)
        text = element.text
        return text

    # Get an element's tag name
    def get_tag_name(self, locator):
        element = self.find_element(locator)
        tagName = element.tag_name
        return tagName

    # Get an element's tag name
    def get_element_attribute(self, attribute, locator):
        element = self.find_element(locator)
        attribute = element.get_attribute(attribute)
        return attribute

    # Determine if a form or form-like element (checkbox, select, etc...) is selected
    def is_element_selected(self, locator):
        element = self.find_element(locator)
        val = element.is_selected()
        return val

    # Determine if an element is currently enabled
    def is_element_enabled(self, locator):
        element = self.find_element(locator)
        val = element.is_enabled()
        return val

    # Determine if an element is currently displayed
    def is_element_displayed(self, locator):
        element = self.find_element(locator)
        val = element.is_displayed()
        return val

    # Determine an element's location on the page or screen
    def get_element_location(self, locator):
        element = self.find_element(locator)
        location = element.location
        return location

    # Determine an element's size in pixels
    def get_element_size(self, locator):
        element = self.find_element(locator)
        size = element.size
        return size

    # Gets dimensions and coordinates of an element
    def get_element_rect(self, locator):
        element = self.find_element(locator)
        val = element.rect
        return val

    # Query the value of a web element's computed CSS property
    def get_element_css_value(self, cssProperty, locator):
        element = self.find_element(locator)
        cssProperty = element.value_of_css_property(cssProperty)
        return cssProperty

    # Determine an element's location on the screen once it has been scrolled into view (mainly an internal command and not supported by all clients)
    def get_element_location_in_view(self, locator):
        element = self.find_element(locator)
        location = element.location_in_view
        return location

    # Other_________________________

    # Submit a FORM element
    def submit_form(self, locator):
        element = self.find_element(locator)
        element.submit()

    # Gets the active element of the current session
    def get_active_element(self, locator):
        element = self.driver.switch_to.active_element
        return element

    # Test if two element IDs refer to the same element
    def are_elements_equal(self, locator1, locator2):
        element1 = self.find_element(locator1)
        element2 = self.find_element(locator2)
        val = ''
        if element1 == element2:
            val = True
        else:
            val = False
        return val

    # Context___________________________________________________________________

    # Get Context_________________________

    # Get the current context in which Appium is running
    def get_current_context(self):
        context = self.driver.current_context
        context = self.driver.context
        return context

    # Get All Context_________________________

    # Get all the contexts available to automate
    def get_all_contexts(self):
        contexts = self.driver.contexts
        return contexts

    # Set Context_________________________

    # Set the context being automated
    def set_current_context(self):
        webview = self.driver.contexts[1]
        self.driver.switch_to.context(webview)
        self.driver.switch_to.context('NATIVE_APP')

    # Interactions___________________________________________________________________

    # Mouse_________________________

    # Move the mouse by an offset of the specificed elemen
    def move_mouse_to(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to(element, 10, 10)
        actions.perform()

    # Click any mouse button at the current mouse coordinates
    def click_by_actionChains(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.perform()

    # Double-clicks at the current mouse coordinates (set by moveto).
    def double_click_by_actionChains(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.double_click()
        actions.perform()

    # Click and hold the left mouse button at the current mouse coordinates
    def button_down(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click_and_hold()
        actions.perform()

    # Releases the mouse button previously held
    def button_up(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click_and_hold()
        actions.perform()

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
