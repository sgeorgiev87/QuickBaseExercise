import unittest

from Configuration.Drivers_setup import *
from WebDriverIO.common.page_objects import *

URL = 'https://webdriver.io'
SEARCH_KEYWORD = 'click'
EXPECTED_LIST_PROTOCOL_SECTION = ['WebDriver Protocol', 'Appium', 'Mobile JSON Wire Protocol', 'Chromium', 'Sauce Labs', 'Selenium Standalone', 'JSON Wire Protocol']

class SearchAPIDocumentation(unittest.TestCase):
    driver = None
    skip_test = False

    @classmethod
    def setUpClass(cls):
        cls.driver = driver_init()
        cls.driver.maximize_window()

    def test_01_open_homepage(self):
        try:
            HomePage(self.driver).open_homepage(URL)
        except:
            self.__class__.skip_test = True
            handle_exception(self.driver, screenshot_name='Homepage_fail.png', custom_exception='#### Homepage opening failed!!!')

    def test_02_open_and_search_api_page(self):
        if self.__class__.skip_test:
            raise Exception('### Test skipped')
        try:
            header = Header(self.driver)
            header.click_api_link()
            header.click_search_field()
            search_widget = SearchWidget(self.driver)
            search_widget.search_for_text(SEARCH_KEYWORD)
            search_widget.click_on_specific_search_result(SEARCH_KEYWORD)
            search_widget.assert_clicked_result_was_loaded(SEARCH_KEYWORD)
        except:
            handle_exception(self.driver, screenshot_name='Api_page_failed.png',
                             custom_exception='#### Api Page failed!!!')

    def test_03_verify_protocols_list(self):
        if self.__class__.skip_test:
            raise Exception('### Test skipped')
        try:
            api_documentation = APIDocumentation(self.driver)
            api_documentation.expand_protocols_section()
            api_documentation.verify_elements_in_section_list('Protocols', EXPECTED_LIST_PROTOCOL_SECTION)
        except:
            handle_exception(self.driver, screenshot_name='Verify_protocols_failed.png',
                             custom_exception='#### Verification of protocols section failed!!!')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()