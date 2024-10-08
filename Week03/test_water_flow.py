"""
Author: Shaun Marquis

Purpose: This program will test the functions from water_flow.py
"""
from pytest import approx
from water_flow import water_column_height, pressure_gain_from_water_height, \
pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, \
pressure_loss_from_pipe_reduction, convert_kpa_psi
import pytest

def test_water_column_height():
    """Verify that the water_column_height function works correctly.
    Parameters: none
    Return: nothing
    """

    assert water_column_height(0.0, 0.0) == 0.0
    assert water_column_height(0.0, 10.0) == 7.5
    assert water_column_height(25.0, 0.0) == 25.0
    assert water_column_height(48.3, 12.8) == 57.9

def test_pressure_gain_from_water_height():
    """Verify that the pressure_gain_from_water_height function works correctly.
    Parameters: none
    Return: nothing
    """

    assert pressure_gain_from_water_height(0.0) == approx(0.000, rel=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, rel=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, rel=0.001)

def test_pressure_loss_from_pipe():
    """Verify that the pressure_loss_from_pipe function works correctly.
    Parameters: none
    Return: nothing
    """
    assert pressure_loss_from_pipe(0.048692, 0.0, 0.018, 1.75) == approx(0.000, rel=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0.000, rel=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0.000, rel=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, rel=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, rel=0.001)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, rel=0.001)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, rel=0.001)

def test_pressure_loss_from_fittings():
    """Verify that the pressure_loss_from_fittings function works correctly.
    Parameters: none
    Return: nothing
    """
    assert pressure_loss_from_fittings(0.00, 3) == approx(0.000, rel=0.01)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0.000, rel=0.01)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, rel=0.01)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, rel=0.01)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, rel=0.01)

def test_reynolds_number():
    """Verify that the reynolds_number function works correctly.
    Parameters: none
    Return: nothing
    """
    assert reynolds_number(0.048692, 0.00) == approx(0, rel=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069, rel=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, rel=1)
    assert reynolds_number(0.286870, 1.65) == approx(471729, rel=1)
    assert reynolds_number(0.286870, 1.75) == approx(500318, rel=1)

def test_pressure_loss_from_pipe_reduction():
    """Verify that the pressure_loss_from_pipe_reduction function works correctly.
    Parameters: none
    Return: nothing
    """
    assert pressure_loss_from_pipe_reduction(0.28687, 0.0, 1, 0.048692) == approx(0.000, rel=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, rel=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, rel=0.001)

def test_convert_kpa_psi():
    """Verify that the convert_kpa_psi function works correctly.
    Parameters: none
    Return: nothing
    """
    assert convert_kpa_psi(0) == approx(0.0, rel=0.1)
    assert convert_kpa_psi(158.7) == approx(23.0, rel=0.1)
    assert convert_kpa_psi(200) == approx(29.0, rel=0.1)

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])