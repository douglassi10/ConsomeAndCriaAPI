import requests
import json

# Extract
lista = []
for i in range(1, 10001): # vai da primeira a última página
    while 1:
        r = requests.get('http://challenge.dienekes.com.br/api/numbers?page=' + str(i))
        # se o status for diferente de 200 tenta o request novamente
        if (r.status_code == 200):
            lista.extend(r.json()['numbers']) # adiciona os números de cada página na lista
            print('carregando... ' + str(len(lista)) + ' numeros adicionados.')
            break

# Transform
def quick_transform(list):
    if len(list) <= 1:
        return list
    pivot = list.pop()
    inferiores = [n for n in list if n < pivot]
    ordem_lista = quick_transform(inferiores)
    ordem_lista.append(pivot)
    superiores = [n for n in list if n >= pivot]  
    ordem_lista.extend(quick_transform(superiores))
    return ordem_lista  

# gera arquivo json que pode ser consumido mesmo que a api dienekes não funcione
obj = {'chave': quick_transform(lista)}
out_file = open("info/numeros.json", "w")
json.dump(obj, out_file, indent = 4)
out_file.close()