from modelos.restaurante import Restaurante

restaurante_JJ = Restaurante('JJ Food', 'Fast Food')
restaurante_Cat = Restaurante('Cat Cafe', 'Cafe')
restaurante_Hello = Restaurante('Hello Kitty', 'Japonesa')

restaurante_JJ.receber_avaliacao('Iza', 10)
restaurante_JJ.receber_avaliacao('Belli', 8.5)
restaurante_Cat.receber_avaliacao('Maria', 8)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()