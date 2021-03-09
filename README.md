# :construction: [WIP] Microservices Fastapi Template :construction:

## Resumo

> Este projeto foi construído como resultado de um aprofundamento dos estudos discutidos no blog [farlley.com](https://farlley.com)
> com foco maior na arquitetura **_Domain Driven Design (DDD)_**. Neste trabalho você encontrará um template simples para criação de
> microsserviços, bem como um caso de uso (que ainda será implementado de acordo com o Roadmap que se encontra neste mesmo documento)
> aplicando as torias e estudos apresentados nos livros **_Implementando Domain-Driven Design - Vaughn Vernon_**,
> **_Domain-Driven Design: Atacando as Complexidades no Coração do Software - Eric Evans_**,
> e **_*Building Microservices: Designing Fine-Grained Systems - Sam Newman*_**, a bibliografia consultada será adicionada ao final
> deste documento em acordo com o roadmap da aplicação. O template foi escrito para a linguagem python em sua versão 3.9.0, utilizando
> o framework [FastApi](https://fastapi.tiangolo.com/). Para a camada de testes utilizamos a biblioteca [PyTest](https://docs.pytest.org/en/stable/).
> Nossa aplicação faz ainda integração com os seguintes serviços:
>
> <ul>
> <li> Mongo DB </li>
> <li> Elasticsearch </li>
> <li> Elastic APM </li>
> <li> Rabbit MQ </li>
> <li> Redis </li>
> </ul>
>
> Ao longo do desenvolvimento do projeto, outras integrações poderão ser adicionadas, desde que, sejam feitas respeitando as diretrizes
> e arquitetura adotadas neste projeto base, com a finalidade de manter a integridade do mesmo. Todos os itens pertinentes a arquitetura
> e estrutura do projeto serão extensivamente discutidos nos itens que estão contidos neste mesmo documento. Sinta-se a vontade para
> contribuir com o mesmo.

### Roadmap

> <ol>
> <li> Criação e ajuste das documentações de utilização e design. </li>
> <li> Criação do manual de requisitos para PR. </li>
> <li> Implantação de caso de uso. </li>
> <li> Ajuste e melhoria da arquitetura. </li>
> <li> Criação da bibliografia de referencia do projeto</li>
> </ol>

### How to

> Este é apenas um guia básico de utilização que será refatorado e ajustado posteriormente.
>
> #### Para rodar todas as aplicações via docker-compose.
>
> Realize o clone desta aplicação para a pasta de destino, abra o arquivo config.yaml do diretório **_./api/project/infrastructure/environments_**
> Para cada serviço contido neste arquivo, altere o host: localhost para o nome do serviço desejado (nome do serviço no arquivo docker-compose).
>
> </ul>

##### **_Original:_**

```
    rabbitmq:
        host: "localhost"
        port: 5672
        username: "farlley_ferreira"
        password: "mstemplate123"
```

##### **_Ajustado:_**

```
    rabbitmq:
        host: "rabbit"
        port: 5672
        username: "farlley_ferreira"
        password: "mstemplate123"
```

> Tendo executado o ajuste para todos os serviços desejados, o usuário deverá rodar o comando:
> </br></br> **_docker-compose up_** ou em alguns casos **_sudo docker-compose up_** </br></br>
> Se os ajustes tiverem sido feitos de forma adequada a aplicação irá iniciar no endereço **_http://localhost:5000_**
> e sua documentação via swagger estará ativa via **_http://localhost:5000/docs_**
>
> #### Para rodar somente o projeto ms-template localmente e o restante via docker-compose.
>
> Certifique-se de possuir o make instalado em seu OS. Crie um ambiente virtual utilizando gerenciador de sua preferencia
> (pyenv, virtualenv, anaconda...). Aponte seu terminal para o diretório api, dessa mesma aplicação e execute o comando:
> </br></br> **_make install-requeriments_** ou caso não possua o make **_pip install -r requirements.txt_** </br></br>
> Se todos os pacotes foram instalados corretamente você poderá executar:
> </br></br> **_make run-aplication_** ou caso não possua o make **_python setup.py_** </br></br>
> No arqruivo docker-compose.yml, deverá ser comentado o item referente ao serviço da aplicação web.
> Tendo sido executados os ajustes para todos os serviços desejados, o usuário deverá rodar o comando:
> </br></br> **_docker-compose up_** ou em alguns casos **_sudo docker-compose up_** </br></br>
> Se os ajustes tiverem sido feitos de forma adequada a aplicação irá iniciar no endereço **_http://localhost:5000_**
> e sua documentação via swagger estará ativa via **_http://localhost:5000/docs_**

## Padrões e estrutura adotados :european_castle:

#### Objetivo: :mag:

#### Metodologia: :chart_with_upwards_trend:

#### Observações: :books:

## Api :electric_plug:

#### Objetivo: :mag:

#### Metodologia: :chart_with_upwards_trend:

#### Observações: :books:

## Workers :construction_worker:

#### Objetivo: :mag:

#### Metodologia: :chart_with_upwards_trend:

#### Observações: :books:

## Tests :hammer:

#### Objetivo: :mag:

#### Metodologia: :chart_with_upwards_trend:

#### Observações: :books:
