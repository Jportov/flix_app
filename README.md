# Flix App

Flix App é uma aplicação web desenvolvida com **Streamlit** para gerenciar dados de filmes, incluindo **gêneros**, **atores/atrizes** e **filmes**. O projeto também inclui a **API de filmes**, totalmente desenvolvida pelo autor, que fornece os dados consumidos pela aplicação. As tabelas interativas utilizam **AgGrid** e permitem cadastro e edição de itens em tempo real.

## Funcionalidades

- Listagem de gêneros, atores e filmes em tabelas interativas (AgGrid).
- Cadastro de novos itens via formulário.
- Edição de itens existentes.
- Atualização dinâmica das tabelas após operações de cadastro e edição.
- API de filmes própria, desenvolvida para fornecer os dados da aplicação.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

flix_app/
├── actors/ # Módulo de atores
├── api/ # API de filmes desenvolvida pelo autor
├── genres/ # Módulo de gêneros
├── home/ # Página inicial
├── login/ # Módulo de login
├── movies/ # Módulo de filmes
├── reviews/ # Módulo de avaliações
├── app.py # Arquivo principal da aplicação
├── requirements.txt # Dependências do projeto
└── README.md # Este arquivo

perl
Copiar
Editar

## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:

- Python (versão recomendada: 3.7 ou superior)
- Dependências listadas no arquivo `requirements.txt`  

## Instalação das Dependências

Com o ambiente virtual ativado, instale as dependências do projeto usando:

```bash
pip install -r requirements.txt
Rodar o Projeto
Após instalar as dependências, execute o aplicativo com:

bash
Copiar
Editar
streamlit run app.py
O aplicativo estará disponível em http://localhost:8501 no navegador.

Como Funciona
Ao abrir o app, você encontra a página inicial com opções de Gêneros, Atores/Atrizes e Filmes.

Cada página carrega uma tabela interativa usando AgGrid.

É possível cadastrar novos itens usando formulários específicos.

Após cadastro ou edição de qualquer item, a tabela é atualizada dinamicamente, garantindo que os dados estejam sempre sincronizados com a API.

Toda a API de filmes foi criada para suportar essas operações e fornecer os dados da aplicação.

Contribuições
Contribuições são bem-vindas! Para contribuir:

Faça um fork deste repositório.

Crie uma nova branch (git checkout -b feature/nova-feature).

Faça suas alterações e commit (git commit -am 'Adiciona nova feature').

Envie para o repositório remoto (git push origin feature/nova-feature).

Abra um pull request.
