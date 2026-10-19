import pytest
from Converter_Of_Unit import convert_temperature, convert_length, convert_currency

def test_convert_temperature():

    assert convert_temperature(0, 'C', 'F') == 32.0
    assert convert_temperature(100, 'C', 'K') == 373.15
    assert round(convert_temperature(32, 'F', 'C'), 2) == 0.0
    with pytest.raises(ValueError):
        convert_temperature(10, 'C', 'X')

def test_convert_length():

    assert convert_length(1, 'KM', 'M') == 1000.0
    assert round(convert_length(1, 'MILE', 'KM'), 3) == 1.609
    assert round(convert_length(1, 'M', 'FOOT'), 4) == 3.2808
    with pytest.raises(ValueError):
        convert_length(10, 'CM', 'M')

def test_convert_currency():

    mock_rates = {
        'EUR': 0.95,
        'GBP': 0.80,
        'JPY': 150.0
    }

    assert convert_currency(100, 'EUR', mock_rates) == 95.0
    assert convert_currency(50, 'GBP', mock_rates) == 40.0
    with pytest.raises(ValueError):
        convert_currency(100, 'IRR', mock_rates)
