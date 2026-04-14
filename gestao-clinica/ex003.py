# Contador de Custo: Altere as funções anteriores para que elas retornem, além do
# vetor, o número de vezes que o computador precisou "mover" um dado na memória.
# Compare o custo de inserir no índice 0 vs. inserir no último índice vago.

#Ambos exercicios ex001 e ex002 tem notação Big O O(n), no caso o ex002 teve menos processamento pois eu removi o indice 7, e teve apenas
#2 deslocamento de memória do vetor para preencher o espaço vazio, porém se eu quisesse tirar o elemento[0] teria que mover todos os da frente 
#para o espaço em vazio. Assim ambos algoritmos crescem linearmente.