# 📊 Telegram-бот для построения графиков
## 📝 Бизнес-задача
Цель этого проекта — разработка Telegram-бота для автоматизации построения визуализаций данных на основе пользовательских данных. Основная бизнес-задача заключалась в упрощении процесса создания графиков для пользователей без необходимости в специализированных инструментах или знаниях анализа данных. Пользователь может загрузить свои данные в формате CSV или XLSX, выбрать тип графика, и бот автоматически сгенерирует соответствующую визуализацию.

## 🚀 Выбор технологий
### Для решения задачи были выбраны следующие технологии:

- Python: Основной язык для разработки логики бота и обработки данных.
- Aiogram: Асинхронная библиотека для взаимодействия с Telegram API, что позволяет боту обрабатывать сообщения от пользователей в реальном времени.
- Pandas: Для загрузки и предварительной обработки пользовательских данных в форматах CSV и XLSX.
- Seaborn и Matplotlib: Для создания графиков и визуализаций данных.
- Asyncio: Для асинхронной обработки запросов, что ускоряет работу бота.
  
### Почему были выбраны эти технологии?

- Aiogram обеспечивает удобный способ интеграции с Telegram и поддерживает асинхронные операции, что ускоряет обработку пользовательских запросов.
- Pandas является стандартом для работы с данными в Python и позволяет легко манипулировать табличными данными.
- Seaborn и Matplotlib — мощные библиотеки для создания профессиональных графиков с минимальными усилиями.
- Asyncio делает бота отзывчивым и позволяет выполнять несколько задач параллельно, необходимо при разработке бота.
  
## 🔧 Решение задачи
- Получение данных: Пользователь загружает файл с данными (CSV или XLSX), и бот сохраняет файл, затем читает данные с помощью библиотеки Pandas.
- Выбор типа графика: Пользователю предлагается выбрать тип графика (круговая диаграмма, столбчатая диаграмма, гистограмма или точечная диаграмма) через встроенные клавиатуры.
- Выбор столбцов: После выбора графика бот запрашивает у пользователя, какие столбцы использовать для визуализации.
- Построение графика: На основе выбора пользователя и загруженных данных строится график с использованием Matplotlib и Seaborn.
- Отправка графика: После построения график сохраняется в виде изображения, которое отправляется пользователю обратно в чат.

## 📂 Структура репозитория
- main.py: Основной код бота, содержащий логику обработки сообщений и создание графиков.
- keyboards/inline_kbs.py: Код для создания встроенных клавиатур для взаимодействия с пользователем.
- requirements.txt: Список всех зависимостей проекта.

## 📈 Визуализации
### Поддерживаются следующие типы графиков:

- Круговая диаграмма (Pie Chart).
- Столбчатая диаграмма (Bar Plot).
- Гистограмма (Histogram).
- Точечная диаграмма (Scatter Plot).
