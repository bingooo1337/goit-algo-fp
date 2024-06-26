## Завдання 7: Порівняємо отримані результати за допомогою методу Монте-Карло з аналітичними розрахунками

Аналітичні ймовірності обчислюються виходячи з кількості комбінацій, які дають кожну суму при киданні двох кубиків. Зважаючи на те, що всього є 6×6=36 можливих результатів кидка двох кубиків, аналітичні ймовірності можна обчислити як частку кількості комбінацій для кожної суми до загальної кількості можливих результатів.

| Сума | Аналітична ймовірність | Ймовірність (Монте-Карло) |
|------|------------------------|---------------------------|
|   2  |          2.78%         |           2.777%          |
|   3  |          5.56%         |           5.529%          |
|   4  |          8.33%         |           8.334%          |
|   5  |         11.11%         |          11.096%          |
|   6  |         13.89%         |          13.868%          |
|   7  |         16.67%         |          16.698%          |
|   8  |         13.89%         |          13.886%          |
|   9  |         11.11%         |          11.110%          |
|  10  |          8.33%         |           8.346%          |
|  11  |          5.56%         |           5.568%          |
|  12  |          2.78%         |           2.790%          |

Як видно з таблиці, результати симуляції дуже близькі до аналітичних значень. Це показує, що метод Монте-Карло є ефективним для оцінки ймовірностей у задачах, де можна визначити аналітичні значення. Невеликі відхилення пояснюються випадковим характером симуляцій, але з збільшенням кількості симуляцій ці відхилення ще більше зменшуються.