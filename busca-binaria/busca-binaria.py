import collections

class Algoritmos:
    def busca_binaria(self, lista, item):
        baixo = 0
        alto = len(lista) - 1

        while baixo <= alto:
            # aqui utilizamos // para garantir a divisao inteira
            meio = (baixo + alto) // 2
            chute = lista[meio]
            if chute == item:
                return meio
            if chute > item:
                alto = meio - 1
            else:
                baixo = meio + 1                
        return None

lista = []
for i in range(129):
     lista.append(i)

algo = Algoritmos()
resultado = algo.busca_binaria(lista, 128)

print("o resultado eh: ", resultado)
