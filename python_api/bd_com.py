import pymysql.cursors
import os,time
from dotenv import load_dotenv

load_dotenv()

def conectar_bd():
    for i in range(1,6):
        try:
            conexao = pymysql.connect(host="mysql-api",
                                        user=os.getenv("USER"),
                                        password=os.getenv("PASSWORD"),
                                        database="python_api",
                                        port=3306,
                                        connect_timeout=8,
                                        cursorclass=pymysql.cursors.DictCursor)
            
            return conexao
        except pymysql.OperationalError as e:
            time.sleep(10)

    return None


def ver_tarefa_bd(id_api):
    conexao = conectar_bd()
    with conexao.cursor() as cursor:
        sql = "SELECT * FROM tarefas WHERE id = %s"
        cursor.execute(sql, (id_api))
        result = cursor.fetchone()
        conexao.close()
        
        return result

def criar_tarefa_bd(titulo_api, descricao_api, data_api):
    conexao = conectar_bd()
    with conexao.cursor() as cursor:
        sql = "INSERT INTO tarefas (titulo, descricao, data) VALUES (%s, %s, %s);"
        cursor.execute(sql, (titulo_api, descricao_api, data_api))

        conexao.commit()

    conexao.close()

def atualizar_tarefa_bd(id_api, titulo_api, descricao_api, data_api):
    conexao = conectar_bd()
    with conexao.cursor() as cursor:
            sql = "UPDATE tarefas SET titulo = %s, descricao = %s, data = %s WHERE id = %s;"
            cursor.execute(sql, (titulo_api, descricao_api, data_api, id_api))

            conexao.commit()

    conexao.close()

def apagar_tarefa_bd(id_api):
    conexao = conectar_bd()
    with conexao.cursor() as cursor:
            sql = "DELETE FROM tarefas WHERE id = %s;"
            cursor.execute(sql, (id_api))

            conexao.commit()

    conexao.close()

def criar_tabelas():
    conexao = conectar_bd()
    with conexao.cursor() as cursor:
        sql = "SELECT table_name FROM information_schema.tables WHERE table_name = %s AND table_schema = %s;"
        cursor.execute(sql, ("tarefas", "python_api"))
        result = cursor.fetchone()
        
        if result == None:
            sql = "CREATE TABLE tarefas (id INT AUTO_INCREMENT PRIMARY KEY, titulo VARCHAR (30), descricao TEXT, data TEXT);"
            cursor.execute(sql)
            conexao.commit()

        else:
            pass

    conexao.close()