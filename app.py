from flask import Flask, request, render_template, make_response, jsonify, redirect, url_for, session
from flask_mysqldb import MySQL
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'bancolistatarefas'

mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM ListaTarefas")
    data = cur.fetchall()
    tarefas = []

    for row in data:
        horario_tarefa = datetime.strptime(str(row[3]), '%H:%M:%S').time()
        now = datetime.now().time()

        if now > horario_tarefa:
            statuscor = 'atrasada'
            status = 'Atrasada'
        else:
            statuscor = 'emandamento'
            status = 'Em andamento'

        tarefa = {
            'id': row[0],
            'titulo': row[1],
            'descricao': row[2],
            'horario': row[3],
            'status': status,
            'statuscor': statuscor
        }

        tarefas.append(tarefa)

    cur.close()

    return render_template('index.html', tarefas=tarefas)
    

@app.route('/criar', methods=['GET','POST'])
def criar():
    tarefa_titulo = request.form['titulo']
    tarefa_horario = request.form['horario']
    tarefa_descricao = request.form['descricao']

    cur = mysql.connection.cursor()
    cur.execute(f'INSERT INTO ListaTarefas (titulo_tarefa, descricao_tarefa, horario_tarefa) VALUES ("{tarefa_titulo}","{tarefa_descricao}","{tarefa_horario}")')
    mysql.connection.commit()
    cur.close()
    
    return redirect('/')

@app.route('/editar', methods=['GET','POST'])
def atualizar():
    idTarefas = request.form['idTarefas']
    tarefa_titulo = request.form['tarefa_titulo']
    tarefa_horario = request.form['tarefa_horario']
    tarefa_descricao =  request.form['tarefa_descricao']

    cur = mysql.connection.cursor()
    cur.execute(f'UPDATE ListaTarefas SET descricao_tarefa = "{tarefa_descricao}", horario_tarefa = "{tarefa_horario}", titulo_tarefa = "{tarefa_titulo}" WHERE idTarefas = {idTarefas}')
    mysql.connection.commit()
    cur.close()
    
    return redirect('/')


@app.route('/deletar', methods=['GET','POST'])
def deletar_item():
    idTarefas = request.form['idTarefas']

    cur = mysql.connection.cursor()
    cur.execute(f'DELETE FROM ListaTarefas WHERE idTarefas = {idTarefas}')
    mysql.connection.commit()
    cur.close()

    return redirect('/')


if __name__ == '__main__':
    app.run()



