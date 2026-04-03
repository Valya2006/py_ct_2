def array_diff(a: list, b: list) -> list:
    """Решение для Задачи 1"""
    return [item for item in a if item not in b]

def sum_pairs(nums: list, sum: int) -> list:
    """Решение для Задачи 2"""
    result = set()
    for num in nums:
        a = sum - num
        if a in result:
            return [a, num]
        result.add(num)
    return None



def remove_duplicate_ids(obj: dict) -> dict:
    """Решение для Задачи 3"""
    used_chars = set()
    result = {}
    keys_sort = sorted(obj.keys(), key=int, reverse=True)
    for key in keys_sort:
        unique = list(dict.fromkeys(obj[key]))
        filtered = list(filter(lambda x: x not in used_chars, unique))
        used_chars.update(filtered)
        result[key] = filtered
    return result

# В данной функции определите самостоятельно, что она принимает, а что возвращает
def lazy(n):
    """Решение для Задачи 4"""
    def decorator(func):
        count = 0
        def wrapper(*arg, **kwargs):
            nonlocal count
            count += 1
            if n == 1:
                return func(*arg, **kwargs)
            if n == -1:
                return None
            if n > 0:
                if count == 1:
                    return func(*arg, **kwargs)
                if (count - 1) % n == 0:
                    return func(*arg, **kwargs)
                return None
            if n < 0:
                abs_n = abs(n)
                if count % abs_n == 0:
                    return None
                return func(*arg, **kwargs)
        return wrapper
    return decorator
