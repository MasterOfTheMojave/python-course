import json
from functools import wraps

# Значение атрибута __name__ задекорированной
# функции не должно изменяться. Используйте 
# декоратор wraps из модуля functools.
def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwds):
        return_value = json.dumps(func(*args, **kwds))
        return return_value 
    return wrapper


@to_json
def get_data():
  return {
    'data': 42
  }

print(get_data())  # вернёт '{"data": 42}'
#print(get_data.__name__)