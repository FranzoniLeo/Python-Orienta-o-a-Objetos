from modelos.agencia import conta

# exemplos
conta_1 = conta('itau','001',9999)
conta_2 = conta('bb','002',76767)
# exemplos

def main():
    print(conta_1)
    print(conta_2)
    print(f' \n')

    conta_1.alternar_estado()

    conta.listar_contas()

if __name__ == '__main__':
    main()