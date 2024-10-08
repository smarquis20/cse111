from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert make_full_name("Shaun", "Marquis") == "Marquis; Shaun"
    assert make_full_name("Bk", "Stevenson") == "Stevenson; Bk"
    assert make_full_name("", "") == "; "


def test_extract_family_name():
    """Verify that the extract_family_name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_family_name("Marquis; Shaun") == "Marquis"
    assert extract_family_name("Stevenson; Bk") == "Stevenson"
    assert extract_family_name("; ") == ""

def test_extract_given_name():
    """Verify that the extract_given_name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_given_name("Marquis; Shaun") == "Shaun"
    assert extract_given_name("Stevenson; Bk") == "Bk"
    assert extract_given_name("; ") == ""


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])