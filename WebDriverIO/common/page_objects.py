from WebDriverIO.common.page_objects_selectors import *
from Configuration.BasePage import *
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    def __init__(self, driver, timeout=10):
        BasePage.__init__(self, driver=driver, timeout=timeout)

    def open_homepage(self, url):
        self.driver.get(url)
        self.visibility_of_element(HomePageSelectors.MainContainer)
        print ('--> Homepage was successfully loaded!')


class Header(BasePage):
    def __init__(self, driver, timeout=10):
        BasePage.__init__(self, driver=driver, timeout=timeout)

    def click_api_link(self):
        self.click_on_element('API Link', HeaderSelectors.APILink)

    def click_search_field(self):
        self.click_on_element('Search Field', HeaderSelectors.SearchField)

    def click_on_io_logo(self):
        self.click_on_element('WebDriver IO logo', HeaderSelectors.IOLogo)


class SearchWidget(BasePage):
    def __init__(self, driver, timeout=10):
        BasePage.__init__(self, driver=driver, timeout=timeout)
        try:
            self.visibility_of_element(SearchWidgetSelectors.SearchInputField)
            print ('--> Search Popup was successfully loaded!')
        except:
            raise Exception('#### Search popup was not loaded' + traceback.format_exc())

    def search_for_text(self, text):
        self.clickable_element(SearchWidgetSelectors.SearchInputField).send_keys(text)

    def click_on_specific_search_result(self, exp_search_result):
        time.sleep(0.2)
        iteration = 1
        all_search_results = self.visibility_of_elements(SearchWidgetSelectors.SearchResults)
        for act_search_result in all_search_results:
            if exp_search_result == act_search_result.text:
                act_search_result.click()
                print('--> Clicked on search result: ' + exp_search_result)
                break
            else:
                iteration += 1
            if iteration > len(all_search_results):
                raise Exception('#### Could not find given search result: ' + exp_search_result + '\n' + traceback.format_exc())

    def assert_clicked_result_was_loaded(self, exp_result):
        assert self.visibility_of_element(GeneralSelectors.TitleHeader).text == exp_result, '#### Clicked result was not loaded'
        print('--> Clicked result ' + exp_result + ' was successfully loaded!')

    def assert_no_results_for_invalid_keyword(self, keyword):
        exp_result = 'No results for "' + keyword + '"'
        assert self.visibility_of_element(SearchWidgetSelectors.NoResultsSearchTitle).text == exp_result, '#### Wrong result for invalid keyword'
        print('--> Valid error message for not found results is shown!')

    def verify_recent_history_results_are_saved(self, exp_recent_results):
        all_recent_results = self.visibility_of_elements(SearchWidgetSelectors.RecentSearches)
        all_recent_results_text = []

        for recent_result in all_recent_results:
            all_recent_results_text.append(recent_result.text)

        error_count = 0
        for exp_result in exp_recent_results:
            if exp_result not in all_recent_results_text:
                print ('#### Expected search result ' + exp_result + ' is not in Recent list')
                error_count += 1

        if error_count != 0:
            raise Exception('#### There is difference between expected and actual Recent results. Check the logs!')
        else:
            print('--> All expected search results are in the Recent list')

    def save_recent_result_in_favourite(self, result_to_save):
        self.click_on_element('Favourite button for result ' + result_to_save, SearchWidgetSelectors.favourite_button_specific_recent_result(result_to_save))

    def verify_result_saved_in_favourite(self, saved_result):
        try:
            self.visibility_of_element(SearchWidgetSelectors.result_in_favourites(saved_result))
            print('--> Result ' + saved_result + ' successfully saved in Favorites')
        except:
            raise Exception('#### Result ' + saved_result + ' not saved in Favourites! \n' + traceback.format_exc())


    def delete_specific_recent_result(self, result_to_delete):
        self.click_on_element('Delete button for result ' + result_to_delete, SearchWidgetSelectors.remove_button_specific_recent_result(result_to_delete))

    def verify_deleted_result_not_in_recent_history(self, deleted_result):
        counter = 0
        while counter < 10:
            if self.is_element_displayed(SearchWidgetSelectors.remove_button_specific_recent_result(deleted_result)):
                counter +=1
                time.sleep(0.5)
            else:
                print('--> Element ' + deleted_result + ' successfully deleted from Recent history')
                break
        if counter == 10:
            raise Exception('#### Element not deleted from Recent history for 5 seconds!')

    def close_search_widget(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        print('--> Escape key pressed with Search widget on screen!')


class APIDocumentation(BasePage):
    def __init__(self, driver, timeout=10):
        BasePage.__init__(self, driver=driver, timeout=timeout)

    def expand_protocols_section(self):
        self.click_on_element('Protocols section', APIDocumentationSelectors.ProtocolsSection)

    def verify_elements_in_section_list(self, section, exp_list):
        error_count = 0
        act_list_elements = self.visibility_of_elements(APIDocumentationSelectors.all_elements_in_given_section(section))
        act_list_strings = []

        for element in act_list_elements:
            act_list_strings.append(element.text)  # getting the strings for all web elements in the opened section

        for exp_list_element in exp_list:
            if exp_list_element in act_list_strings:
                act_list_strings.remove(exp_list_element)  # removing checked element from actual list
            else:
                print('#### Expected element: ' + exp_list_element + ' is not in the ' + section + ' section!!!')
                error_count += 1

        if len(act_list_strings) != 0:  # checking if any new elements were added into Protocols section on website
            print('#### There are elements in Actual ' + section + ' section list that are not in the expected one: ' + str(
                act_list_strings))
            error_count += 1

        if error_count == 0:
            print('--> All expected elements in ' + section + ' section match with actual elements!')
        else:
            raise Exception('#### There are differences between expected and actual lists in ' + section + ' section. Please check the log!!!')
