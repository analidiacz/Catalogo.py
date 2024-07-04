# Inicializando o catálogo
catalogo = {}

# Função para adicionar filmes
def adicionar_filme(catalogo, titulo, diretor, ano, genero, comentarios=[]):
    catalogo[titulo] = {
        "diretor": diretor,
        "ano": ano,
        "genero": genero,
        "comentarios": comentarios
    }

# Função para atualizar filmes
def atualizar_filme(catalogo, titulo, diretor=None, ano=None, genero=None, comentarios=None):
    if titulo in catalogo:
        if diretor:
            catalogo[titulo]["diretor"] = diretor
        if ano:
            catalogo[titulo]["ano"] = ano
        if genero:
            catalogo[titulo]["genero"] = genero
        if comentarios:
            catalogo[titulo]["comentarios"] = comentarios
    else:
        print(f"Filme '{titulo}' não encontrado no catálogo.")

# Função para visualizar o catálogo
def visualizar_catalogo(catalogo):
    for titulo, info in catalogo.items():
        print(f"Titulo: {titulo}")
        print(f"Diretor: {info['diretor']}")
        print(f"Ano: {info['ano']}")
        print(f"Gênero: {info['genero']}")
        print(f"Comentários: {info['comentarios']}")
        print()

# Adicionando filmes
adicionar_filme(catalogo, "Matrix", "Lana Wachowski", 1999, "Ficção Científica")
adicionar_filme(catalogo, "Inception", "Christopher Nolan", 2010, "Ação/Suspense")
adicionar_filme(catalogo, "Jogos Vorazes", "Gary Ross", 2012, "Aventura/Ficção Científica", comentarios=["Ótimo filme!", "Adaptação fiel ao livro."])

# Atualizando um filme
atualizar_filme(catalogo, "Matrix", genero="Ficção Científica/Ação")

# Visualizando o catálogo
visualizar_catalogo(catalogo)