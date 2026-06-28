import streamlit as st
import pandas as pd

from N3_InteligenciaArtifical.motor_regras import analisar_chamado


st.set_page_config(
    page_title="Sistema Especialista de Chamados",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Sistema Especialista para Triagem de Chamados")

st.write(
    "Este protótipo utiliza regras de produção para classificar chamados "
    "de suporte em Engenharia de Software."
)

st.divider()

st.sidebar.header("Sobre o sistema")
st.sidebar.write(
    "O sistema recebe fatos sobre um chamado e aplica regras para inferir "
    "a prioridade, categoria e equipe responsável."
)

st.sidebar.write("Técnica utilizada: **Sistema baseado em regras**.")
st.sidebar.write("Estratégia: **Encadeamento para frente**.")


st.subheader("1. Dados do chamado")

coluna1, coluna2 = st.columns(2)

with coluna1:
    tipo_problema = st.selectbox(
        "Tipo do problema",
        [
            "Erro no sistema",
            "Falha em integração/API",
            "Problema de acesso",
            "Dúvida operacional",
            "Solicitação de melhoria"
        ]
    )

    ambiente = st.selectbox(
        "Ambiente afetado",
        [
            "Produção",
            "Homologação",
            "Desenvolvimento"
        ]
    )

    impacto = st.selectbox(
        "Impacto percebido",
        [
            "Baixo",
            "Médio",
            "Alto"
        ]
    )

with coluna2:
    usuarios_afetados = st.selectbox(
        "Quantidade de usuários afetados",
        [
            "Um usuário",
            "Alguns usuários",
            "Muitos usuários",
            "Todos os usuários"
        ]
    )

    existe_contorno = st.radio(
        "Existe solução de contorno?",
        [
            "Sim",
            "Não"
        ],
        horizontal=True
    )

    funcionalidade_critica = st.radio(
        "A funcionalidade afetada é crítica?",
        [
            "Sim",
            "Não"
        ],
        horizontal=True
    )


st.divider()

if st.button("Analisar chamado", type="primary"):
    resultado = analisar_chamado(
        tipo_problema=tipo_problema,
        ambiente=ambiente,
        impacto=impacto,
        usuarios_afetados=usuarios_afetados,
        existe_contorno=existe_contorno,
        funcionalidade_critica=funcionalidade_critica
    )

    st.subheader("2. Resultado da triagem")

    card1, card2, card3, card4 = st.columns(4)

    card1.metric("Prioridade", resultado["prioridade"])
    card2.metric("Categoria", resultado["categoria"])
    card3.metric("Equipe", resultado["equipe"])
    card4.metric("Pontuação", resultado["pontuacao"])

    st.write("### Justificativa")
    st.write(resultado["justificativa"])

    st.write("### Regras aplicadas")

    tabela_regras = pd.DataFrame(
        {
            "Regras aplicadas": resultado["regras_aplicadas"]
        }
    )

    st.dataframe(tabela_regras, use_container_width=True)