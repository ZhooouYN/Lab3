import price_info as price

def test_total_cost_shipping():
    result = price.total_cost_shopping()
    assert (result == 46.75)

def test_cost_of_fruits():
    result = price.cost_of_fruits('apple', 10)
    assert (result == 12.0)