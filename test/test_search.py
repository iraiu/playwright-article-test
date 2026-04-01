import pytest
from pages.main_page import MainPage


class TestSearch:

    @pytest.fixture
    def main_page(self, page):
        return MainPage(page)

    @pytest.mark.parametrize(
        "article_name,articles_count,filter_type,filter_display", [
            ("city", 10, "price_asc", "Price: low to high"),
            ("city", 15, "price_desc", "Price: high to low"),
            ("habits", 10, "price_asc", "Price: low to high"),
            ("habits", 15, "price_desc", "Price: high to low"),
        ])
    def test_search_and_price_sorting(self, main_page, article_name,
                                      articles_count, filter_type,
                                      filter_display):
        main_page.navigate("/")
        search_results = main_page.search(article_name)
        search_results.wait_for_results_loaded()
        search_results.apply_filter(filter_type)

        prices = search_results.get_all_prices(articles_count)

        is_sorted = search_results.are_prices_sorted_correctly(filter_type,
                                                               prices)
        assert is_sorted, f"Prices not sorted correctly for filter '{filter_display}': {prices}"
        assert len(prices) > 0, f"No prices found for '{article_name}'"