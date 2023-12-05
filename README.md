# Yago Faria - Prova SS Telemática - Fullstack

## Aplicação Cliente-Servidor UDP para Gerenciamento de Dados em Banco de Dados MySQL

Este repositório contém uma aplicação simples cliente-servidor UDP para gerenciamento de dados em um banco de dados MySQL. O servidor recebe mensagens UDP do cliente, realiza o parsing dos dados, insere as informações em uma tabela do banco de dados e responde ao cliente.



### Estrutura do Projeto

**Server:** Contém o código do servidor responsável por receber mensagens do cliente, processar os dados e interagir com o banco de dados.

- **UDPServer.py:** Implementação do servidor UDP.

- **config.json**: Arquivo de configuração com detalhes como IP, porta e tamanho do buffer.

**Client**: Contém o código do cliente, que simula o envio periódico de mensagens para o servidor.

- **UDPSimulator.py**: Implementação do cliente simulador.

**Package**: Pacote com módulos compartilhados.

- **ConectSQL.py:** Implementação da classe **'ConectSQL'** para gerenciar a conexão com o banco de dados.

### Requisitos

- Python 3.x

- Biblioteca **mysql-connector-python:** Instalável via:
  
      pip install mysql-connector-python 

### Configuração

1. Instale as dependências utilizando o comando:
   
       pip install -r requirements.txt`

2. Configure as informações do banco de dados no arquivo `config.json` no diretório `Server`
   
       {
        "localIP": "localhost",
        "localPort": 20001,
        "bufferSize": 1024,
        "banco_de_dados": {
            "host": "seu_host",
            "usuario": "seu_usuario",
            "senha": "sua_senha",
            "database": "seu_banco_de_dados"
        }
   
    }

Substitua `"seu_host"`, `"seu_usuario"`, `"sua_senha"` e `"seu_banco_de_dados"` pelos detalhes da sua configuração MySQL.

### Execução:

1. Inicie o servidor executando o arquivo `UDPServer.py` no diretório `Server`.

```bash
python UDPServer.py
```

2. Em um terminal separado, inicie o cliente simulador executando o arquivo `UDPSimulator.py` no diretório `Client`.

O cliente enviará mensagens simuladas periodicamente para o servidor, que processará e inserirá os dados no banco de dados MySQL.

### Encerramento

* Para interromper o servidor, pressione `Ctrl+C` no terminal em que o servidor está sendo executado.
* Para interromper o cliente simulador, pressione `Ctrl+C` no terminal em que o cliente simulador está sendo executado.
