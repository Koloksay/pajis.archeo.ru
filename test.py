import pytest
import data
import method

selector = 'div.issue-page__details > section'

@pytest.mark.parametrize("pair", data.data)
def test_compare_data(pair):
    old_url, new_url = pair.values()

    old_data = method.extract_data_from_page(old_url, selector)
    new_data = method.extract_data_from_page(new_url, selector)
    assert method.compare_data(old_data, new_data), f"Данные не равны {old_url} и {new_url}"
