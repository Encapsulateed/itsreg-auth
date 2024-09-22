Вот документация для кода в указанном формате:

### 1. Функция RunHTTPServer
```go
func RunHTTPServer(createHandler func(router chi.Router) http.Handler)
```
- Запускает HTTP-сервер, используя порт, указанный в переменной окружения `PORT`. Создает маршрутизатор и применяет заданные обработчики.

### 2. Функция RunHTTPServerOnAddr
```go
func RunHTTPServerOnAddr(addr string, createHandler func(router chi.Router) http.Handler)
```
- Запускает HTTP-сервер на указанном адресе. 
- **Параметры:**
  - `addr` — адрес, на котором будет запущен сервер.
  - `createHandler` — функция, создающая обработчик на основе маршрутизатора Chi.

### 3. Функция setMiddlewares
```go
func setMiddlewares(router *chi.Mux)
```
- Устанавливает набор промежуточных обработчиков для маршрутизатора:
  - Генерация уникального ID запроса.
  - Определение реального IP-адреса клиента.
  - Восстановление после паники.
  - Установка заголовков безопасности.
  - Отключение кэширования.

### 4. Функция addCorsMiddleware
```go
func addCorsMiddleware(router *chi.Mux)
```
- Устанавливает промежуточный обработчик CORS для маршрутизатора.
- Читает разрешенные источники из переменной окружения `CORS_ALLOWED_ORIGINS`.
- **Заголовки:**
  - `AllowedOrigins` — список разрешенных источников.
  - `AllowedMethods` — допустимые HTTP-методы.
  - `AllowedHeaders` — допустимые заголовки запроса.
  - `ExposedHeaders` — заголовки, доступные для клиента.
  - `AllowCredentials` — разрешить отправку учетных данных.
  - `MaxAge` — максимальное время кэширования CORS-запросов.