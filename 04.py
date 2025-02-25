def generate_brackets(n):
    def backtrack(open_count, close_count, current, result, counter):
        print('open_count',open_count,' | close_count',close_count,
            ' | current',current
            # ,' | result[counter[0]]', result[counter[0]]
            ,' | counter[0]', counter[0])
        if len(current) == 2 * n:
            result[counter[0]] = current
            counter[0] += 1
            print('========= one variant completed ==================')
            return
            
        if open_count < n:
            backtrack(open_count + 1, close_count, current + '(', result, counter)
        if close_count < open_count:
            backtrack(open_count, close_count + 1, current + ')', result, counter)
    
    result = {}
    counter = [0]  # используем список для передачи счетчика по ссылке
    backtrack(0, 0, '', result, counter)
    return result

n = int(input())
sequences = generate_brackets(n)
for key in sorted(sequences.keys()):
    print(sequences[key])


"""
D. Генерация скобочных последовательностей
Ограничение времени	1 секунда
Ограничение памяти	20Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дано целое число n. Требуется вывести все правильные скобочные последовательности длины 2 ⋅ n, упорядоченные лексикографически (см. https://ru.wikipedia.org/wiki/Лексикографический_порядок).

В задаче используются только круглые скобки.

Желательно получить решение, которое работает за время, пропорциональное общему количеству правильных скобочных последовательностей в ответе, и при этом использует объём памяти, пропорциональный n.

Формат ввода
Единственная строка входного файла содержит целое число n, 0 ≤ n ≤ 11

Формат вывода
Выходной файл содержит сгенерированные правильные скобочные последовательности, упорядоченные лексикографически.

Пример 1
Ввод	Вывод
2
(())
()()
Пример 2
Ввод	Вывод
3
((()))
(()())
(())()
()(())
()()()
"""

"""
рекурсивная функция неявно хранит дерево вызовов в стеке вызовов (call stack), который управляется интерпретатором Python.

🔹 Как работает стек вызовов в рекурсии?
Когда функция backtrack вызывается, интерпретатор Python:

Создаёт новый кадр стека (stack frame), где хранятся:
Текущие значения аргументов (open_count, close_count, current, result, counter).
Место, куда нужно вернуться после завершения функции.
Какие ветви if уже были выполнены.
Когда рекурсивный вызов завершается (return), этот стековый кадр удаляется, а управление возвращается в точку вызова.

Разберём на примере перехода от "((()))" к "(()"
Допустим, n = 3. Вот дерево вызовов:

backtrack(0, 0, "")
 ├─ backtrack(1, 0, "(")
 │   ├─ backtrack(2, 0, "((")
 │   │   ├─ backtrack(3, 0, "(((")
 │   │   │   ├─ backtrack(3, 1, "((()")
 │   │   │   │   ├─ backtrack(3, 2, "((())")
 │   │   │   │   │   ├─ backtrack(3, 3, "((()))")  ← [Финальный return, выход]
 │   │   │   │   │   └─ возврат в `"((())"`
 │   │   │   │   └─ возврат в `"((()"`
 │   │   │   └─ возврат в `"((("`
 │   │   ├─ **backtrack(2, 1, "(()")**  ← [новый вариант]
 │   │   │   ├─ backtrack(3, 1, "(()(")
 │   │   │   │   ├─ ... (дальше по аналогии)

Когда "((()))" найдено, стек вызовов начинает разворачиваться:

Вершина стека (backtrack(3, 3, "((()))")) завершает выполнение и удаляется.
Возвращаемся в backtrack(3, 2, "((())"), но тут больше нет других if → ещё один return.
Аналогично откатываемся назад, пока не вернёмся к backtrack(2, 0, "((").
Что происходит в backtrack(2, 0, "((")?

В этот момент правая ветка (if close_count < open_count:) ещё не была вызвана, поэтому вызываем backtrack(2, 1, "(()").

Где хранятся все эти данные?
📌 В стеке вызовов (call stack).
Python автоматически управляет стеком, добавляя новые вызовы (push) и удаляя их при завершении (pop).

Пример визуализации стека в момент ((())):
Каждый вызов хранит:

Аргументы (open_count, close_count, current).
Адрес возврата (где продолжить после return).

-----------------------------------------------------
| backtrack(3, 3, "((()))")  <- Верхний кадр стека
| backtrack(3, 2, "((())")
| backtrack(3, 1, "((()")
| backtrack(3, 0, "(((")
| backtrack(2, 0, "((")
-----------------------------------------------------

После return из "((()))", стек схлопывается:
-----------------------------------------------------
| backtrack(3, 2, "((())") <- Теперь верхний кадр
| backtrack(3, 1, "((()")
| backtrack(3, 0, "(((")
| backtrack(2, 0, "((")
-----------------------------------------------------

Так продолжается, пока не найдётся новый путь ((()).
🔹 Вывод
Дерево вызовов не хранится в явном виде.
Интерпретатор Python автоматически управляет стеком вызовов.
Стек позволяет "откатываться" назад и проверять альтернативные пути.
Когда одна ветка if завершилась, Python возвращается в точку вызова и проверяет, есть ли другой if, который ещё не выполнялся.
"""