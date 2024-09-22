Вот документация для указанного пакета `main` в нужном формате:

### Пакет `main`

#### Функция `main`
```go
func main() {
	app, cleanup := service.NewApplication()
	defer cleanup()

	server.RunHTTPServer(func(router chi.Router) http.Handler {
		return httpport.HandlerFromMux(httpport.NewHTTPServer(app), router)
	})
}
```
- **Описание:**
  - Основная функция приложения, которая инициализирует сервис и запускает HTTP сервер.

- **Параметры:**
  - `app`: объект приложения, возвращаемый функцией `service.NewApplication()`.
  - `cleanup`: функция очистки ресурсов, вызываемая с помощью `defer` для обеспечения корректного завершения работы.

- **Логика:**
  1. Инициализирует новое приложение с помощью `service.NewApplication()`.
  2. Отложенно вызывает функцию `cleanup()` для освобождения ресурсов при завершении работы.
  3. Запускает HTTP сервер, передавая функцию-обработчик, которая создает HTTP сервер на основе Mux из библиотеки `chi`.

#### Взаимодействующие Пакеты:
- **`github.com/go-chi/chi/v5`**: библиотека для маршрутизации HTTP.
- **`github.com/itsreg-auth/internal/common/server`**: пакет для запуска HTTP сервера.
- **`github.com/itsreg-auth/internal/ports/httpport`**: пакет, предоставляющий интерфейс для работы с HTTP сервером.
- **`github.com/itsreg-auth/internal/service`**: пакет, отвечающий за бизнес-логику приложения.