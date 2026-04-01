from pages.base_page import BasePage
from playwright.sync_api import Page


class MainPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def search_input(self):
        return self.page.get_by_test_id("search-input")

    @property
    def search_button(self):
        return self.page.get_by_test_id("search-button")

    def search(self, query: str):
        self.search_input.fill(query)
        self.search_button.click()
        self.page.wait_for_load_state("networkidle")

        from pages.search_results_page import SearchResultsPage
        return SearchResultsPage(self.page)