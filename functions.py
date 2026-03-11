def buscar_clima(cidade: str):
    clima = {
        "sao paulo": "24°C e nublado",
        "bauru": "30°C e ensolarado",
        "curitiba": "18°C e chuvoso"
    }
    return clima.get(cidade, "Cidade não encontrado")