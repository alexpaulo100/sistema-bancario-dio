# Sistema-Bancário-Dio

**Sistema bancário em linha de comando com Python**

Utilizado **rich-click** para uma melhor experiência do usuário em linha de comando.
- [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


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

![2-ezgif com-animated-gif-maker](https://github.com/user-attachments/assets/a37aad63-053f-4d2b-9b15-ff3595474fcc)

