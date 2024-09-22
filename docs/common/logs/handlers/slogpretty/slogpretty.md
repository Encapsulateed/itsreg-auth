Вот документация для данного кода в указанном формате:

### 1. Структура PrettyHandlerOptions
```go
type PrettyHandlerOptions struct {
	SlogOpts *slog.HandlerOptions
}
```
- Структура для хранения опций, связанных с созданием `PrettyHandler`. Включает настройки `slog.HandlerOptions`.

### 2. Структура PrettyHandler
```go
type PrettyHandler struct {
	opts PrettyHandlerOptions
	slog.Handler
	l     *stdLog.Logger
	attrs []slog.Attr
}
```
- Структура `PrettyHandler` реализует интерфейс `slog.Handler` и добавляет функциональность для красивого форматирования логов. Содержит логгер стандартной библиотеки и атрибуты для расширения логирования.

### 3. Метод NewPrettyHandler
```go
func (opts PrettyHandlerOptions) NewPrettyHandler(out io.Writer) *PrettyHandler
```
- Метод создает новый экземпляр `PrettyHandler`, использующий `slog.JSONHandler` для форматирования вывода в JSON и стандартный логгер для вывода сообщений. Принимает `io.Writer` для указания места вывода логов.

### 4. Метод Handle
```go
func (h *PrettyHandler) Handle(_ context.Context, r slog.Record) error
```
- Метод обрабатывает запись лога, окрашивая уровень логирования и выводя сообщение в консоль в цвете. Форматирует атрибуты записи в виде JSON. Возвращает ошибку, если произошла ошибка при маршализации JSON.

### 5. Метод WithAttrs
```go
func (h *PrettyHandler) WithAttrs(attrs []slog.Attr) slog.Handler
```
- Метод создает новый экземпляр `PrettyHandler`, добавляя новые атрибуты к уже существующим. Это позволяет расширять контекст логирования без изменения исходного обработчика.

### 6. Метод WithGroup
```go
func (h *PrettyHandler) WithGroup(name string) slog.Handler
```
- Метод создает новый экземпляр `PrettyHandler`, добавляя группу к логгеру. Позволяет организовать логи по группам, не изменяя исходный обработчик.