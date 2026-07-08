from food_order import calculate_total

def test_order1():
    assert calculate_total(10, 2) == 20

def test_order2():
    # test if total food order is equal to 30
    assert calculate_total(10, 3) == 30

def test_order3():
    # test if total food order is equal to 100
    assert calculate_total(50, 2) == 100

def test_order4():
    # test if total food order is equal to 10
    assert calculate_total(5, 2) == 10

def test_order5():
    # test if total food order is equal to "invalid price"
    assert calculate_total(-5, 2) == "invalid price"
    assert calculate_total(0, 2) == "invalid price"

def test_order6():
    # test if total food order is equal to "invalid quantity"
    assert calculate_total(10, -1) == "invalid quantity"
    assert calculate_total(10, 0) == "invalid quantity"
