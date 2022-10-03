import sqlite3

class Data_base:
    
    def __init__(self, name = 'system.db') -> None:   
        self.name = name
        
    def connect(self):
        self.connection = sqlite3.connect(self.name)
    
    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    
    def create_table_turmas(self):

        cursor = self.connection.cursor()
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Alunos(
                     
                        NOME TEXT,
                        SERIE TEXT,
                        NASCIMENTO TEXT,
                        NATURALIDADE TEXT,
                        NACIONALIDADE TEXT,
                        TELEFONE TEXT,
                        PAI TEXT,
                        MAE TEXT,
                        CPF TEXT,
                        RG TEXT,
                        CEP TEXT,
                        ENDERECO TEXT,
                        BAIRRO TEXT,
                        CIDADE TEXT,
                        PROFESSORA TEXT,
                        TURMA TEXT,
                        EMAIL TEXT,
                        ALERGIA TEXT,
                
                        PRIMARY KEY(CPF)
                
               
                 )  
                    ''')
    
    def register_alunos(self, fullDataSet):
        
        campos_tabela = ('NOME','SERIE','NASCIMENTO','NATURALIDADE','NACIONALIDADE','TELEFONE','PAI','MAE',
                         'CPF','RG','CEP','ENDERECO','BAIRRO','CIDADE','PROFESSORA','TURMA','EMAIL','ALERGIA')
        
        qntd = ('?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?')
        cursor = self.connection.cursor()
        
        try:
            cursor.execute(f'''INSERT INTO Alunos {campos_tabela}
            VALUES({qntd})''',fullDataSet)
            self.connection.commit()
            return('OK')
        except:
            return 'Erro'
        
    def select_all_alunos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM Alunos ORDER BY NOME')
            alunos = cursor.fetchall()
            return alunos
        except:
            pass
        
    def delete_aluno(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM alunos WHERE CPF = '{id}' ")
            self.connection.commit()
            return 'Cadastro de aluno excluído com sucesso!'
    
        except:
            return 'Erro ao excluir registro!'

    def update_turmas(self, fullDataSet):
    
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Alunos set
            CPF '{fullDataSet[0]}',
            NOME '{fullDataSet[1]}',
            SERIE '{fullDataSet[2]}',
            NASCIMENTO '{fullDataSet[3]}',
            NATURALIDADE '{fullDataSet[4]}',
            NACIONALIDADE '{fullDataSet[5]}',
            TELEFONE '{fullDataSet[6]}',
            PAI '{fullDataSet[7]}',
            MAE '{fullDataSet[8]}',
            RG '{fullDataSet[9]}',
            CEP '{fullDataSet[10]}',
            ENDERECO '{fullDataSet[11]}',
            BAIRRO '{fullDataSet[12]}',
            CIDADE '{fullDataSet[13]}',
            PROFESSORA '{fullDataSet[14]}',
            TURMA '{fullDataSet[15]}',
            EMAIL '{fullDataSet[16]}',
            ALERGIA '{fullDataSet[17]}',
    
            WHERE CPF = {fullDataSet[0]} """)

        self.connection.commit()


