# classificacoes-futebol

Um web app desenvolvido em Django e integrado com a [API-Football](https://www.api-football.com/) que exibe as classificações das principais ligas de futebol do mundo.

## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:

- Python (versão recomendada: 3.7 ou superior)
- Django (instalado automaticamente ao seguir as instruções abaixo)
- Outras dependências listadas no arquivo `requirements.txt`

Observações: Você pode rodar este projeto de duas maneiras, em um Ambiente virtual (venv) ou em um Docker Container, portanto atente-se a qual o modo que deseja rodar este projeto e siga as intruções de acordo com os mesmos.


## Instalação das Dependências

### Ambiente Virtual
Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:
```bash
pip install -r requirements.txt
```

## Configuração de API_KEY

No arquivo views.py na pasta "ratings" do projeto, defina a API_KEY, você pode obte-la acessando [https://www.api-football.com](https://www.api-football.com/) e criando uma conta.
```bash
URL = 'https://v3.football.api-sports.io/standings'
API_KEY = 'SUA API_KEY'
```

## Docker Container
Localizado no diretório do projeto, abra o terminal e crie a imagem da aplicação:
```bash
docker build -t ratings-app-image .
```
Rode o container com a imagem da aplicação:
```bash
docker run --name ratings-app-container -p 8000:8000 ratings-app-image
```
Utilize a porta que desejar, no exemplo usado acima será utilizado um espelhamento de porta na porta 8000.

## Rodando o projeto em Ambiente Virtual

Após instalar as dependências, se não estiver rodando em um Docker Container aplique as migrations no banco de dados com o comando:
```bash
python manage.py migrate
```

Agora o projeto jã pode ser inicializado com o comando:
```bash
python manage.py runserver
```

Após isso, o sistema estará pronto para ser acessado em:
[http://localhost:8000](http://localhost:8000)
