# Класс дескриптора
class ValidatedField:
    def __init__(self, data_type, min_value = None, max_value = None, min_length = None, max_length = None):
        self.data_type = data_type
        self.min_value = min_value
        self.max_value = max_value
        self.min_length = min_length
        self.max_length = max_length
        self.data = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(instance, None)

    def __set__(self, inst, value):
        # Проверка типа данных
        if not isinstance(value, self.data_type):
            raise ValueError(f"Недопустимый тип: {self.data_type}")
        
        # Проверка на значения для int или float
        if self.data_type in (float, int):
            if self.min_value is not None and self.min_value > value:
                raise ValueError(f"Недопустимый возраст: {value}")
            if self.max_value is not None and self.max_value < value:
                raise ValueError(f"Недопустимый возраст: {value}")
        
        # Проверка на str или list
        if self.data_type in (str, list):
            if self.min_length is not None and self.min_length > len(value):
                raise ValueError(f"Недопустимое имя: {value}")
            if self.max_length is not None and self.max_length < len(value):
                raise ValueError(f"Недопустимое имя: {value}")
                
        self.data[inst] = value



# Клиентский класс
class Person:
    name = ValidatedField(str, min_length=3, max_length=50)
    age = ValidatedField(int, min_value=0, max_value=120)

person = Person()

# Допустимые значения
person.name = "Alice"
person.age = 25 

print(person.name)
print(person.age)


# Некорректные значения
try:
    person.name = "Al"  # Слишком короткое имя
except ValueError as e:
    print(e) 

try:
    person.age = -5  # Отрицательный возраст
except ValueError as e:
    print(e)




