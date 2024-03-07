# Descrição PythonFastAPI

Este projeto é uma aplicação web de página única (SPA) que permite realizar operações CRUD (Create, Read, Update, Delete) em uma aplicação de notas. A aplicação é construída utilizando as tecnologias FastAPI e Vue.js, fornecendo um backend em Python e um frontend interativo.

## Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

```
fastapi-vue
├── services
│   └── backend
│       ├── migrations
│       │   └── models
│       ├── Dockerfile
│       ├──requirements.txt
│       └── src
│           ├── main.py
│           ├── auth
│           │   ├── jwthandler.py
│           │   └── users.py
│           ├── crud
│           │   ├── notes.py
│           │   └── users.py
│           ├── database
│           │   ├── config.py
│           │   └── models.py
│           │   └── register.py
│           ├── routes
│           │   ├── notes.py
│           │   └── users.py
│           └── schemas
│               ├── notes.py
│               ├── token.py
│               └── users.py
│   └── frontend
│       ├── Dockerfile
│       ├── public
│       ├── src
│       │   ├── assets
│       │   ├── components
│       │   │   ├── HelloWord.vue
│       │   │   └── NavBar.vue
│       │   ├── router
│       │   │   ├── index.js
│       │   ├── store
│       │   │   ├── index.js
│       │   │   └── modules
│       │   │       ├── notes.js
│       │   │       └── users.js
│       │   ├── views
│       │   │   ├── AboutView.vue
│       │   │   ├── DashBoardView.vue
│       │   │   ├── EditNoteView.vue
│       │   │   ├── HomeView.vue
│       │   │   ├── LginView.vue
│       │   │   ├── NoteView.vue
│       │   │   ├── ProfileView.vue
│       │   │   └── RegisterView.vue
│       │   ├── main.js
│       │   └── App.vue
│       ├── babel.config.js
│       ├── package.json
│       └── vue.config.js
└── docker-compose.yml
```

### Backend

- **Dockerfile**: Arquivo de configuração para construção da imagem do Docker para o backend.
- **requirements.txt**: Arquivo que lista as dependências do backend.
- **src/main.py**: Arquivo principal do backend que contém as configurações e rotas da API.
- **src/models.py**: Arquivo que define os modelos de dados utilizados na aplicação.
- **src/routers**: Pasta que contém os arquivos de rotas da API.
- **src/schemas**: Pasta que contém os arquivos de esquemas de validação de dados.
- **src/tests**: Pasta que contém os arquivos de testes automatizados do backend.

### Frontend

- **Dockerfile**: Arquivo de configuração para construção da imagem do Docker para o frontend.
- **public**: Pasta que contém os arquivos públicos do frontend, como o arquivo HTML principal.
- **src/assets**: Pasta que contém os arquivos estáticos, como imagens e estilos.
- **src/components**: Pasta que contém os componentes reutilizáveis do frontend.
- **src/router**: Pasta que contém o arquivo de configuração do Vue Router.
- **src/services**: Pasta que contém os serviços de comunicação com o backend.
- **src/store**: Pasta que contém o arquivo de configuração do Vuex (gerenciador de estado).
- **src/views**: Pasta que contém as views (páginas) do frontend.
- **src/App.vue**: Arquivo principal do Vue.js que contém a estrutura base da aplicação.

## Tecnologias Utilizadas

- **FastAPI**: Framework web em Python para construção de APIs RESTful.
- **Vue.js**: Framework JavaScript para construção de interfaces de usuário interativas.
- **Docker**: Plataforma de virtualização que permite empacotar a aplicação em um ambiente isolado e portável.

## Funcionalidades

A aplicação possui as seguintes funcionalidades:

- Autenticação de usuários utilizando tokens JWT.
- Criação, leitura, atualização e exclusão de notas.
- Listagem das notas criadas por um usuário específico.
- Interface de usuário interativa e responsiva.
- Manutenção do estado da aplicação utilizando Vuex.

## Executando o Projeto

Para executar o projeto, siga as instruções abaixo:

1. Certifique-se de ter o Docker instalado em sua máquina.
2. Clone o repositório do projeto: `git clone https://github.com/seu-usuario/fastapi-vue.git`
3. Navegue até a pasta do projeto: `cd fastapi-vue`
4. Execute o comando `docker-compose up` para iniciar o projeto.
5. Acesse a aplicação no navegador através do endereço http://localhost:8080.

## Conclusão

O projeto "FastAPI + Vue + Docker" demonstra a integração entre o backend em FastAPI e o frontend em Vue.js para criar uma aplicação web completa. A documentação forneceuma visão geral da estrutura e funcionalidades do projeto, além de instruções para executá-lo. Para mais detalhes e informações, consulte a documentação completa no [repositório do projeto](https://github.com/abcvinicius/PythonFastAPI).
