# To-Do List em Python (CLI)

Aplicação de linha de comando (CLI) feita em Python para gerenciar tarefas, com persistência em arquivo texto.

O objetivo deste projeto é consolidar fundamentos da linguagem Python, como manipulação de arquivos, funções, controle de fluxo e tratamento básico de erros.

---

## ✅ Funcionalidades

- Adicionar tarefas (status inicial: `pendente`)
- Listar todas as tarefas
- Listar somente tarefas pendentes
- Listar somente tarefas concluídas
- Marcar tarefa como concluída pelo ID
- Interface via menu no terminal

As tarefas são armazenadas em `tarefas.txt` no formato: ID;DESCRICAO;STATUS

Exemplo:

1;Estudar Python;pendente
2;Criar README;concluida

---

## 🛠️ Tecnologias e Conceitos

- Python 3
- Funções e modularização (`main.py` + `funcoes.py`)
- Leitura e escrita em arquivos (`open`, `with`)
- Estruturas de repetição e condição (`while`, `for`, `if/elif`)
- Tratamento básico de exceções (`try/except`)
- Formatação de saída e alinhamento (f-strings)

---

## 📁 Estrutura do Projeto

todo_list_python/
├─ main.py
├─ funcoes.py
└─ tarefas.txt (criado automaticamente)


---

## ▶️ Como executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/todo-list-python-cli.git
```
2. Entre na pasta:

````bash
cd todo-list-python-cli
```
3.Execute:
```bash
python main.py
```

🚀 Melhorias futuras (ideias)

->Remover tarefa por ID

->Editar descrição de tarefa

->Persistência em JSON/CSV

->Filtros por palavras-chave

->Logs e histórico de alterações

👤 Autor

Cristovão Cavalcante


