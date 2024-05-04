ldef escolher_estrategia(cenario):
    if "transicao de aplicativo sem valor comercial" in cenario:
        return "retire"
    elif "aplicativo com necessidade de adiar sua migracao para a nuvem" in cenario:
        return "retain"
    elif "substituir o aplicativo por uma versao ou produto diferente" in cenario:
        return "repurchase"
    elif "modificar a arquitetura do aplicativo" in cenario:
        return "refactor or re-architect"
    elif "mover aplicativos para a nuvem sem modifica-los" in cenario:
        return "rehost"
    elif "introduzir otimizacoes no aplicativo para opera-lo de forma eficiente" in cenario:
        return "replatform"
    elif "transferir servidores ou instancias para outra plataforma na nuvem" in cenario:
        return "relocate"
    else:
        return "Estratégia não encontrada"

entrada = input()
print(escolher_estrategia(entrada))