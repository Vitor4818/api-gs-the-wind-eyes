from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Adicionando o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite requisições de qualquer origem (use "*" para permitir todas as origens)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Defina suas rotas
@app.get("/ranking")
def get_ranking():
    # Lista de empresas com seus percentuais
    empresas = [
        {"nome_empresa": "Greentech", "percentual": 9},
        {"nome_empresa": "Suzano", "percentual": 42},
        {"nome_empresa": "Siemens", "percentual": 32},
        {"nome_empresa": "Ambev", "percentual": 25},
        {"nome_empresa": "Itaú", "percentual": 55},
    ]

    # Ordena a lista de empresas pelo percentual de forma decrescente
    ranking_ordenado = sorted(empresas, key=lambda x: x['percentual'], reverse=True)

    # Adiciona a posição do ranking (1º, 2º, 3º, ...)
    for index, empresa in enumerate(ranking_ordenado):
        empresa['ranking'] = index + 1

    return ranking_ordenado
