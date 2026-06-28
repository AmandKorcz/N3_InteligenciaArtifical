from N3_InteligenciaArtifical.motor_regras import analisar_chamado

resultado = analisar_chamado(
    tipo_problema="Erro no sistema",
    ambiente="Produção",
    impacto="Alto",
    usuarios_afetados="Todos os usuários",
    existe_contorno="Não",
    funcionalidade_critica="Sim"
)

print("Prioridade:", resultado["prioridade"])
print("Categoria:", resultado["categoria"])
print("Equipe responsável:", resultado["equipe"])
print("Pontuação:", resultado["pontuacao"])
print("Justificativa:", resultado["justificativa"])

print("\nRegras aplicadas:")
for regra in resultado["regras_aplicadas"]:
    print("-", regra)