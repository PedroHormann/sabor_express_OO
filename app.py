from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça','gourmet')
restaurante_mexican = Restaurante('mexican food','mexicana')
restaurante_japa = Restaurante('japapei','japonesa')



def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()