from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Laís', 8)
restaurante_praca.receber_avaliacao('Emy', 2)

restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_mexicano.receber_avaliacao('Ana', 9)
restaurante_mexicano.receber_avaliacao('Carlos', 7)

restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_japones.receber_avaliacao('Pedro', 8)
restaurante_japones.receber_avaliacao('Maria', 6)
restaurante_japones.receber_avaliacao('João', 7)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
