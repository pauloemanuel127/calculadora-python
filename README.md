# Calculadora em Python 🐍

Este projeto é um sistema de calculadora desenvolvido para praticar lógica de programação e os fundamentos da linguagem Python. O foco principal foi aplicar recursos que tornem o código robusto, organizado e de fácil interação.

### 🚀 Funcionalidades Atuais

- **Operações Básicas:** Realiza cálculos de soma, subtração, multiplicação e divisão.
- **Histórico de Operações:** Armazena todos os cálculos realizados durante a execução em uma lista. O usuário pode consultar o log de operações digitando o comando `hist`.
- **Tratamento de Erros (Try/Except):** O programa utiliza blocos de exceção para evitar interrupções caso o usuário digite valores inválidos ou formatos incorretos.
- **Lógica Matemática Específica:** O código trata divisões por zero de forma técnica, diferenciando entre **Indefinido** (X/0) e **Indeterminação** (0/0).
- **Uso Contínuo:** A calculadora opera em um loop (`while True`), permitindo múltiplas contas em sequência até que o comando `exit` seja acionado.

### 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Estruturas de Dados:** Listas para gerenciamento do histórico.
- **Controle de Fluxo:** Estruturas condicionais (`if/elif/else`) e loops de repetição.
- **Tratamento de Exceções:** Uso de `try/except` para validação de tipos.

### 📋 Como utilizar

1. Certifique-se de ter o Python instalado.
2. Baixe o arquivo `calculadora.py`.
3. Execute o comando no seu terminal: `python calculadora.py`.
4. **Formato de entrada:** Digite a conta separando os termos por espaço (Ex: `10 + 20`).
5. **Comandos de suporte:** Use `hist` para ver o histórico ou `exit` para sair.

### 📈 Próximos Passos (Roadmap)

Este projeto está em desenvolvimento e as próximas implementações previstas são:
- [ ] **Modularização:** Criar funções específicas para cada operação matemática.
- [ ] **Persistência de Dados:** Implementar a gravação das últimas 10 operações em um arquivo `.txt` para acesso posterior.
- [ ] **Criação de Biblioteca:** Organizar a lógica de cálculos em um módulo separado.
- [ ] **Melhoria no Input:** Ajustar a lógica de entrada para aceitar expressões sem a necessidade obrigatória de espaços.

---
*Projeto desenvolvido como exercício de lógica e portfólio em Python.*