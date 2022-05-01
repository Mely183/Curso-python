

# def potencia(numero):

#     potencia = 1
    
#     while (potencia <= 5):

#         result = numero ** potencia
#         print ('Potencia de {} elevado a la {} es {}' . format(numero, potencia, result))
#         potencia += 1

# def run ():
#     numero = int (input ('Escribe el número al cual quieres averiguarle la potencia : '))
#     potencia(numero)


# if __name__ == "__main__":
#     run()
    

from contextlib import ContextDecorator


def run():
    LIMITE = 1000

    contador = 0
    potencia_2 = 2** contador
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + 'es igual a: ' + potencia_2)

if __name__ == '__main__':
    run()
    
    