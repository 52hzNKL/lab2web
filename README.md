﻿# Запустить проект
---------------------------

```sh
cd lab2web-main

Загрузить volume, содержащий данные
docker volume create pgdata
docker run --rm -v pgdata:/var/lib/postgresql/data -v ${PWD}:/backup ubuntu tar xvf /backup/pgdata.tar -C /

Запустить
docker-compose up --build
```

## Автор:
Нгуен Кхань Ли - N3347
