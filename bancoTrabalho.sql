create database bancoListaTarefas;
use bancoListaTarefas;

create table tarefas(
	idTarefas INTEGER NOT NULL PRIMARY KEY auto_increment,
	tarefa_titulo VARCHAR(50) NOT NULL,
    tarefa_descricao VARCHAR(1000) NOT NULL,
    tarefa_horario TIME
);

drop table listatarefas;

insert into listatarefas(idTarefas,titulo_tarefa,descricao_tarefa,horario_tarefa) values(3, "Teste1", "Teste2", "12:12");

Select * from ListaTarefas;