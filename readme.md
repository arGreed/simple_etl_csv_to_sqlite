## Итоговые проекты этапа 1

### 📝 Проект 1: ETL-процесс для CSV → SQLite
**Цель:** Создать автоматизированный процесс обработки данных  
**Требования:**
- Входные данные: CSV-файлы с продажами (дата, продукт, цена)
- Этапы:
  1. Валидация данных (типизация, проверка на дубликаты)
  2. Трансформация (агрегация по типу товаров)
  3. Загрузка в SQLite с логированием
- Выходные данные: База данных с таблицами `raw_data` и `aggregated_data`

**Этапы:**
1. Создание класса валидации данных
2. Реализация агрегации (сумма, среднее)
3. Настройка логирования
4. Добавление CLI-интерфейса

**Дополнительно:**
- Реализовать повторные попытки при ошибках
- Добавить тесты для проверки корректности агрегации
