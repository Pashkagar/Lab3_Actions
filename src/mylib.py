# определение n чисел Фибоначчи – функция принимает n, возвращает список из чисел
def fibonacci(n):
    fib = [0, 1]
    if n <= 0:
        return "Input should be a positive integer"
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]


# сортировка пузырьком - функция принимает список чисел, возвращает его отсортированную копию
def bubble_sort(arr):
    n = len(arr)
    sorted_arr = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr


# калькулятор  функция принимает 3 аргумента:
# число 1, число 2 и знак действия: +, -, *, /
# выполняет действие и возвращает результат
def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
