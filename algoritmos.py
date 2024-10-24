class Algoritmos:
    @staticmethod
    def busca_binaria_com_loop(lista, alvo):
        baixo = 0
        alto = len(lista) - 1

        while (baixo <= alto):
            meio = (baixo + alto) // 2
            if alvo == lista[meio]:
                print('o item existe na lista e seu indice eh', meio)
                print(lista)
                return lista[meio]
            
            if alvo > lista[meio]:
                baixo += 1
            else:
                alto += -1
    
    @staticmethod
    def busca_binaria_com_recursao(lista, alvo):
        baixo = 0
        alto = len(lista) -1
        Algoritmos.busca_binaria_recursao(lista, alvo, baixo, alto)

    @staticmethod
    def busca_binaria_recursao(lista, alvo, baixo, alto):
        meio = (alto + baixo) // 2
        
        if (alvo == lista[meio]):
            print('o item existe na lista e seu indice eh', meio)
            print(lista)
            return meio
        else:
            Algoritmos.busca_binaria_recursao(lista, alvo, baixo, alto -1 if (alvo > lista[meio]) else alto -1)




Algoritmos.busca_binaria_com_loop([1,2,3,4,5,6,7,8,9,10], 5)
Algoritmos.busca_binaria_com_recursao([1,2,3,4,5,6,7,8,9,10], 5)
        