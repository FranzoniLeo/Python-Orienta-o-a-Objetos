from modelos.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas

    def __str__(self):
        return (f'este veiculo é da marca {self._marca}, modelo: {self._modelo}, tem como estado:{self._ligado}, o numero de portas é {self._portas}')

