# 📝 To-Do List em Python

Boas-vindas ao meu projeto de Lista de Tarefas! 👋

Este é um aplicativo simples e direto ao ponto que roda direto no terminal. Criei esse projeto para praticar lógica de programação, manipulação de arquivos e modularização de código utilizando Python. 

Apesar de rodar no terminal, a ideia principal aqui é resolver um problema real: **não esquecer o que precisa ser feito no dia a dia**, mantendo tudo salvo de forma segura.

## ✨ O que este projeto faz?

A aplicação possui um menu interativo onde você pode:
* **Adicionar novas tarefas:** Digite o que precisa ser feito e a tarefa vai para a sua lista.
* **Visualizar tarefas:** Um painel limpo que mostra tudo o que está pendente.
* **Remover tarefas:** Concluiu algo ou desistiu de uma ideia? É só deletar buscando pelo nome da tarefa.
* **Salvar automaticamente (Persistência de Dados):** Ninguém merece perder as anotações quando fecha o programa, né? Todas as tarefas são salvas automaticamente em um arquivo `minhas_tarefas.txt`, garantindo que elas continuem lá na próxima vez que você abrir o app.

## 🚀 Como rodar o projeto na sua máquina

Se você quiser testar o código, é super fácil. Você só vai precisar ter o **Python** instalado no seu computador.

1. Faça o clone deste repositório (ou baixe os arquivos).
2. Abra o terminal e navegue até a pasta do projeto (onde está o arquivo `main.py`).
3. Execute o arquivo principal com o comando:
   ```bash
   python main.py
   ```
4. O menu interativo vai aparecer e é só seguir as opções da tela!

## 🛠️ Tecnologias e Estrutura

* **Linguagem:** Python 3
* **Estrutura do Projeto:** * `main.py`: O coração do projeto, onde fica o menu e o loop de execução (`while` e `match case`).
  * `funcoes.py`: Onde a mágica acontece (as funções isoladas de adicionar, remover, listar, além de ler e salvar os dados).
  * `minhas_tarefas.txt`: O arquivo de texto que funciona como o "banco de dados" local do projeto.

---

### 👨‍💻 Sobre o Autor

Desenvolvido por **Davi Belo de Souza** *Desenvolvedor Back-end e estudante de Análise e Desenvolvimento de Sistemas (ADS).*

Sinta-se à vontade para dar uma olhada no código, testar e me enviar feedbacks!