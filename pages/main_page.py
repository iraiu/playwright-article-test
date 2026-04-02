from pages.base_page import BasePage
from pages.search_results_page import SearchResultsPage


class MainPage(BasePage):

    def search(self, query: str):
        self.page.get_by_test_id("search-input").fill(query)
        self.page.get_by_test_id("search-button").click()
        self.page.wait_for_load_state("networkidle")
        return SearchResultsPage(self.page)
