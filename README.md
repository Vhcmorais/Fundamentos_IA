# 🧠 Formação - "Fundamentos do Mundo da Inteligência Artificial - ALURA"


🧑🏽‍💻 Este repositório hospeda meus documentos de todo o desenvolvimento na formação "Fundamentos do mundo da Inteligência Artificial" pela plataforma Alura.

---

## 💡 Sobre o Projeto

Este repositório contém os materiais e códigos desenvolvidos ao longo da formação em Inteligência Artificial da Alura. A formação aborda os principais fundamentos da IA com foco prático em Python,
incluindo aprendizado supervisionado, não supervisionado, redes neurais, NLP (Processamento de Linguagem Natural) e ferramentas como Scikit-learn e TensorFlow.

Durante a formação, diversos temas foram introduzidos e praticados por meio de exercícios e desafios. Ao final, foi desenvolvido um projeto prático, com o objetivo de aplicar 
os conceitos estudados e construir uma Inteligência Artificial funcional, explorando técnicas como aprendizado supervisionado, redes neurais, processamento de linguagem 
natural (NLP), entre outros.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11
- Visual Studio Code
- Google Colab
- Alura (plataforma de ensino)

## 📚 Bibliotecas

- Pandas - Manipulação e análise de dados
- NumPy - Operações matemáticas e vetoriais
- Matplotlib - Visualização de dados
- Scikit-learn - Algoritmos de Machine Learning

---

## 📂 Estrutura do Repositório

- `/final_project/`: Arquivos de código do projeto final desenvolvido
- `/fundamentos_IA/`: Arquivos de código de atividades propostas durante o curso de fundamentos da inteligência artificial
- `/machine_learning/`: Arquivos de código de atividades propostas durante o curso de Machine Learning
- `README.md`: Este arquivo
  
---

## 💭 Planejamento de Projeto

Ao concluir a formação "Fundamentos do Mundo da Inteligência Artificial" da Alura, desenvolvi um agente inteligente utilizando a abordagem de aprendizado supervisionado, aplicando na prática os principais conceitos estudados ao longo do curso.

A ideia central do projeto foi criar uma Inteligência Artificial capaz de receber uma frase como input e identificar o sentimento humano associado a ela, classificando-o entre alegria, tristeza, raiva ou ansiedade. O modelo foi treinado com um conjunto de dados rotulado, desenvolvido manualmente para o projeto, utilizando técnicas de Processamento de Linguagem Natural (NLP) e classificação de texto.

---

## 🧑🏽‍💻 Criação do DataSet "Emoções"

O ponto de partida do projeto foi a criação de um dataset personalizado, nomeado "Emoções", composto por frases rotuladas de acordo com a emoção expressa: alegria, tristeza, raiva ou ansiedade.

Cada entrada do conjunto de dados representa uma frase associada a uma dessas emoções, permitindo o treinamento supervisionado do modelo. A construção manual do dataset foi essencial para garantir exemplos realistas e relevantes, promovendo um aprendizado mais eficaz por parte da IA.

Este dataset foi utilizado como base para as etapas de pré-processamento, vetorização e treinamento do classificador.

## 📝 Exemplo de dados

| Frase                                 | Emoção    |
| ------------------------------------- | --------- |
| Hoje o dia está incrível!             | alegria   |
| Não aguento mais essa situação.       | raiva     |
| Me sinto tão sozinho e perdido.       | tristeza  |
| Tenho uma prova amanhã e estou tenso. | ansiedade |

🔗 

---

## 🫵 Desafio 

A apresentação do projeto contou com 3 desafios propostos pelo professor orientador para avaliação do sistema, foram eles: 

1) Inserir uma view de tabela temporária com JOINs;
2) Inserir triggers para controle da operação UPDATE em qualquer tabela;
3) Inserir um Stored Procedure que receba uma inserção em uma tabela e retorne o ID do dado inserido.

Cada desafio foi resolvido com os seguintes códigos:

1) Inserir uma view de tabela temporária com JOINs;

```
SELECT
    ag.data_hora,
    t.nome AS tutor,
    f.nome AS profissional,
    ag.status
FROM sistema.agenda ag
JOIN sistema.tutores t ON ag.id_tutor = t.id_tutor
JOIN sistema.funcionarios f ON ag.id_funcionario = f.id_funcionario
ORDER BY ag.data_hora;
```
2) Inserir triggers para controle da operação UPDATE em qualquer tabela;
```
CREATE TABLE sistema.dia_consultas (
data_hr	VARCHAR		NOT NULL,
consultas_qt	NUMERIC);
CREATE TABLE sistema.dia_consulta_controle(
operacao	CHAR 		NOT NULL,
usuario	    VARCHAR     NOT NULL,
dt_hr	    TIMESTAMP	NOT NULL,
data_hr	    VARCHAR	 	NOT NULL,
consultas_qt     NUMERIC);
CREATE OR REPLACE FUNCTION sistema.fn_dia_consulta_controle()
RETURNS trigger AS
$$
	BEGIN
    	IF(tg_op = 'UPDATE') THEN
           	INSERT INTO sistema.dia_consulta_controle
            SELECT 'A', user, now(),NEW.*;
            RETURN NEW;
        END IF;
        RETURN NULL;                   
    END
$$
LANGUAGE plpgsql;
CREATE TRIGGER tg_controle_diaconsulta
AFTER INSERT OR UPDATE OR DELETE ON sistema.dia_consultas
FOR EACH ROW EXECUTE PROCEDURE sistema.fn_dia_consulta_controle();

select * from sistema.dia_consultas;

select * from sistema.dia_consulta_controle;

insert into sistema.dia_consultas(data_hr, consultas_qt)
values  ('08/05/2025', 5),
		('15/05/2025', 3),
		('18/05/2025', 7),
		('25/05/2025', 3),
		('31/05/2025', 15);
		
update sistema.dia_consultas
set data_hr = '10/05/2025' where consultas_qt = 5;

update sistema.dia_consultas
set data_hr = '01/06/25' where consultas_qt = 15;
```

3) Inserir um Stored Procedure que receba uma inserção em uma tabela e retorne o ID do dado inserido:
```
CREATE OR REPLACE FUNCTION sistema.fn_return_insertedid(
    p_nome VARCHAR,
    p_telefone VARCHAR,
    p_email VARCHAR,
    p_endereco VARCHAR
) RETURNS INTEGER AS
$$
DECLARE 
    t_id sistema.tutores.id_tutor%TYPE;
BEGIN
    INSERT INTO sistema.tutores (nome, telefone, email, endereco)
    VALUES (p_nome, p_telefone, p_email, p_endereco)
    RETURNING id_tutor INTO t_id;

    RETURN t_id;
END;
$$
LANGUAGE plpgsql;


SELECT sistema.fn_return_insertedid(
    'Rafinha Santos',
    '(11) 98765-4321',
    'rafinha@logomail.com',
    'Rua das Flores, 123'
);


SELECT sistema.fn_return_insertedid(
    'Luca Braga',
    '(11)1234-2314',
    'lucabraga@gmail.com',
    'Rua das Acacias, 4356'
);

SELECT sistema.fn_return_insertedid(
    'Rony',
    '(11)43414',
    'rony@gmail.com',
    'Rua das Acacias, 213'
);
```
---

## 📌 Conclusão

Este projeto me proporcionou uma experiência prática essencial na modelagem, criação e manipulação de bancos de dados relacionais. A simulação de um sistema real de um Hospital Veterinário exigiu atenção a detalhes como integridade referencial, organização de dados e clareza na consulta das informações. Tenho como planejamento e objetivo futuro de implementar uma interface gráfica para esse projeto :)   

<p align="center">
  <img src="assets/dog.png" width="100" height="100" style="border-radius: 50%;"/>
</p>

---

## 👤 Sobre o Autor

Desenvolvido por **Vitor Henrique Carvalho de Morais**, estudante de Engenharia da Computação na **Universidade Federal de Uberlândia (UFU)**.

- 💼 [Portfólio](https://vhcdev.netlify.app/)
- 🐙 [GitHub](https://github.com/Vhcmorais)
- ✉️ vhcmdev@gmail.com

Sinta-se à vontade para explorar o repositório, deixar sugestões ou entrar em contato! 🚀
