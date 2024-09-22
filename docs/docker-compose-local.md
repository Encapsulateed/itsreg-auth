Вот документация для указанного Docker Compose файла в нужном формате:

### Docker Compose File для сервисов `auth-db` и `auth-migrate`

#### Сервис `auth-db`
```yaml
auth-db:
  image: postgres:15.3-alpine3.18
  container_name: ir-auth-postgres
  command: postgres
  ports:
    - 30002:5432
  environment:
    POSTGRES_DB: test-db
    POSTGRES_USER: test-user
    POSTGRES_PASSWORD: test-pass
  healthcheck:
    test: [ "CMD-SHELL", "pg_isready -U test-user -d test-db" ]
    interval: 5s
    retries: 5
    start_period: 10s
    timeout: 10s
  networks:
    ir-web-auth:
      aliases:
        - db
```
- **Описание:**
  - Запускает контейнер с PostgreSQL версии 15.3 на базе Alpine 3.18.
  
- **Параметры:**
  - `container_name`: имя контейнера (`ir-auth-postgres`).
  - `ports`: пробрасывает порт 5432 контейнера на хост 30002.
  - `environment`: задает переменные окружения для создания базы данных:
    - `POSTGRES_DB`: имя базы данных (`test-db`).
    - `POSTGRES_USER`: имя пользователя (`test-user`).
    - `POSTGRES_PASSWORD`: пароль пользователя (`test-pass`).
  - `healthcheck`: проверяет состояние сервиса с помощью команды `pg_isready`, интервалом 5 секунд, с 5 попытками и таймаутом 10 секунд.
  - `networks`: подключает контейнер к сети `ir-web-auth` с псевдонимом `db`.

#### Сервис `auth-migrate`
```yaml
auth-migrate:
  image: migrate/migrate
  container_name: ir-auth-migrate
  volumes:
    - ../migrations:/migrations
  command: [ "-path", "/migrations", "-database", "postgres://test-user:test-pass@db:5432/test-db?sslmode=disable", "up" ]
  depends_on:
    auth-db:
      condition: service_healthy
  networks:
    - ir-web-auth
```
- **Описание:**
  - Запускает контейнер для выполнения миграций базы данных с использованием образа `migrate/migrate`.

- **Параметры:**
  - `container_name`: имя контейнера (`ir-auth-migrate`).
  - `volumes`: монтирует локальную папку с миграциями в контейнер.
  - `command`: команда для выполнения миграции:
    - `-path`: указывает путь к миграциям.
    - `-database`: строка подключения к базе данных.
  - `depends_on`: указывает, что сервис зависит от `auth-db` и будет ждать, пока он не станет здоровым.
  - `networks`: подключает контейнер к сети `ir-web-auth`.

#### Сеть `ir-web-auth`
```yaml
networks:
  ir-web-auth:
    driver: bridge
```
- **Описание:**
  - Определяет сеть с именем `ir-web-auth` с использованием драйвера `bridge`, который позволяет контейнерам обмениваться данными внутри одной сети.