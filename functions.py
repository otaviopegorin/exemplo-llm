def buscar_produto(nome_produto: str):
    produtos = {
        "notebook": 4500,
        "mouse": 80,
        "teclado": 150
    }
    return produtos.get(nome_produto, "Pedido não encontrado")

def verificar_estoque(nome_produto: str):
    estoque = {
    "notebook": 5,
    "mouse": 20,
    "teclado": 8
    }
    return estoque.get(nome_produto, "Pedido não encontrado") > 0