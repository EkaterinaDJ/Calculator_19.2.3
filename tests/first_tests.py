import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 5, 5) == 25


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 35, 5) == 7

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 35, 5) == 30

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 35, 5) == 40

