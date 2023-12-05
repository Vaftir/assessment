import mysql.connector
import json

class ConectSQL:
    def __init__(self):
        self.conexao = None  
    def carregar_configuracoes(self, arquivo_config='config.json'):
        try:
            with open(arquivo_config, 'r') as arquivo:
                config = json.load(arquivo)
                db_config = config.get('banco_de_dados')
                if db_config:
                    host = db_config.get('host')
                    user = db_config.get('usuario')
                    password = db_config.get('senha')
                    database = db_config.get('database')
                    return host, user, password, database
                else:
                    print("Configurações de banco de dados não encontradas no arquivo.")
                    return None, None, None, None
        except FileNotFoundError:
            print(f"O arquivo de configuração '{arquivo_config}' não foi encontrado.")
            return None, None, None, None
    
    def conectar(self):
        host, user, password, database = self.carregar_configuracoes()
        try:
            if all([host, user, password, database]):
                self.conexao = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database,
                )
                if self.conexao.is_connected():
                    print(f"Conectado ao banco de dados {database}")
                    return self.conexao 
            else:
                print("Faltam informações de configuração.")
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None  


conexao_sql = ConectSQL()
conexao = conexao_sql.conectar()


