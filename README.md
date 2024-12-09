# Запустить проект
---------------------------
## Запустить Проект

```sh
cd lab2web-main
docker volume create pgdata
docker-compose up --build
docker cp ./frontend/backup <container_id_or_name>:/var/lib/postgresql/data
```

## Автор:
Нгуен Кхань Ли - N3347
