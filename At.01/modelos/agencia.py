from modelos.banco import Bancos

class Agencia(Bancos):
    contas = []

    def __init__(self, _nome_do_banco, _agencia, numero_da_conta):
        super().__init__(_nome_do_banco, _agencia)
        self._numero_da_conta = numero_da_conta
        self._ativa = False
        Agencia.contas.append(self)
    
    def __str__(self):
        return f'{self._nome_do_banco.ljust(25)} | {self._agencia.ljust(25)} | {str(self._numero_da_conta).ljust(25)} | {self._ativa}'
      

    def alternar_estado(self):
        self._ativa = not self._ativa

    @classmethod
    def listar_contas(cls):
        print (f'{'Nome do Banco'.ljust(25)} | {'agencia'.ljust(25)} | {'numero da conta'.ljust(25)} | {'status'} \n')
        for conta in cls.contas:
            print(f'{conta._nome_do_banco.ljust(25)} | {conta._agencia.ljust(25)} | {str(conta._numero_da_conta).ljust(25)} | {conta._ativa}')
            
