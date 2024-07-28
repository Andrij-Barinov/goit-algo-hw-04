import timeit
import random

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Генерація даних для тестування
def generate_data(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Вимірювання часу виконання
def measure_time(sort_function, data):
    start_time = timeit.default_timer()
    sort_function(data)
    return timeit.default_timer() - start_time

# Основна функція для виконання тестів
def main():
    data_sizes = [100, 1000, 10000]
    algorithms = {
        "Merge Sort": merge_sort,
        "Insertion Sort": insertion_sort,
        "Timsort": sorted
    }

    for size in data_sizes:
        print(f"Data size: {size}")
        for name, func in algorithms.items():
            data = generate_data(size)
            time_taken = measure_time(func, data.copy())
            print(f"{name}: {time_taken:.6f} seconds")
        print()

if __name__ == "__main__":
    main()
