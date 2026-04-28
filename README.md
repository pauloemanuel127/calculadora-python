# Calculadora em Python 🐍

Este projeto é um sistema de calculadora desenvolvido para praticar lógica de programação e os fundamentos da linguagem Python. O foco principal foi aplicar recursos que tornem o código robusto, organizado e de fácil interação.

### 🚀 Funcionalidades Atuais

- **Operações Matemáticas:** Realiza cálculos de soma (+), subtração (-), multiplicação (*), divisão (/), potenciação (^) e radiciação (r).
- **Suporte a Números Negativos e Decimais:** O sistema interpreta corretamente entradas matemáticas complexas (ex: `-5.5 + 3`).
- **Histórico de Operações:** Armazena todos os cálculos realizados durante a execução em uma lista. O usuário pode consultar o log de operações a qualquer momento digitando o comando `hist`.
- **Validação com Expressões Regulares (Regex):** O programa utiliza a biblioteca `re` para validar e extrair as entradas do usuário, garantindo precisão e evitando travamentos por entradas inválidas de formato.
- **Lógica Matemática Específica:** O código trata divisões por zero de forma técnica, diferenciando entre **Indefinido** (X/0) e **Indeterminação** (0/0).
- **Uso Contínuo:** A calculadora opera em um loop (`while True`), permitindo múltiplas contas em sequência até que o comando `exit` seja acionado.

### 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Estruturas de Dados:** Listas para gerenciamento do histórico.
- **Expressões Regulares (Regex):** Para manipulação e validação avançada de strings e inputs.
- **Modularização:** Separação de responsabilidades (Front-end no loop principal e Back-end matemático em módulo separado).

### 📋 Como utilizar

1. Certifique-se de ter o Python instalado.
2. Certifique-se de que os arquivos `calculadora.py` e `operacoes.py` estão na mesma pasta.
3. Execute o comando no seu terminal: `python calculadora.py`.
4. **Formato de entrada:** Digite a conta com ou sem espaços (Ex: `10+20`, `-5 * 4`, ou `2 r 16`).
5. **Comandos de suporte:** Use `hist` para ver o histórico ou `exit` para sair.

### 📈 Próximos Passos (Roadmap)

Este projeto está em desenvolvimento contínuo. As metas alcançadas e futuras são:
- [x] **Modularização:** Criar funções específicas para cada operação matemática.
- [x] **Criação de Biblioteca:** Organizar a lógica de cálculos em um módulo separado (`operacoes.py`).
- [x] **Melhoria no Input:** Ajustar a lógica de entrada para aceitar expressões sem a necessidade obrigatória de espaços e com suporte a negativos.
- [ ] **Persistência de Dados:** Implementar a gravação das últimas operações em um arquivo `.txt` para acesso posterior mesmo após fechar o programa.
- [ ] **Interface Gráfica:** (Opcional) Migrar a calculadora do terminal para uma interface com janelas usando bibliotecas como `Tkinter` ou `CustomTkinter`.

---
*Projeto desenvolvido como exercício de lógica e portfólio em Python.*