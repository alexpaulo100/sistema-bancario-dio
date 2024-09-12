# Sistema-Bancário-Dio

**Sistema bancário em linha de comando com Python**

Utilizado **rich-click** para uma melhor experiência do usuário em linha de comando.

## Descrição dos Comandos

- Para verificar todos os comandos disponíveis, digite `bcdio --help` no terminal.

- **Comando para depositar**: `bcdio depositar [VALOR]`
  - Exemplo: `bcdio depositar 1000` - Depositando R$1000,00 na conta especificada.

- **Comando para exibir extrato**: `bcdio extrato`
  - Solicita CPF e número da conta para mostrar o saldo e movimentações.

- **Comando para sacar**: `bcdio sacar [VALOR]`
  - Exemplo: `bcdio sacar 1000` - Realiza um saque de R$1000,00 da conta especificada.

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
