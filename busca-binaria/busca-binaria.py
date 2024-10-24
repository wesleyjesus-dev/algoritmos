import collections

# o metodo deve receber a lista e o alvo
# a lista deve esta ordenada
# define uma variavel com como baixo = indice 0
# define uma variavel alto = len(lista) -1
# fazemos o loop que executa enquanto baixo for menor ou igual a alto

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
