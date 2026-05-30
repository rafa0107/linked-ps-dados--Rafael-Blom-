# 📊 Dashboard de Análise de Vendas — Linked PS

> Solução desenvolvida para o desafio técnico de Análise de Dados e Visualização de Informações.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
</p>

---

## 📌 Objetivo do Projeto

Este projeto tem como objetivo realizar a **Análise Exploratória (EDA)** e **Analítica** de uma base de dados de e-commerce contendo 1.200 pedidos. A proposta consistiu em transformar dados brutos de vendas em inteligência de negócios, estruturando indicadores operacionais estratégicos e disponibilizando os resultados através de um **Dashboard Interativo em Streamlit**.

A modelagem dimensional e as validações métricas de apoio foram estruturadas em paralelo utilizando o **Power BI** para garantir a consistência centavo por centavo de todas as visões de negócio apresentadas.

---

## 🚀 Demonstração (Deploy Online)

O dashboard está publicado e pode ser acessado publicamente em qualquer dispositivo através do link abaixo:
🔗 **[Acesse o Dashboard Interativo Aqui](https://linked-ps-dados-rafael-blom.streamlit.app/)**

---

## 🛠️ Tecnologias e Ferramentas

* **Linguagem Principal:** Python 3.x
* **Manipulação de Dados:** Pandas & NumPy
* **Visualização Interativa:** Plotly Express
* **Interface Web & Dashboard:** Streamlit
* **Design & Validação Analítica:** Power BI Desktop

---

## 📂 Estrutura do Repositório

```text
LINKED-PS-DADOS-RAFAEL-BLOM-
│
├── app.py                      # Arquivo principal (Página Inicial / Navegação)
├── requirements.txt            # Dependências do ecossistema Python
├── README.md                   # Documentação do projeto
│
├── data/                       # Camada de Persistência dos Dados (CSVs)
│   ├── f_vendas_tratada.csv    # Tabela Fato de Vendas processada e higienizada
│   └── d_calendario.csv        # Tabela Dimensão Calendário para análises temporais
│
├── src/                        # Módulos e scripts de suporte
│   ├── __init__.py
│   └── loader.py               # Otimização de carga de dados e cache do Streamlit
│
├── pages/                      # Páginas do Dashboard Multipage do Streamlit
│   ├── 01_ANALISE_DESCRITIVA.py
│   └── 02_ANALISE_AVANCADA.py
│
└── notebooks/                  # Ambiente de Desenvolvimento e Prototipagem
    └── teste_linked.ipynb      # Pipeline de EDA e extração de insights em Python
```


## 🔄 Ciclo de Desenvolvimento & Engenharia dos Dados

Todo o pipeline de extração, tratamento e modelagem analítica foi prototipado e validado no nosso **[🧪 Jupyter Notebook de Desenvolvimento](notebooks/teste_linked.ipynb)** antes de ser modularizado para o ecossistema do Streamlit.

### <span style="color:#8B242E">1. Análise Exploratória Inicial (EDA)</span>
Exploração e diagnóstico da integridade da base para mapear a volumetria, distribuição geográfica dos clientes, representatividade das categorias de produtos, métodos de pagamento preferidos e severidade dos status de cancelamento.

### <span style="color:#8B242E">2. Visão Analítica Descritiva</span>
Montagem de uma matriz de KPIs operacionais macro e análises de posicionamento de mercado:
* **Métricas Principais:** Receita Bruta, Receita Líquida, Ticket Médio, Volumetria de Pedidos e Taxa de Cancelamento.
* **Visões de Mercado:** Quebra de faturamento por região, identificação dos Top 5 produtos mais vendidos por volume físico e por receita financeira, e preço médio praticado por categoria de item.

### <span style="color:#8B242E">3. Visão Analítica Avançada & Cruzamento de Dados</span>
Cruzamento de dimensões para identificação de padrões de comportamento comercial ocultos:
* **Segmentação de Portfólio:** Classificação dinâmica dos produtos em faixas de preço (*Baixo Valor, Médio Valor e Premium*) para analisar a participação de cada cluster na receita total.
* **Análise de Sazonalidade Temporal:** Mapeamento do fluxo de faturamento por dias da semana para identificar janelas de maior conversão de vendas.
* **Risco de Dependência de SKU:** Cálculo analítico do impacto do produto líder de vendas sobre a receita global para alertar contra riscos de ruptura de estoque ou flutuações de mercado.
* **Matriz de Correlação de Cancelamentos:** Relacionamento entre produtos, métodos de pagamento e volume de ordens canceladas para isolar riscos de gargalos operacionais ou fraudes.

---

## 📊 Estrutura das Páginas do Dashboard

### 📈 <span style="color:#8B242E">Aba 01: Análise Descritiva</span>
Focada em responder o panorama atual do negócio através de visuais limpos e diretos:
* **KPIs Operacionais:** Cartões de indicadores financeiros e volumetria atualizados.
* **Geografia do Negócio:** Gráfico de Distribuição Geográfica de pedidos e faturamento.
* **Rankings Comerciais:** Top 5 de produtos por quantidade vendida e por receita gerada.
* **Distribuição Operacional:** Análise de representatividade de Métodos de Pagamento e Status dos pedidos.

### 🚀 <span style="color:#8B242E">Aba 02: Análise Avançada</span>
Focada no direcionamento estratégico e tomadas de decisão de alto nível:
* **Evolução de Performance:** Análise temporal e linhas de tendência da receita líquida.
* **Comportamento Cruzado:** Gráficos relacionais de Sazonalidade Semanal e Faixas de Preço.
* **Gestão de Riscos:** Indicadores visuais de Risco de Portfólio (SKU Líder).
* **Diagnóstico Operacional:** Gráficos de dispersão/barras para mapeamento da Correlação de Cancelamentos.

---

## 💻 <span style="color:#8B242E">Como Executar o Projeto Localmente</span>

Siga os passos abaixo para replicar o ambiente de desenvolvimento e executar o dashboard na sua máquina:

1. **Clone o repositório:**
```bash
    git clone [https://github.com/seu-usuario/linked-ps-dados--Rafael-Blom-.git](https://github.com/seu-usuario/linked-ps-dados--Rafael-Blom-.git)
    cd linked-ps-dados--Rafael-Blom-
```
2. **Crie e Ative o Ambiente Virtual(Venv):**

```bash
    python -m venv .venv
    source .venv/bin/activate  # No Linux/Mac
    # No Windows use: .venv\Scripts\activate
```

3. **Instale as Dependências:**

```bash
    pip install -r requirements.txt
```

4. **Execute a Aplicação Streamlit**

```bash
    streamlit run Dashboard_de_Vendas.py
```
5. **O navegador abrirá automaticamente o endereço local: http://localhost:8501**

## 💻 <span style="color:#8B242E">Principais Aprendizados Aplicados</span>

Durante o ciclo de engenharia e modelagem deste desafio, foram consolidados conceitos práticos essenciais para a atuação em Data Science e Business Intelligence:

* **Manipulação de Dados Avançada:** Limpeza, tratamento de nulos, junções de tabelas e agregações temporais utilizando a biblioteca Pandas.

* **Data Storytelling Visual:** Seleção estruturada de gráficos (barras comparativas, dispersão e linhas temporais) com Plotly Express, respeitando estritamente a paleta de cores institucionais do processo seletivo para garantir sobriedade e elegância.

* **Métricas de Negócio Reais:** Modelagem e cálculo de indicadores fiéis ao mercado corporativo, como Ticket Médio Real, taxas de conversão de métodos de pagamento, quebra geográfica e análise crítica de portfólio (risco de dependência de SKU).

* **Arquitetura de Software Multipage:** Organização modular de diretórios e arquivos para construção de aplicações web robustas e escaláveis via Streamlit.

## 💻 <span style="color:#8B242E">👨‍💻 Autor</span>

* **Rafael Andrade Blom Gurgel**

* **Estudante de Ciência da Computação — Federal University of São João del-Rei (UFSJ)**
