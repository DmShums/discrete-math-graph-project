# Графи ETC
## Команда №7

У цьому завданні ми реалізувати декілька функцій, які забезпечують виконання різноманітних операцій над графами, наприклад розфарбування, пошук ейлерового та гамільтонового циклів, перевірка на дводольність, тощо. Було розроблено 5 функцій, команда спільно працювала над проектом, однак основні завдання розподілялись наступним чином:
- Скутар Наталя - читання графу з файла, опис функції у звіті та презентації, основні аспекти оформлення звіту і презентації
- Чарнош Вероніка - пошук гамільтоновго циклу, опис функції у звіті та презентації
- Кучерук Анастасія - пошук ейлерового циклу, опис функції у звіті та презентації
- Дишлева Софія - двочастковість графа, опис функції у звіті та презентації
- Шумський Дмитро - розфарбування графа, опис функції у звіті та презентації

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
Функція приймає граф та перевіряє чи є він дводольним. Як агумент функція приймає словник (граф) Повертає булеве значення, яке вказує чи граф є дводольним. Алгоритм:

- 2 сети точок
- додаємо першу точку в set1, щоб почати розподіл.       р
- додаємо values(суміжні точки до першої) в set2
- якщо вершина в set2, то перевіряємо чи не належать суміжні вершини цьому сету і додаємо їх в інший, якщо перша умова виконується
- повторюємо алгоритм, поки не пройдемо всі вершини

### 5. graph_coloring()
Проблему було реалізовано за допомогою двох функцій.
grath_coloring():
- Функція приймає зв’язний граф і повертає його розфарбування у три кольори або повідомлення про те що розфарбування неможливе
- Сама функція розбивається на дві:
- checkpoint() - первіряє чи безпечно використовувати саме цей колір
- coloring_process() - за допомогою бектрекінгового алгоритму виконує саме розфарбування

coloring_process():
Допоміжна функція, яка за допомогою бібліотеки networkx та matplot візуалізує саме розфарбування:
- створюється каркас network
- зафарбовуються вершини
- зафарбовуються ребра
- створюються цифри біля вершин


### Висновки
Для реалізації цього проекту з дослідження графів ми застосували знання, отримані на курсі дискретної математики. Зокрема ми скористалися властивостями ейлерових і гамільтонових графів, умовами двочастковості та бектрекінговим алгоритмом розфарбування.
