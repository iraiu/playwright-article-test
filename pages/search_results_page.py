import re
from pages.base_page import BasePage
from playwright.sync_api import Page
from typing import List


class SearchResultsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def filter_sort(self):
        return self.page.get_by_test_id("filter-sort")

    @property
    def results_loader(self):
        return self.page.get_by_test_id("results-loader-track")

    def get_price_by_index(self, index: int = 1) -> float:
        price_element = self.page.get_by_test_id(
            f"search-result-price-{index}")
        price_text = price_element.text_content() or ""

        match = re.search(r'(\d+[.,]?\d*)',
                          price_text.replace(' ', '').replace(',', '.'))
        if match:
            return float(match.group(1))
        return 0.0

    def get_all_prices(self, count: int = 10) -> List[float]:
        prices = []
        for i in range(1, count + 1):
            try:
                price = self.get_price_by_index(i)
                if price > 0:
                    prices.append(price)
            except:
                break
        return prices

    def apply_filter(self, filter_type: str):
        self.filter_sort.select_option(filter_type)
        self.wait_for_results_loaded()
        return self

    def wait_for_results_loaded(self):
        self.results_loader.wait_for(state="attached", timeout=5000)
        self.results_loader.wait_for(state="hidden", timeout=30000)
        return self

    def are_prices_sorted_correctly(self, filter_type: str,
                                    prices: List[float]) -> bool:
        if len(prices) < 2:
            return True

        if filter_type == "price_asc":
            return all(
                prices[i] <= prices[i + 1] for i in range(len(prices) - 1))
        elif filter_type == "price_desc":
            return all(
                prices[i] >= prices[i + 1] for i in range(len(prices) - 1))

        return True