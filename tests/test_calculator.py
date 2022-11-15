import shop_app.calculator as calc


## def test_calculator_class():
##     a_calc = calc.Calculator()
##     assert type(a_calc) == type(calc.Calculator)
def test_calculator_add():
    a_calc = calc.Calculator()
    assert a_calc.add(1,2) == 3

def test_calculator_negative_add():
    a_calc = calc.Calculator()
    assert a_calc.add(-1,-1) == -2
    