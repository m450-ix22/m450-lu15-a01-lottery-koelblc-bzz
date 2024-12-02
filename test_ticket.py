import pytest

from authenticate import load_people
from lottery import create_ticket
from money import transfer_money
from numeric_input import read_int, read_float
from person import Person
from ticket import Ticket


def test_read_int_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "10")
    assert read_int("Test Prompt", 1, 20) == 10

def test_read_int_out_of_range(monkeypatch, capsys):
    inputs = iter(["50", "10"])  # First input is invalid, second valid
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert read_int("Test Prompt", 1, 20) == 10
    output = capsys.readouterr().out
    assert "Eingabe ist zu gross oder zu klein" in output

def test_read_float_invalid(monkeypatch, capsys):
    inputs = iter(["abc", "10.5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert read_float("Test Prompt", 1.0, 20.0) == 10.5
    output = capsys.readouterr().out
    assert "Geben Sie eine Zahl ein" in output

def test_ticket_numbers():
    ticket = Ticket(5, [])
    ticket.numbers = [1, 2, 3, 4, 5, 6]
    assert ticket.numbers == [1, 2, 3, 4, 5, 6]
    with pytest.raises(ValueError):
        ticket.joker = "invalid"

def test_integration_ticket_creation(monkeypatch):
    person = Person("TestUser", "password", 10.0)
    inputs = iter(["10", "20", "30", "40", "12", "15", "2"])  # Dummy-Inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    create_ticket(person)
    assert person.balance == 8.0  # 2 Euro abgezogen

