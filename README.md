# Forest_Mobile
Projeto final da disciplina de Programação Mobile da faculdade de Análise e Desenvolvimento de Sistemas


- python -m venv venv
- source venv/bin/activate   # linux / mac
- venv\Scripts\activate      # windows
- pip install -r requirements.txt
----------

- Rodar
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
----------

- Deploy no Railway (resumo)
1 - Push do repositório no GitHub.
2 - No Railway: New Project → Deploy from GitHub → selecione repo.
3 - Em Variables, adicione:
 - - MONGO_URL = <sua string do MongoDB Atlas>
4 - Command:
uvicorn main:app --host 0.0.0.0 --port $PORT
