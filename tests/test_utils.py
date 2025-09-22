from utils import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(2, 3) == 5

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(10, 0) == "Error: división entre cero"
