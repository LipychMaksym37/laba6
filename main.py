from decorators import ignore_errors

@ignore_errors
def divide(a, b):
    return a / b

print(divide(10, 2))   # 5.0
print(divide(10, 0))   # "Помилка оброблена"
print(divide("a", 2))  # "Помилка оброблена"
