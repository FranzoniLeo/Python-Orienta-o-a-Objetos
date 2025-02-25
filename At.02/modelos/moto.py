from modelos.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo
        
    def __str__(self):
        return (f'este veiculo é da marca {self._marca}, e do modelo: {self._modelo}, tem como estado: {self._ligado}, o seu estilo é {self._tipo}')