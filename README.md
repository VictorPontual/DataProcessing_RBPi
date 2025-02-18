# 📊 Controle Estatístico de Processos (CEP)

## 📌 Sobre o Projeto
Este projeto é uma aplicação para melhor compreensão do **Controle Estatístico de Processos (CEP)**. Ele fornece simulações de dados estatísticos, ajudando na análise de variabilidade e controle de qualidade em processos industriais.

## ✨ Funcionalidades
- Geração de **dados simulados** para análise estatística
- Cálculo de:
  - **Média**
  - **Amplitude**
  - **Limites Superior e Inferior**
  - **Desvio Padrão**
  - **Índices de Capacidade do Processo (Cp e Cpk)**
- Identificação de **outliers**
- Implementação das **4 regras da Western Electric**
- **Plotagem gráfica interativa** (gráficos atualizados dinamicamente com novos dados)

## 📈 Visualização
A aplicação gera gráficos interativos que são atualizados automaticamente à medida que novos dados chegam, permitindo um acompanhamento em tempo real da performance do processo.

## 🛠 Tecnologias Utilizadas
- [Linguagem e bibliotecas utilizadas: matplotlib,fastapi,uvicorn,pydantic,requests,websockets]

## 🚀 Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/VictorPontual/DataProcessing_RBPi.git -b Enzo
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd DataProcessing_RBPi
   ```
3. Abra WEB e RBPi separadamente e baixe suas dependencias separadamente.

4. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute a aplicação:
   ```bash
   python main.py
   ```
6. Acesse a aplicação em **localhost** para facilitar os testes:
   ```
   http://localhost:5000
   ```
7. Caso precise compartilhar externamente, a aplicação já foi testada com o **ngrok** e funcionou perfeitamente.

---
