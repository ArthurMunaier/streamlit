import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Acidentes De Trânsito - MG", layout="wide")

dados_hardcoded = [
    {"NOMEUP": "Taquaril", "ANO": 2023, "SERIE": "SERIE HISTORICA", "IQVU": 0.412, "Educacao": 0.39, "Saude": 0.42, "Habitacao": 0.45, "Infraestrutura": 0.38, "Cultura": 0.42},
    {"NOMEUP": "Taquaril", "ANO": 2023, "SERIE": "SERIE HISTORICA", "IQVU": 0.448, "Educacao": 0.43, "Saude": 0.45, "Habitacao": 0.48, "Infraestrutura": 0.42, "Cultura": 0.46},
    {"NOMEUP": "Taquaril", "ANO": 2023, "SERIE": "SERIE HISTORICA", "IQVU": 0.485, "Educacao": 0.47, "Saude": 0.49, "Habitacao": 0.51, "Infraestrutura": 0.46, "Cultura": 0.49},
    {"NOMEUP": "Taquaril", "ANO": 2023, "SERIE": "SERIE HISTORICA", "IQVU": 0.512, "Educacao": 0.50, "Saude": 0.52, "Habitacao": 0.54, "Infraestrutura": 0.49, "Cultura": 0.51},
    {"NOMEUP": "Taquaril", "ANO": 2023, "SERIE": "SERIE HISTORICA", "IQVU": 0.530, "Educacao": 0.52, "Saude": 0.54, "Habitacao": 0.55, "Infraestrutura": 0.51, "Cultura": 0.53},
    {"NOMEUP": "Taquaril", "ANO": 2023, "SERIE": "SERIE HISTORICA", "IQVU": 0.549, "Educacao": 0.54, "Saude": 0.55, "Habitacao": 0.57, "Infraestrutura": 0.53, "Cultura": 0.55},
    {"NOMEUP": "Taquaril", "ANO": 2023, "SERIE": "SERIE HISTORICA", "IQVU": 0.568, "Educacao": 0.56, "Saude": 0.57, "Habitacao": 0.59, "Infraestrutura": 0.55, "Cultura": 0.57},

    {"NOMEUP": "Santa Ines", "ANO": 2023, "SERIE": "SERIE HISTORICA", "IQVU": 0.615, "Educacao": 0.63, "Saude": 0.60, "Habitacao": 0.64, "Infraestrutura": 0.61, "Cultura": 0.59},
    {"NOMEUP": "Santa Ines", "ANO": 2023, "SERIE": "SERIE HISTORICA", "IQVU": 0.642, "Educacao": 0.66, "Saude": 0.63, "Habitacao": 0.66, "Infraestrutura": 0.64, "Cultura": 0.62},
    {"NOMEUP": "Santa Ines", "ANO": 2023, "SERIE": "SERIE HISTORICA", "IQVU": 0.678, "Educacao": 0.69, "Saude": 0.67, "Habitacao": 0.70, "Infraestrutura": 0.67, "Cultura": 0.66},
    {"NOMEUP": "Santa Ines", "ANO": 2023, "SERIE": "SERIE HISTORICA", "IQVU": 0.705, "Educacao": 0.72, "Saude": 0.70, "Habitacao": 0.72, "Infraestrutura": 0.69, "Cultura": 0.69},
    {"NOMEUP": "Santa Ines", "ANO": 2023, "SERIE": "SERIE HISTORICA", "IQVU": 0.721, "Educacao": 0.74, "Saude": 0.71, "Habitacao": 0.74, "Infraestrutura": 0.71, "Cultura": 0.70},
    {"NOMEUP": "Santa Ines", "ANO": 2023, "SERIE": "SERIE HISTORICA", "IQVU": 0.739, "Educacao": 0.75, "Saude": 0.73, "Habitacao": 0.76, "Infraestrutura": 0.73, "Cultura": 0.72},
    {"NOMEUP": "Santa Ines", "ANO": 2023, "SERIE": "SERIE HISTORICA", "IQVU": 0.756, "Educacao": 0.77, "Saude": 0.75, "Habitacao": 0.78, "Infraestrutura": 0.74, "Cultura": 0.74},

    {"NOMEUP": "Taquaril", "ANO": 2023, "SERIE": "NOVA SERIE", "IQVU": 0.510, "Educacao": 0.50, "Saude": 0.51, "Habitacao": 0.52, "Infraestrutura": 0.50, "Cultura": 0.52},
    {"NOMEUP": "Santa Ines", "ANO": 2023, "SERIE": "NOVA SERIE", "IQVU": 0.710, "Educacao": 0.72, "Saude": 0.70, "Habitacao": 0.71, "Infraestrutura": 0.70, "Cultura": 0.72},
    {"NOMEUP": "Centro", "ANO": 2023, "SERIE": "SERIE HISTORICA", "IQVU": 0.812, "Educacao": 0.80, "Saude": 0.82, "Habitacao": 0.81, "Infraestrutura": 0.83, "Cultura": 0.80},
]

df = pd.DataFrame(dados_hardcoded)

df_filtrado = df[
    (df["NOMEUP"].isin(["Taquaril", "Santa Ines"])) &
    (df["SERIE"] == "SERIE HISTORICA")
].copy()

df_tabela = df_filtrado[["NOMEUP", "ANO", "IQVU"]]

st.title("Painel Streamlit de Acidentes em MG")

st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])

if opcao == "Tabela":
    st.header("Tabela Acidentes de MG")
    st.dataframe(df_tabela, use_container_width=True, hide_index=True)

elif opcao == "Gráficos":
    st.header("Gráficos Acidentes de MG")

    st.subheader("1. Gráfico de Linha")
    df_taquaril = df_tabela[df_tabela["NOMEUP"] == "Taquaril"]

    fig_linha_taquaril = px.line(
        df_taquaril,
        x="ANO",
        y="IQVU",
        markers=True,
        title="Evolução do IQVU — Taquaril (1994 a 2016)",
        template="plotly_dark"
    )
    fig_linha_taquaril.update_traces(line_color="#FF6B6B", line_width=3, marker_size=8)
    fig_linha_taquaril.update_xaxes(type="category")
    fig_linha_taquaril.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_linha_taquaril, use_container_width=True)

    st.subheader("2. Gráfico de Linha")
    df_santa_ines = df_tabela[df_tabela["NOMEUP"] == "Santa Ines"]

    fig_linha_santa_ines = px.line(
        df_santa_ines,
        x="ANO",
        y="IQVU",
        markers=True,
        title="Evolução do IQVU — Santa Inês (1994 a 2016)",
        template="plotly_dark"
    )
    fig_linha_santa_ines.update_traces(line_color="#00F5D4", line_width=3, marker_size=8)
    fig_linha_santa_ines.update_xaxes(type="category")
    fig_linha_santa_ines.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_linha_santa_ines, use_container_width=True)

    st.subheader("3. Gráfico de Barras Agrupadas")
    fig_barras = px.bar(
        df_tabela,
        x="ANO",
        y="IQVU",
        color="NOMEUP",
        barmode="group",
        title="Comparativo Anual de IQVU (Barras Agrupadas)",
        color_discrete_map={"Taquaril": "#FF6B6B", "Santa Ines": "#00F5D4"},
        template="plotly_dark"
    )
    fig_barras.update_xaxes(type="category")
    fig_barras.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_barras, use_container_width=True)

    st.subheader("4. Gráfico de Barras Empilhadas (Dimensões em 2016)")
    dados_empilhado = pd.DataFrame([
        {"Bairro": "Taquaril", "Dimensao": "Educação", "Valor": 0.56},
        {"Bairro": "Taquaril", "Dimensao": "Saúde", "Valor": 0.57},
        {"Bairro": "Taquaril", "Dimensao": "Habitação", "Valor": 0.59},
        {"Bairro": "Taquaril", "Dimensao": "Infraestrutura", "Valor": 0.55},
        {"Bairro": "Taquaril", "Dimensao": "Cultura", "Valor": 0.57},
        {"Bairro": "Santa Ines", "Dimensao": "Educação", "Valor": 0.77},
        {"Bairro": "Santa Ines", "Dimensao": "Saúde", "Valor": 0.75},
        {"Bairro": "Santa Ines", "Dimensao": "Habitação", "Valor": 0.78},
        {"Bairro": "Santa Ines", "Dimensao": "Infraestrutura", "Valor": 0.74},
        {"Bairro": "Santa Ines", "Dimensao": "Cultura", "Valor": 0.74},
    ])

    fig_empilhado = px.bar(
        dados_empilhado,
        x="Bairro",
        y="Valor",
        color="Dimensao",
        barmode="stack",
        title="Composição do IQVU por Dimensão — Ano 2016 (Barras Empilhadas)",
        template="plotly_dark"
    )
    fig_empilhado.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_empilhado, use_container_width=True)

    st.subheader("5. Gráfico de Pizza")
    dados_pizza = pd.DataFrame([
        {"Bairro": "Taquaril", "IQVU": 0.568},
        {"Bairro": "Santa Ines", "IQVU": 0.756},
    ])

    fig_pizza = px.pie(
        dados_pizza,
        names="Bairro",
        values="IQVU",
        title="Proporção do IQVU entre os Bairros (2016)",
        color="Bairro",
        color_discrete_map={"Taquaril": "#FF6B6B", "Santa Ines": "#00F5D4"},
        template="plotly_dark"
    )
    fig_pizza.update_traces(textinfo="percent+label+value")
    fig_pizza.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_pizza, use_container_width=True)

    st.subheader("6. Gráfico de Radar (px.line_polar)")
    dados_radar = pd.DataFrame([
        {"Bairro": "Taquaril", "Dimensao": "Educação", "Nota": 0.56},
        {"Bairro": "Taquaril", "Dimensao": "Saúde", "Nota": 0.57},
        {"Bairro": "Taquaril", "Dimensao": "Habitação", "Nota": 0.59},
        {"Bairro": "Taquaril", "Dimensao": "Infraestrutura", "Nota": 0.55},
        {"Bairro": "Taquaril", "Dimensao": "Cultura", "Nota": 0.57},
        {"Bairro": "Santa Ines", "Dimensao": "Educação", "Nota": 0.77},
        {"Bairro": "Santa Ines", "Dimensao": "Saúde", "Nota": 0.75},
        {"Bairro": "Santa Ines", "Dimensao": "Habitação", "Nota": 0.78},
        {"Bairro": "Santa Ines", "Dimensao": "Infraestrutura", "Nota": 0.74},
        {"Bairro": "Santa Ines", "Dimensao": "Cultura", "Nota": 0.74},
    ])

    fig_radar = px.line_polar(
        dados_radar,
        r="Nota",
        theta="Dimensao",
        color="Bairro",
        line_close=True,
        title="Perfil Multidimensional (Gráfico de Radar - 2016)",
        color_discrete_map={"Taquaril": "#FF6B6B", "Santa Ines": "#00F5D4"},
        template="plotly_dark"
    )
    fig_radar.update_traces(fill="toself")
    fig_radar.update_layout(
        polar=dict(bgcolor="#1E293B", radialaxis=dict(visible=True, range=[0, 1])),
        paper_bgcolor="#111827"
    )
    st.plotly_chart(fig_radar, use_container_width=True)

    st.subheader("7. Gráfico de Área")
    fig_area = px.area(
        df_tabela,
        x="ANO",
        y="IQVU",
        color="NOMEUP",
        title="Evolução em Área do IQVU (1994 a 2016)",
        color_discrete_map={"Taquaril": "#FF6B6B", "Santa Ines": "#00F5D4"},
        template="plotly_dark"
    )
    fig_area.update_xaxes(type="category")
    fig_area.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_area, use_container_width=True)

    st.subheader("8. Gráfico de Dispersão")
    fig_dispersao = px.scatter(
        df_filtrado,
        x="Educacao",
        y="Saude",
        color="NOMEUP",
        size="IQVU",
        hover_data=["ANO"],
        title="Dispersão: Educação vs Saúde (Tamanho = IQVU)",
        color_discrete_map={"Taquaril": "#FF6B6B", "Santa Ines": "#00F5D4"},
        template="plotly_dark"
    )
    fig_dispersao.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_dispersao, use_container_width=True)

    st.subheader("9. Gráfico Boxplot")
    fig_box = px.box(
        df_tabela,
        x="NOMEUP",
        y="IQVU",
        color="NOMEUP",
        points="all",
        title="Distribuição Estatística do IQVU (Boxplot)",
        color_discrete_map={"Taquaril": "#FF6B6B", "Santa Ines": "#00F5D4"},
        template="plotly_dark"
    )
    fig_box.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_box, use_container_width=True)

st.markdown("---")
st.caption("Fonte dos dados: dados abertos da Prefeitura de Belo Horizonte — https://basedosdados.org/")