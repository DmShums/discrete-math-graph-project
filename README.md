# Графи ETC
## Команда №7

У цьому завданні ми реалізувати декілька функцій, які забезпечують виконання різноманітних операцій над графами, наприклад розфарбування, пошук ейлерового та гамільтонового циклів, перевірка на дводольність, тощо.
Ми реалізувати 4 з 5 функцій, описаних у заваданні, зокрема усі окрім п'ятої.

### 1. read_scv()
Функція яка вміє прочитати файл і записати дані в відповідну структуру.
Як агумент функція приймає назву файлу.
Повертає словник, де ключі - номери вершин, а значення - списки номерів суміжних вешин
Використано імпортовану бібліотеку csv, необхідну для читання файлів відповідного формату.

### 2. hamiltonian_cycle()
Функція приймає граф, записаний у словник, де ключі це вершини, а їхні значення, це вершини з якими вони з’єднані. Спершу ми перевіряємо чи можемо працювати з цим графом, тобто перевіряємо його на наявність петель, а також перевіряємо чи він правильно заданий (степінь вершини має відповідати числу, скільки разів вона зустрічається у значеннях).
Далі ми створюємо шлях з вершин по яких ходимо, шукаючи Гамільтонів цикл. Шлях – це список, куди ми додаємо вершину, з якої розпочинаємо, далі додаємо вершину з її значень, які ще не були в шлях. Такий же ж алгоритм використовуємо для вершини, яку щойно додали, і так далі.
Наступним кроком ми перевіряємо чи є шлях з останньої вершини в початкову, якщо ж немає, то видаляємо її з шляху, і повторюємо попередній алгоритм, тепер уже для останньої вершини, не враховуючи ту, яку щойно викинули.
Тоді повертаємо список з вершин, які утворюють правильний Гамільтонів цикл, додаючи у нього першу, щоб показати, що це цикл.
### 3. euler_cycle()
Як аргумент функція приймає граф у вигляді словника, де ключ - вершини графа, а значення - суміжні вершини. Для початку функція перевіряє чи є граф словником, якщо ж ні - повертається None. Далі відбувається перевірка: чи має граф ізольовані вершини, вершини непарного степеня, петлі. Якщо одна з цих умов виконується - функція повертає повідомлення про те, що ейлерового циклу немає ('Graph has no Euler cycle'). Також, перевіряємо чи є в значеннях вершин ті точки, які не є серед вершин графа, якщо є такі вершини повертається відповідний меседж - 'Vertex not in graph'. Після того, як граф успішно пройшов усі перевірки відбувається пошук ейлерового циклу. Починаємо з першої вершини, і йдемо до однієї з суміжних вершин, додаємо її  у список результату . Видаляємо зі значень цю точку, а також перевіряємо, якщо в значеннях точки, яку ми додали, є початкова вершина, то видаляємо її теж. Далі ми беремо останню точку з списку результату і повторюємо усі дії, допоки всі значення ключів не стануть порожніми.  Також перевіряємо наш кінцевий список, якщо перша точка та остання однакові - повертаємо ейлеровий цикл, якщо ж ні - повертаємо повідомлення про те, що у графі немає ейлерового циклу.

### 4. dvodolniy(graph)

### 5. graph_coloring()

### Висновки
Для реалізації цього проекту з дослідження графів ми застосували знання, отримані на курсі дискретної математики. Зокрема ми скористалися властивостями ейлерових і гамільтонових графів, умовами двочастковості та бектрекінговим алгоритмом розфарбування.
Команда спільно працювала над проектом, однак основні завдання розподілялись наступним чином:
- Скутар Наталя - 1 функція, її опис у звіті та презентації, решта звіту і презентації
- Чарнош Вероніка - 2 функція, її опис у звіті та презентації
- Кучерук Анастасія - 3 функція, її опис у звіті та презентації
- Дишлева Софія - 4 функція, її опис у звіті та презентації
- Шумський Дмитро - 5 функція, її опис у звіті та презентації
