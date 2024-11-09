data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]
def calculate_structure_sum(data):
    total = 0
    def recursive_sum(item):
        nonlocal total
        if isinstance(item, int):
            total += item
        elif isinstance(item,str):
            total += len(item)
        elif isinstance(item, (list, tuple, set)):
            for sub_item in item:
                recursive_sum(sub_item)
        elif isinstance(item, dict):
            for key, value in item.items():
                recursive_sum(key)
                recursive_sum(value)
    recursive_sum(data)
    return total
result = calculate_structure_sum(data_structure)
print(result)



