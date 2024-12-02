from authenticate import login
from person import Person


def test_login_success(monkeypatch):
    # Testdaten vorbereiten
    def mock_load_people():
        return [
            Person("TestUser1", "password1", 10.0),
            Person("TestUser2", "password2", 20.0)
        ]

    # Eingaben simulieren
    inputs = iter(["password2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('authenticate.load_people', mock_load_people)

    person = login()
    assert person.givenname == "TestUser2"
    assert person.password == "password2"
    assert person.balance == 20.0

def test_login_failure(monkeypatch):
    # Testdaten vorbereiten
    def mock_load_people():
        return [
            Person("TestUser1", "password1", 10.0),
            Person("TestUser2", "password2", 20.0)
        ]

    # Eingaben simulieren
    inputs = iter(["wrongpassword", "password1"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('authenticate.load_people', mock_load_people)

    person = login()
    assert person.givenname == "TestUser1"
    assert person.password == "password1"
    assert person.balance == 10.0