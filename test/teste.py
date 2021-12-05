import requests 

list_unitaria = [4]
list_aleatoria = [0.3, 0.6, 0.2, 0.5, 0.1, 0.4]

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

def test_list_unitaria():
    assert quick_transform(list_unitaria) == [4]

def test_lista_aleatoria():
    assert quick_transform(list_aleatoria) == [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

# conexao a api bem sucedida
def test_is_conect(client):
    assert client.get('/numerosordem').status_code == 200

def test_acess_pag_not_found(client):
    assert client.get('/qualquercoisa').status_code == 404

    
      

    