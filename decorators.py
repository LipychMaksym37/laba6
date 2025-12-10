def ignore_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            return "Помилка оброблена"
    return wrapper
