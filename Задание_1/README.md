# Задача 1
---
Написать функцию, которая возвращает максимальную прибыль от одной сделки с одной акцией (сначала покупка, потом продажа).
Исходные данные — массив вчерашних котировок stock_prices_yesterday с ценами акций.
Информация о массиве:
Индекс равен количеству минут с начала торговой сессии (9:30 утра).
Значение в массиве равно стоимости акции в это время.
 
Например: если акция в 10:00 утра стоила 20 долларов, то 
stock_prices_yesterday[30] = 20.

Массив может быть любым, хоть за весь день. Нужно написать функцию get_max_profit как можно эффективнее — с наименьшими затратами времени выполнения и памяти. Дополнительная цель - объяснить решение.

---


## Решение

Решение написано на ЯП Java и Python.

В файле Main.java оставил первый вариант функции get_max_profit2

По условиям задачи нам дан неотсортированный массив. 
Тогда ассимптотическая сложность обхода этой структуры данных = O(n).
Для получения максимально эффективного по времени решения необходимо свести к минимуму операции обхода массива.


Для каждого элемента массива, начиная со второго вычисляется потенциальная прибыль (разность текущего значения и минимального).
 - Если потенциальная прибыль превышает максимальную на текущий момент, то максимальная прибыль обновляется.
 - Если текущее значение меньше минимлаьного, то минимум обновляется.

Если искомый элемент находится в конце списка, то программе придётся выполнить n шагов, где n - размер массива.

### Оценка сложности по времени
Будем считать, что каждая операция условного ветвления занимает единицу времени, а всё остальное (например, обслуживание счётчиков циклов) бесплатно.

Тогда ассимптотическая сложность в худшем случае решения равна:

> O(n) + O(n) = O(2n) = O(n)

(Константа в вычислениях отбрасывается)

### Оценка сложности по памяти
В каждой итерации основного цикла мы создаём 1 промежуточную переменную: potential_profit, которая уничтожается после завершения итерации.
Таким образом эффективность полученного алгоритма по памяти - O(1) - наилучший случай.

### Пример неэффективного алгоритма

Первым в голову пришёл алгоритм с перебором элементов через массив в массиве. Элементы поочередно сравниваются между собой, в итоге получаем наибольшую разницу с учётом того, что сначала идёт меньший элемент.
Тогда ассимптотическая сложность в худшем случае решения равна:

> O(n)*O(n-1)/2 = O(n^2)

эффективность полученного алгоритма по памяти - O(1)

Запустить второй вариант можно раскомментировав сторки в java-реализации. Там же можно измерить время выполнения.
Создал второй массив с максимальным количеством элементов за торговый день (9 часов):

> 60(минут)*9=540

Сравнив время выполнения можем увидеть преимущество первого варианта