def consultar_status_pedido(pedido_id: int):
    pedidos = {
        1029: "Em separação",
        2040: "Enviado",
        3001: "Entregue"
    }
    return pedidos.get(pedido_id, "Pedido não encontrado")

def gerar_boleto(email: str):
    return f"Boleto gerado e enviado para {email}"

def agendar_consulta(data: str, hora: str):
    return f"Consulta agendada para {data} às {hora}"