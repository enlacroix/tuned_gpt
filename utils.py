import functools


def retry_on_error(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        max_retries = 3
        for i in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Произошла ошибка, осталось ({i + 1}/{max_retries} попыток)...")
        # If all retries failed, raise the last exception
        raise e

    return wrapper
