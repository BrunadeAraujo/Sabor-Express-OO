from modelos.restaurante import Restaurante


restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avalicao('gui', 10)
restaurante_praca.receber_avalicao('Bru', 8)
restaurante_praca.receber_avalicao('tutu', 9)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()