def analisar_chamado(tipo_problema, ambiente, impacto, usuarios_afetados, existe_contorno, funcionalidade_critica):
    pontuacao = 0
    regras_aplicadas = []

    if ambiente == "Produção":
        pontuacao += 2
        regras_aplicadas.append("R01 - Ambiente de produção aumenta a prioridade.")

    if impacto == "Alto":
        pontuacao += 3
        regras_aplicadas.append("R02 - Impacto alto aumenta a prioridade.")
    elif impacto == "Médio":
        pontuacao += 2
        regras_aplicadas.append("R03 - Impacto médio adiciona prioridade moderada.")
    else:
        pontuacao += 1
        regras_aplicadas.append("R04 - Impacto baixo adiciona baixa prioridade.")

    if usuarios_afetados == "Muitos usuários" or usuarios_afetados == "Todos os usuários":
        pontuacao += 3
        regras_aplicadas.append("R05 - Muitos usuários afetados aumenta a prioridade.")
    elif usuarios_afetados == "Alguns usuários":
        pontuacao += 1
        regras_aplicadas.append("R06 - Alguns usuários afetados adiciona prioridade moderada.")

    if existe_contorno == "Não":
        pontuacao += 2
        regras_aplicadas.append("R07 - Ausência de solução de contorno aumenta a prioridade.")
    else:
        regras_aplicadas.append("R08 - Existência de solução de contorno reduz a urgência.")

    if funcionalidade_critica == "Sim":
        pontuacao += 2
        regras_aplicadas.append("R09 - Funcionalidade crítica aumenta a prioridade.")

    if tipo_problema == "Dúvida operacional" and existe_contorno == "Sim":
        pontuacao -= 2
        regras_aplicadas.append("R10 - Dúvida operacional com contorno reduz a prioridade.")

    if pontuacao >= 9:
        prioridade = "Crítica"
    elif pontuacao >= 6:
        prioridade = "Alta"
    elif pontuacao >= 3:
        prioridade = "Média"
    else:
        prioridade = "Baixa"

    if tipo_problema == "Erro no sistema":
        categoria = "Incidente"
        equipe = "Backend / Sustentação"
    elif tipo_problema == "Falha em integração/API":
        categoria = "Integração"
        equipe = "Backend / Integrações"
    elif tipo_problema == "Problema de acesso":
        categoria = "Acesso"
        equipe = "Segurança / Suporte"
    elif tipo_problema == "Dúvida operacional":
        categoria = "Dúvida"
        equipe = "Suporte Funcional"
    else:
        categoria = "Melhoria"
        equipe = "Produto / Requisitos"

    justificativa = f"O chamado foi classificado como {prioridade} porque atingiu {pontuacao} pontos no motor de regras."

    return {
        "prioridade": prioridade,
        "categoria": categoria,
        "equipe": equipe,
        "pontuacao": pontuacao,
        "justificativa": justificativa,
        "regras_aplicadas": regras_aplicadas
    }