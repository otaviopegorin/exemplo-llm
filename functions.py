eventos = []

def criar_evento(titulo: str, data: str):
    evento = {
        "titulo": titulo,
        "data": data
    }
    eventos.append(evento)
    print(f"Evento criado: {titulo} em {data}")

def listar_eventos():
    if not eventos:
        print("Nenhum evento cadastrado.")
        return
    
    print("Lista de eventos:")
    for evento in eventos:
        print(f"- {evento['titulo']} | Data: {evento['data']}")