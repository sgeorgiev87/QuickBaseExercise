import unittest

from Configuration.Drivers_setup import *
from WebDriverIO.common.page_objects import *

URL = 'https://webdriver.io'
VALID_TEXT_RESULT1 = 'click'
VALID_TEXT_RESULT2 = 'Timeouts'
INVALID_TEXT_RESULT = 'euiwqydhak'
VALID_RESULTS_RECENT_HISTORY = [VALID_TEXT_RESULT1, VALID_TEXT_RESULT2]


class TestSearchWidget(unittest.TestCase):
    driver = None
    skip_test = False
    header = None
    search_widget = None

    @classmethod
    def setUpClass(cls):
        cls.driver = driver_init()
        cls.driver.maximize_window()

    def test_01_search_valid_result(self):
        try:
            print('\n ---- Starting test 1 - Search for valid search result ----')
            HomePage(self.driver).open_homepage(URL)
            self.__class__.header = Header(self.driver)
            self.__class__.header.click_search_field()
            self.__class__.search_widget = SearchWidget(self.driver)
            self.__class__.search_widget.search_for_text(VALID_TEXT_RESULT1)
            self.__class__.search_widget.click_on_specific_search_result(VALID_TEXT_RESULT1)
            self.__class__.search_widget.assert_clicked_result_was_loaded(VALID_TEXT_RESULT1)
        except:
            handle_exception(self.driver, screenshot_name='Search_valid_result_failed.png',
                             custom_exception='#### Search for valid result failed!!!')

    def test_02_search_invalid_result(self):
        try:
            print('\n ---- Starting test 2 - Search for invalid search result ----')
            HomePage(self.driver).open_homepage(URL)
            self.__class__.header.click_search_field()
            self.__class__.search_widget.search_for_text(INVALID_TEXT_RESULT)
            self.__class__.search_widget.assert_no_results_for_invalid_keyword(INVALID_TEXT_RESULT)
        except:
            handle_exception(self.driver, screenshot_name='Search_invalid_result_failed.png',
                             custom_exception='#### Search for invalid result failed!!!')

    def test_03_history_for_valid_results_is_kept(self):
        try:
            print('\n ---- Starting test 3 - History is kept for valid search results ----')
            HomePage(self.driver).open_homepage(URL)  # we will search for 1 more valid results, to have 1 more line in search history
            self.__class__.header.click_search_field()
            self.__class__.search_widget.search_for_text(VALID_TEXT_RESULT2)
            self.__class__.search_widget.click_on_specific_search_result(VALID_TEXT_RESULT2)
            self.__class__.search_widget.assert_clicked_result_was_loaded(VALID_TEXT_RESULT2)
            self.__class__.header.click_search_field()
            self.__class__.search_widget.verify_recent_history_results_are_saved(VALID_RESULTS_RECENT_HISTORY)
        except:
            handle_exception(self.driver, screenshot_name='Recent_history_failed.png',
                             custom_exception='#### Recent history for search results failed!!!')

    def test_04_save_search_result_as_favourite(self):
        try:
            print('\n ---- Starting test 4 - Saving recent result in favourite----')
            HomePage(self.driver).open_homepage(URL)
            self.__class__.header.click_search_field()
            self.__class__.search_widget.save_recent_result_in_favourite(VALID_TEXT_RESULT1)
            self.__class__.search_widget.verify_result_saved_in_favourite(VALID_TEXT_RESULT1)
        except:
            handle_exception(self.driver, screenshot_name='Saving_recent_result_in_favorites_failed.png',
                             custom_exception='#### Saving recent result in favorites failed!!!')

    def test_05_delete_recent_result(self):
        try:
            print('\n ---- Starting test 5 - Deleting recent result ----')
            HomePage(self.driver).open_homepage(URL)
            self.__class__.header.click_search_field()
            self.__class__.search_widget.delete_specific_recent_result(VALID_TEXT_RESULT2)
            self.__class__.search_widget.verify_deleted_result_not_in_recent_history(VALID_TEXT_RESULT2)
        except:
            handle_exception(self.driver, screenshot_name='Deleting_recent_result_failed.png',
                             custom_exception='#### Deleting recent result failed!!!')

    def test_06_close_search_widget(self):
        try:
            print('\n ---- Starting test 6 - Closing search widget ----')
            HomePage(self.driver).open_homepage(URL)
            self.__class__.header.click_search_field()
            self.__class__.search_widget.close_search_widget()
            self.__class__.header.click_on_io_logo()
            print('--> Search Widget was successfully closed with Escape key')
        except:
            handle_exception(self.driver, screenshot_name='Closing_search_widget_failed.png',
                             custom_exception='#### Closing Search Widget failed!!!')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


""" 
we can also write the following tests:
- going through the search results with the arrow keys and checking if the next area is selected - aria-selected tag changes from false to true
- clicking on X button in the search valid and validating the input field is empty, and the button is gone
- select a result with the Enter key instead of clicking on it
- checking the result we want is shown in the relevant section (Guides/Protocols/etc.)
- clicking on See all results and verifying we are redirected to the correct page
- closing the search widget by clicking outside of it (locating an element, moving by ActionChains offset with given pixels, and clicking)
"""

