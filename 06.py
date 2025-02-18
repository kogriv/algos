from collections import deque

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def solve():
    # Read input
    n = int(input())
    cities = []
    for _ in range(n):
        x, y = map(int, input().split())
        cities.append((x, y))
    
    k = int(input())
    start, end = map(lambda x: int(x) - 1, input().split())
    
    # Create adjacency list
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist = manhattan_distance(cities[i][0], cities[i][1], 
                                       cities[j][0], cities[j][1])
                if dist <= k:
                    graph[i].append(j)
    
    # BFS to find shortest path
    visited = [-1] * n
    queue = deque([start])
    visited[start] = 0
    
    while queue:
        current = queue.popleft()
        if current == end:
            return visited[end]
            
        for next_city in graph[current]:
            if visited[next_city] == -1:
                visited[next_city] = visited[current] + 1
                queue.append(next_city)
    
    return -1

print(solve())

"""
This is essentially a graph problem where we 
need to find the shortest path between
cities while ensuring the distance between
consecutive cities doesn't exceed the fuel capacity k.

Here's a solution in Python that uses
breadth-first search (BFS) to find the shortest path:

This solution:

Takes input in the specified format
Calculates Manhattan distance between cities
Creates a graph where edges exist between cities that are within distance k
Uses BFS to find the shortest path from start to end city
Returns the minimum number of roads needed or -1 if no path exists
"""


"""
Не секрет, что некоторые программисты очень любят путешествовать. Хорошо всем известный программист Петя тоже очень любит путешествовать, посещать музеи и осматривать достопримечательности других городов.
Для перемещений между из города в город он предпочитает использовать машину. При этом он заправляется только на станциях в городах, но не на станциях по пути. Поэтому он очень аккуратно выбирает маршруты, чтобы машина не заглохла в дороге. А ещё Петя очень важный член команды, поэтому он не может себе позволить путешествовать слишком долго. Он решил написать программу, которая поможет ему с выбором очередного путешествия. Но так как сейчас у него слишком много других задач, он попросил вас помочь ему.
Расстояние между двумя городами считается как сумма модулей разности по каждой из координат. Дороги есть между всеми парами городов.

Формат ввода
В первой строке входных данных записано количество городов n (2≤n≤1000). В следующих n строках даны два целых числа: координаты каждого города, не превосходящие по модулю миллиарда. Все города пронумерованы числами от 1 до n в порядке записи во входных данных.
В следующей строке записано целое положительное число k, не превосходящее двух миллиардов, — максимальное расстояние между городами, которое Петя может преодолеть без дозаправки машины.
В последней строке записаны два различных числа — номер города, откуда едет Петя, и номер города, куда он едет.

Формат вывода
Если существуют пути, удовлетворяющие описанным выше условиям, то выведите минимальное количество дорог, которое нужно проехать, чтобы попасть из начальной точки маршрута в конечную. Если пути не существует, выведите -1.
Пример 1
Ввод
Вывод
7
0 0
0 2
2 2
0 -2
2 -2
2 -1
2 1
2
1 3

2
"""