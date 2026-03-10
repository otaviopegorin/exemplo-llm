def buscar_produto(nome_produto: str):
    produtos = {
        "notebook": 4500,
        "mouse": 80,
        "teclado": 150
    }
    return produtos.get(nome_produto, "Pedido não encontrado")
