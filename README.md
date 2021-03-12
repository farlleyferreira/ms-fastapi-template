# :construction: [WIP] Microservices Fastapi Template :construction:

### Resumo

> <p style="text-align: justify"> 
> Este projeto foi construído como resultado de um aprofundamento dos estudos discutidos no blog 
> <a href="https://farlley.com">farlley.com</a> com foco maior na arquitetura <i><b>Domain Driven Design (DDD)</b></i>. 
> Neste trabalho você encontrará um template simples para criação de microsserviços, bem como um caso de uso (que ainda 
> será implementado de acordo com o Roadmap que se encontra neste mesmo documento) aplicando as torias e estudos apresentados 
> nos livros <i><b>Implementando Domain-Driven Design - Vaughn Vernon</b></i>, <i><b>Domain-Driven Design: Atacando as 
> Complexidades no Coração do Software - Eric Evans</b></i>, e <i><b>Building Microservices: Designing Fine-Grained Systems
>  - Sam Newman</b></i>, a bibliografia consultada será adicionada ao final deste documento em acordo com o roadmap da aplicação. 
> O template foi escrito para a linguagem python em sua versão 3.9.0, utilizando o framework <a href="https://fastapi.tiangolo.com/">
> FastApi</a>. Para a camada de testes utilizamos a biblioteca <a href="https://docs.pytest.org/en/stable/">PyTest</a>. Nossa aplicação faz 
> ainda integração com os seguintes serviços: 
> </p>
>
> <ul>
> <li> Mongo DB </li>
> <li> Elasticsearch </li>
> <li> Elastic APM </li>
> <li> Rabbit MQ </li>
> <li> Redis </li>
> </ul>
>
> <p style="text-align: justify">
> Ao longo do desenvolvimento do projeto, outras integrações poderão ser adicionadas, desde que, sejam feitas respeitando as diretrizes
> e arquitetura adotadas neste projeto base, com a finalidade de manter a integridade do mesmo. Todos os itens pertinentes a arquitetura
> e estrutura do projeto serão extensivamente discutidos nos itens que estão contidos neste mesmo documento. Sinta-se a vontade para
> contribuir com o mesmo.
> </p>

### Roadmap

</br>

> <ol>
> <li> Criação e ajuste das documentações de utilização e design. </li>
> <li> Criação do manual de requisitos para PR. </li>
> <li> Implantação de caso de uso. </li>
> <li> Ajuste e melhoria da arquitetura. </li>
> <li> Criação da bibliografia de referencia do projeto</li>
> </ol>

### Setup

> <p style="text-align: justify">
> Este projeto está estruturado em docker, utilizamos o <i><b>docker-compose</b></i> para montar o processo de startup dos serviços os
> quais a aplicação necessita para rodar. A configuração desses serviços bem como sua estrutura, serão melhor discutidos na seção 
> <a href="#patterns">Estrutura e padrões adotados</a>.
> </p>
>
> <i><b>Para rodar todas as aplicações via docker-compose.</b></i>
>
> <p>
>   <ol>
>    <li> Realize o clone desta aplicação para seu diretório de projetos</li>
>    <li> Dentro deste diretório será possivel verificar a criação da pasta: <i><b>ms-fastapi-template</b></i></li>
>    <li> Abra o diretório <i><b>ms-fastapi-template/api/project/infrastructure/environments</b></i></li>
>    <li> Neeste diretório você encontrará o arquivo <i><b>config.yaml d</b></i></li>
>    <li> Para cada serviço contido neste arquivo, altere o host: localhost para o nome do serviço desejado (nome do serviço no arquivo docker-compose).</li>
>   </ol>
>   <p style="text-align: justify">
>   <i><b>Obs</b></i>:
>   <a>
>    Neste arquivo estão as configurações de ambiente do nosso projeto e não, eu optei por não criar um arquivo .ENV por 
>    motivos que discutiremos melhor na seção <a href="#patterns">Estrutura e padrões adotados</a>.
>    </a>
>   </p>
> </p>
>
> <i><b>Trecho Original</b></i>:
>
> ```yaml
> rabbitmq:
>   host: "localhost"
>   port: 5672
>   username: "farlley_ferreira"
>   password: "mstemplate123"
> ```
>
> <i><b>Trecho Ajustado</b></i>:
>
> ```yaml
> rabbitmq:
>   host: "rabbit"
>   port: 5672
>   username: "farlley_ferreira"
>   password: "mstemplate123"
> ```
>
> <p>
>   <ol start="6">
>    <li> Após ajustar o arquivo para todos os serviços desejados, o usuário deverá rodar o comando:</li>
>   </ol>
> </p>
>
> ```bash
> docker-compose up
> ```
>
> <i> &nbsp;&nbsp;&nbsp; Ou em alguns casos </i>
>
> ```bash
> sudo docker-compose up
> ```
>
> <p>
> Se os ajustes tiverem sido feitos de forma adequada a aplicação irá iniciar no endereço <i><b>http://localhost:5000</b></i>:
> e sua documentação via swagger estará ativa via <i><b>http://localhost:5000/docs</b></i>
> </p>
> </br>
>
> <i><b>Para rodar somente o projeto ms-template localmente e o restante via docker-compose.</b></i>
>
> <p>
>   <ol>
>    <li> Realize o clone desta aplicação para seu diretório de projetos</li>
>    <li> Certifique-se de possuir o make instalado em seu OS</li>
>    <li> Crie um ambiente virtual utilizando gerenciador de sua preferência > (pyenv, virtualenv, anaconda...).</li>
>    <li> Dentro deste diretório será possivel verificar a criação da pasta: <i><b>ms-fastapi-template</b></i></li>
>    <li> No arqruivo docker-compose.yml, dentro deste diretório deverá ser comentado o item referente ao serviço da com tag: <i><b>web</b></i>.</li>
>    <li> Aponte seu terminal para o diretório api, dessa mesma aplicação e execute o comando:</b></i></li>
>   </ol>
> </p>
>
> ```bash
> make install-requeriments
> ```
>
> <i> &nbsp;&nbsp;&nbsp; ou caso não possua o make, poderá rodar o comando:</i>
>
> ```bash
> pip install -r requirements.txt
> ```
>
> <p>
>   <ol start="7">
>    <li> Se todos os pacotes foram instalados corretamente você poderá executar:</li>
>   </ol>
> </p>
>
> ```bash
> docker-compose up
> ```
>
> <i> &nbsp;&nbsp;&nbsp; Ou em alguns casos </i>
>
> ```bash
> sudo docker-compose up
> ```
>
> <p>
>   <ol start="8">
>    <li> Com todos os procedimentos tendo sido executados corretamente você poderá executar:</li>
>   </ol>
> </p>
>
> ```bash
> make run-aplication
> ```
>
> <i> &nbsp;&nbsp;&nbsp; ou caso não possua o make, poderá rodar o comando:</i>
>
> ```bash
> python setup.py
> ```
>
> <p>
> Nossa aplicação estará então disponivel para ser utilizada no endereço <i><b>http://localhost:5000</b></i>:
> e sua documentação via swagger estará ativa via <i><b>http://localhost:5000/docs</b></i>
> </p>
>
> <i><b>Para rodar a suite de testes:</b></i>
>
> <p>
>   <ol start="9">
>    <li> Com todos os procedimentos anteriores tendo sido executados corretamente:</li>
>   </ol>
> </p>
>
> ```bash
> make test-coverage
> ```
>
> <i> &nbsp;&nbsp;&nbsp; ou caso não possua o make, poderá rodar o comando:</i>
>
> ```bash
> pytest --cov-report term-missing --cov=project/
> ```
>
> Ou ainda, de acordo com a prferencia do desenvolvedor, os testes poderão ser executados via plugin da sua IDE
> ou editor de códigos preferida, recomendo a [Python Test Explorer for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter) ou ainda [Test Explorer UI](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer). Já para os testes do tipo BDD que utilizaremos nos casos de uso, recomendo [Pytest BDD](https://marketplace.visualstudio.com/items?itemName=vtenentes.bdd)

## <a id="patterns">Estrutura e padrões adotados</a> :european_castle:

> ### Estrutura: :mag:
>
> ```file
>
>   - ms-fastapi-template
>   |   - api
>   |   |   - project
>   |   |   |   - helpers
>   |   |   |   - infrastructure
>   |   |   |   |   - constants
>   |   |   |   |   - drivers
>   |   |   |   |   - environments
>   |   |   |   |   - monitoring_layer
>   |   |   |   |   - open_api
>   |   |   |   |   - logs
>   |   |   |   - repositories
>   |   |   |   - resources
>   |   |   |   - routers.py
>   |   |   - tests
>   |   |   |   - helpers
>   |   |   |   - infrastructure
>   |   |   |   |   - constants
>   |   |   |   |   - drivers
>   |   |   |   |   - environments
>   |   |   |   |   - monitoring_layer
>   |   |   |   |   - open_api
>   |   |   |   |   - logs
>   |   |   |   - repositories
>   |   |   |   - resources
>   |   |   - .coveragerc
>   |   |   - dockerfile
>   |   |   - makefile
>   |   |   - requirements.txt
>   |   |   - setup.cfg
>   |   |   - setup.py
>   |   - worker
>   |   - volumes
>   |   - .gitignore
>   |   - .deepsource.toml
>   |   - .whitesource
>   |   - docker-compose.yml
>
> ```
>
> ### Padrões adotados: :chart_with_upwards_trend:
>
> #### Api :electric_plug:
>
> ```file
>
>   - project
>   |   - helpers
>   |   - infrastructure
>   |   |   - constants
>   |   |   - drivers
>   |   |   - environments
>   |   |   - monitoring_layer
>   |   |   - open_api
>   |   |   - logs
>   |   - repositories
>   |   - resources
>   |   - routers.py
>   - tests
>   - .coveragerc
>   - dockerfile
>   - makefile
>   - requirements.txt
>   - setup.cfg
>   - setup.py
>
> ```
>
> #### Workers :construction_worker:
>
> #### Tests :hammer:
>
> ```filee
>
>   - project
>   - tests
>   |   - helpers
>   |   - infrastructure
>   |   |   - constants
>   |   |   - drivers
>   |   |   - environments
>   |   |   - monitoring_layer
>   |   |   - open_api
>   |   |   - logs
>   |   - repositories
>   |   - resources
>   - .coveragerc
>   - dockerfile
>   - makefile
>   - requirements.txt
>   - setup.cfg
>   - setup.py
>
> ```
>
> #### Observações: :information_source:
>
> ### Bibliografia: :books:
