from selenium.webdriver.common.by import By


class HomePageSelectors(object):
    MainContainer = (By.CSS_SELECTOR, '.hero--primary')


class HeaderSelectors(object):
    IOLogo = (By.CSS_SELECTOR, '.navbar__items .navbar__brand img')
    APILink = (By.LINK_TEXT, 'API')
    SearchField = (By.CLASS_NAME, 'DocSearch-Button-Placeholder')


class SearchWidgetSelectors(object):
    SearchInputField = (By.ID, 'docsearch-input')
    SearchResults = (By.CSS_SELECTOR, '.DocSearch-Hit-title')
    NoResultsSearchTitle = (By.CSS_SELECTOR, '.DocSearch-NoResults .DocSearch-Title')
    RecentSearches = (By.CSS_SELECTOR, '#docsearch-list .DocSearch-Hit-title')

    @staticmethod
    def remove_button_specific_recent_result(recent_result):
        return (By.XPATH, '//span[text()="' + recent_result + '"]/ancestor::div[@class="DocSearch-Hit-Container"]//button[@title="Remove this search from history"]')

    @staticmethod
    def favourite_button_specific_recent_result(recent_result):
        return (By.XPATH,
                '//span[text()="' + recent_result + '"]/ancestor::div[@class="DocSearch-Hit-Container"]//button[@title="Save this search"]')

    @staticmethod
    def result_in_favourites(result):
        return (By.XPATH, '//div[text()="Favorites"]/ancestor::section//span[text()="' + result + '"]')

class GeneralSelectors(object):
    TitleHeader = (By.CLASS_NAME, 'docTitle_Oumm')


class APIDocumentationSelectors(object):
    ProtocolsSection = (By.LINK_TEXT, 'Protocols')

    @staticmethod
    def all_elements_in_given_section(section):
        return (By.XPATH, '//a[text()="' + section + '"]/ancestor::li//li/a')

