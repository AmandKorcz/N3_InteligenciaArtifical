import streamlit as st
import pandas as pd

from motor_regras import analisar_chamado, obter_base_conhecimento


st.set_page_config(
    page_title="Sistema Especialista de Chamados",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Sistema Especialista para Triagem de Chamados")

st.write(
    "Protótipo acadêmico de um sistema baseado em regras para classificar "
    "chamados de suporte em Engenharia de Software."
)

st.divider()

if "historico" not in st.session_state:
    st.session_state.historico = []


aba_triagem, aba_base, aba_historico = st.tabs(
    [
        "Triagem individual",
        "Base de conhecimento",
        "Histórico e indicadores"
    ]
)


with aba_triagem:
    st.subheader("Dados do chamado")

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

        st.subheader("Resultado da triagem")

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

        st.session_state.historico.append(
            {
                "Tipo do problema": tipo_problema,
                "Ambiente": ambiente,
                "Impacto": impacto,
                "Usuários afetados": usuarios_afetados,
                "Existe contorno": existe_contorno,
                "Funcionalidade crítica": funcionalidade_critica,
                "Prioridade": resultado["prioridade"],
                "Categoria": resultado["categoria"],
                "Equipe": resultado["equipe"],
                "Pontuação": resultado["pontuacao"]
            }
        )


with aba_base:
    st.subheader("Base de conhecimento do sistema")

    st.write(
        "A base de conhecimento representa o conjunto de regras utilizadas "
        "pelo sistema especialista para realizar a triagem dos chamados."
    )

    base_conhecimento = obter_base_conhecimento()

    tabela_base = pd.DataFrame(base_conhecimento)

    st.dataframe(tabela_base, use_container_width=True)

    st.info(
        "Essas regras representam o conhecimento do domínio convertido em "
        "condições e ações. O motor de inferência utiliza essas regras para "
        "classificar cada chamado."
    )


with aba_historico:
    st.subheader("Histórico e indicadores da sessão")

    if len(st.session_state.historico) == 0:
        st.warning("Nenhum chamado foi analisado ainda.")
    else:
        historico_df = pd.DataFrame(st.session_state.historico)

        total_chamados = len(historico_df)
        media_pontuacao = historico_df["Pontuação"].mean()
        prioridade_mais_comum = historico_df["Prioridade"].mode()[0]

        col1, col2, col3 = st.columns(3)

        col1.metric("Chamados analisados", total_chamados)
        col2.metric("Média de pontuação", round(media_pontuacao, 2))
        col3.metric("Prioridade mais comum", prioridade_mais_comum)

        st.write("### Histórico completo")

        st.dataframe(historico_df, use_container_width=True)

        st.write("### Chamados por prioridade")

        grafico_prioridade = historico_df["Prioridade"].value_counts()

        st.bar_chart(grafico_prioridade)

        st.write("### Chamados por categoria")

        grafico_categoria = historico_df["Categoria"].value_counts()

        st.bar_chart(grafico_categoria)

        csv = historico_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Baixar histórico em CSV",
            data=csv,
            file_name="historico_chamados.csv",
            mime="text/csv"
        )