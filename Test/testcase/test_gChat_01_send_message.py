from pages.intro_page import IntroPage
from testcase.base_test import BaseTest


class TestIntroPage(BaseTest):

    def test_intro(self):
        introPage = IntroPage(self.driver)
        introPage.test_gChat_01_send_message()

# python3 -m unittest testcase.test_01_intro_to_home
