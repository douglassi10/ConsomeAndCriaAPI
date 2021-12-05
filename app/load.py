from flask import Flask, jsonify
import json 

# leitura do arquivo json salvo
data = open("info/numeros.json", 'r').read()
data = json.loads(data) 

server = Flask(__name__)

@server.get("/numerosordem")
def obter_numeros():
    return jsonify(data)

def retorna_instancia():
    return server

if __name__ == '__main__':
    server.run(debug=True)    

