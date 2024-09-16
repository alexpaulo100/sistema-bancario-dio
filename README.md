# Sistema-Bancário-Dio

**Sistema bancário em linha de comando com Python**

#### Ferramentas Utilizadas ####

**rich-click**

Para uma melhor experiência do usuário em linha de comando.

**ruff**

Este projeto utiliza o Ruff para linting e análise de código.
Ruff é uma ferramenta de linting rápida e eficiente para Python, que ajuda a garantir que o código siga as melhores práticas e padrões de codificação.
- [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


**Instalação**
#### Siga os passos abaixo para instalar e configurar o ambiente necessário para executar o projeto:

**Clone o Repositório**

`git clone
https://github.com/alexpaulo100/sistema-bancario-dio.git`

**Entre no diretorio**

`cd sistema-bancario-dio`

**Crie e Ative um Ambiente Virtual**

Crie um ambiente virtual para isolar as dependências do projeto:

`python -m venv .venv`

**Ative o ambiente virtual:**
- No Windows:
`.venv\Scripts\activate`
- No macOS/Linux:
`source .venv/bin/activate`

**Instale as Dependências**
- Com o ambiente virtual ativado, instale as dependências listadas no requirements.txt:

`pip install -r requirements.txt`

**Executar o Comando bcdio**
- Agora você pode executar o comando bcdio no terminal para interagir com o sistema bancário:
`bcdio --help`
- Isso exibirá a lista de comandos disponíveis e suas descrições.

## Descrição dos Comandos

- Para verificar todos os comandos disponíveis, digite `bcdio --help` no terminal.

- **Comando para depositar**: `bcdio depositar`
  - Exemplo: `bcdio depositar` - Deposito do usuário e na conta especificada.

- **Comando para exibir extrato**: `bcdio extrato`
  - Solicita CPF e número da conta para mostrar o saldo e movimentações.

- **Comando para sacar**: `bcdio sacar`
  - Exemplo: `bcdio sacar` - Realiza um saque do usuário e da conta especificada.

- **Comando para criar usuário**: `bcdio criar_usuario`
  - Solicita os detalhes do usuário e cria um novo usuário no sistema.

- **Comando para criar conta**: `bcdio criar_conta`
  - Solicita o CPF do usuário e cria uma nova conta associada a esse CPF.

- **Comando para excluir usuário**: `bcdio excluir_usuario`
  - Solicita o CPF do usuário e exclui o usuário e suas contas associadas.

- **Comando para excluir conta**: `bcdio excluir_conta`
  - Solicita o CPF e número da conta e exclui a conta se não houver saldo.

- **Comando para sair**: `bcdio sair`

## [0.1.1] - 2024-09-11

### Adicionado
- **Novas Funcionalidades**:
  - Criar conta
  - Criar usuário
  - Excluir usuário
  - Excluir conta
- **Persistência de Dados**: Implementada persistência usando o banco de dados SQLite.
- **Depósito Interativo**: Implementado o comando de depósito com entrada interativa para CPF e número da conta.





---

**Autor**: Alex Silva
[LinkedIn](https://www.linkedin.com/in/alexpaulo100/)

**version=[0.1.0]**

![Sistema Bancário](https://github.com/user-attachments/assets/ebd0a1b6-ad6a-453d-91fa-b8ef12dabe56)

**version=[0.1.1]**

![bcdio-version-0 1 1](https://github.com/user-attachments/assets/264e4c4f-0501-43be-94b1-c807b3b3b961)
