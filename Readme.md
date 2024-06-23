## Stack

A Aplicação foi desenvolvida utilizando o `Django`. Para salvar os dados está sendo utilizado o `postgres`, por meio do `docker`.

## Execução
Primeiro você precisa do `pyenv` e do `poetry`, para gerenciar o `python` e o ambiente virtual, respectivamente. Caso não tenha instalado, aqui está uma [documentação](https://github.com/nayannanara/poetry-documentation) para te ajudar.

Para subir o banco de dados, caso não tenha o [docker](https://docs.docker.com/engine/install/ubuntu/) e o [docker-compose](https://docs.docker.com/compose/install/linux/) instalado, faça a instalação e logo em seguida, execute:

```bash
docker-compose up -d
```

Para aplicar as migrações, execute:
```bash
task migrate
```
 
Para subir a aplição, execute:
```bash
task run
```

Em seguida, para visualizar abra seu navegador no endereço: http://127.0.0.1:8000/
