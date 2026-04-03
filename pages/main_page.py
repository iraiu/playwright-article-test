from pages.base_page import BasePage
from playwright.sync_api import Page
from pages.search_results_page import SearchResultsPage


class MainPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = page.get_by_test_id("search-input")
        self.search_button = page.get_by_test_id("search-button")

    def search(self, query: str):
        self.search_input.fill(query)
        self.search_button.click()
        return SearchResultsPage(self.page)
