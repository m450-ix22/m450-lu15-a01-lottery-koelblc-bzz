from menu import select_menu, show_menu


def test_show_menu(capsys):
    # Überprüfen, ob die Menüausgabe korrekt ist
    show_menu()
    output = capsys.readouterr().out
    assert output == (
        "Lotto\n"
        "---------\n"
        "A) Konto Ein- und Auszahlungen tätigen\n"
        "B) Lottotipps abgeben\n"
        "Z) Beenden\n"
    )

def test_select_menu_valid_input(monkeypatch):
    # Simulieren von gültigen Eingaben
    inputs = iter(["A", "B", "Z"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert select_menu() == "A"
    assert select_menu() == "B"
    assert select_menu() == "Z"

def test_select_menu_invalid_input(monkeypatch, capsys):
    # Simulieren von ungültigen Eingaben gefolgt von einer gültigen
    inputs = iter(["X", "Y", "B"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    selection = select_menu()
    output = capsys.readouterr().out
    assert "Bitte geben Sie eine gültige Wahl ein" in output
    assert selection == "B"