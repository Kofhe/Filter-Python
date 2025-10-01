#faça o filtro de numeros negativos
numeros = [-1, -2, 0, 1,2,3,4,5,6,7,8,9,10]
negativos = list(filter(lambda x : x < 0 ,numeros))
print(negativos)
