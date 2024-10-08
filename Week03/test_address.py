from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_extract_city():
    """Verify that the extract_city function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_city("1234 Zion Ave, Zion, Missouri 64079") == "Zion"
    assert extract_city("1234 Zion Ave, , Missouri 64079") == ""


def test_extract_state():
    """Verify that the extract_state function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_state("1234 Zion Ave, Zion, Missouri 64079") == "Missouri"
    assert extract_state("1234 Zion Ave, Zion, 64079") == ""

def test_extract_zipcode():
    """Verify that the extract_zipcode function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_zipcode("1234 Zion Ave, Zion, Missouri 64079") == "64079"
    assert extract_zipcode("1234 Zion Ave, Zion, Missouri") == ""


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])