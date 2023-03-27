# Resolução do desafio da Refera 

Segue a resolução do desafio de Engenharia de dados da REFERA no qual foi criado um script em python com o objetivo de extrair e carregar o banco de dados.

Primeiramente foi feito todo o passo a passo de configuração do ambiente do linux/docker. Os bancos de dados foram configurados usando docker composer através do git clone.

 No **script.py** usa a biblioteca psycopg2 para estabelecer a conexão com os bancos de dados. Ele também define uma lista de tabelas que serão transferidas do banco de dados `transacional`(dvdrental) para o banco de dados `analytics´`.

PS: Tive dificuldades em carregar as tabelas que estão comentadas no código.

Adorei o desafio!!

# Seja bem vindo ao desafio de engenharia de dados da Refera!

⚠️⚠️ Não faça fork deste repositório!


O objetivo desse desafio é ser algo rápido para exemplificar alguns desafios do dia a dia de quem trabalha com dados. Queremos com esse desafio avaliar o seu conhecimento básico em programação, banco de dados e entender mais quais as boas práticas você segue para construção de código.


## O desafio

Pensando em não sobrecarregar nosso banco de dados transacional, precisamos ter um ambiente separado para analisar nossos dados sem grandes problemas. Assim, escreva um código local que faça uma extração total de todas as tabelas do banco de dados `transactional` e as carregue para o banco de dados `analytics`.

O arquivo [docker-compose.yml](docker-compose.yml) ativa containers com os bancos de dados `transactional` e `analytics`.

![Infra dos banco de dados](fluxo.png)

Diferenciais na implementação:
- script rodando dentro do docker

## Configuração do Ambiente

Os banco de dados podem ser configurados usando o docker compose. Você pode instalá-lo seguindo as instruções em https://docs.docker.com/compose/install/.

Clone o repositório:


```bash
git clone https://github.com/Refera-Tech/refera-data-engineer-short-challenge
```

Com o docker compose instalado, basta executar:

```bash
cd refera-data-engineer-short-challenge
docker-compose up
```

## Entrega

Subir os códigos em um repositório seu público no Github e enviar por email.

⚠️⚠️ Não faça fork deste repositório!

## Observações

- Escolha a linguagem de programação que quiser, mas evite ambientes complexos.
- Use bibliotecas de código aberto e escreva seu próprio código.
- É importante lembrar que precisaremos executar seu código.

## Links Úteis

- [Transactional vs. Analytical Workloads](https://www.youtube.com/watch?v=ivSPZB6zUKY)
- [Docker Docs](https://docs.docker.com/)
- [Docker em 22 minutos - teoria e prática](https://www.youtube.com/watch?v=Kzcz-EVKBEQ)
- [Docker Compose na prática](https://www.youtube.com/watch?v=HxPz3eLnXZk)
