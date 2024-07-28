import heapq

def merge_k_lists(lists):
    # Створюємо мін-купу для відслідковування мінімальних елементів
    min_heap = []
    for i in range(len(lists)):
        if lists[i]:  # Перевірка, чи список не порожній
            heapq.heappush(min_heap, (lists[i][0], i, 0))
    
    result = []
    while min_heap:
        # Витягуємо найменший елемент з купи
        val, list_index, element_index = heapq.heappop(min_heap)
        result.append(val)
        
        # Якщо список, з якого був взятий елемент, не пустий, додаємо наступний елемент до купи
        if element_index + 1 < len(lists[list_index]):
            next_val = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_val, list_index, element_index + 1))
    
    return result

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
