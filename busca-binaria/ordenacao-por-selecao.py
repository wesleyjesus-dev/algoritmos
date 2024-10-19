# algoritmo de ordenacao por insercao | selection sort | 
# Ele tem complexidade O(n ^ 2) por é necessario percorer o array n vezes para ordernar
# os registros em uma nova lista
class Algoritmos:
    @staticmethod
    def buscaMenor(arr):
        menor = arr[0] # armazena o menor valor
        menor_indice = 0 # armazena o indice do menor valor
        for i in range(1, len(arr)): 
            if arr[i] < menor: # o item atual é menor que o menor valor 
                menor = arr[i] # guarda o menor valor
                menor_indice = i # atualiza o indice do menor valor
        return menor_indice # retorna o indice do menor valor
    
    @staticmethod
    def ordernacaoPorSelecao(arr):
        novoArr = []
        for i in range(len(arr)):
            menor = Algoritmos.buscaMenor(arr) # retorna o indice do menor valor
            novoArr.append(arr.pop(menor)) # adiciona na nova lista o indice de menor valor
        return novoArr
    
print(Algoritmos.ordernacaoPorSelecao([5,3,6,2,10]))