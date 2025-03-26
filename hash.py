# Класс пользователей
class User(object):
    def __init__(self, name: str, age: int, info: str = ''):
        self.name = name
        self.age = age
        self.info = info

    def __repr__(self):
        return f"User(name: {self.name}, age: {self.age}, email: {self.info})"
    


# Класс хэш-функций
class HashFunc(User):
    def __init__(self, name: str, age: int, info: str= '', func: str = ''):
        super().__init__(name, age, info)
        if func == 'djb2':
            self.index = self.djb2()
        if func == 'MurmurHash':
            self.index = self.MurmurHash()

    def djb2(self) -> int:
        # Начальное значение хэша и константа
        hash = 5381
        c1 = 5

        # Вычисляем хэш при каждом символе name 
        for c in self.name:
            hash = ((hash << c1) + hash) + ord(c) # hash = hash * 33 + c

        # Добавляем возраст к хэшу
        hash = ((hash << c1) + hash) + self.age

        return hash & 0xFF # Обрезать до 3 знаков
    

    def MurmurHash(self) -> int:
        # Начальное значение хэша и константы
        hash = 5381
        c1 = 6
        c2 = 5

        # Вычисляем хэш при каждом символе name 
        for c in self.name:
            k = ((ord(c) << c1) + ord(c)) >> c2
            hash = hash * k

        # Добавляем возраст к хэшу
        k = ((self.age << c1) + self.age) >> c2
        hash = hash * k

        return hash & 0xFF # Обрезать до 3 знаков
    

# Класс хэш таблицы
class HashTable():
    def __init__(self, size: int = 10):
        self.size = size
        self.buckets = [[] for _ in range(size)]


    # Вставка
    def insert(self, user: User) -> list[list]:
        bucket = self.buckets[user.index]
        for i, (k, v, a) in enumerate(bucket):
            if k == user.name:
                bucket[i] = (user.name, user.age, user.info)
                return None
        bucket.append((user.name, user.age, user.info))


    # Получение по индексу
    def get(self, user: User) -> list[tuple[str]]:
        return self.buckets[user.index]
    
    # Удаление по индексу
    def delete(self, user: User) -> None:
        self.buckets[user.index] = []
        return None
    
    # Размер таблицы
    def sizeof(self):
        return f"Размер таблицы: {len(self.buckets)}"

    # Количество заполненных ячеек таблицы
    def count_cell(self):
        c = 0
        for i in self.buckets:
            if i != []:
                c +=1 
        return c
    

    # Получение всех ключей
    def key(self) -> list[str]:
        a = []
        for buck in self.buckets:
            for name_key, age_key, info in buck:
                a.append(name_key)
        return a
    

    # Получение всех значений
    def values(self) -> list[str]:
        val = []
        for buck in self.buckets:
            for name_key, age_key, info in buck:
                val.append(info)
        return val
    

    # Получение всех пар ключ: значение
    def item(self) -> list[tuple[str]]:
        item = []
        for buck in self.buckets:
            for name_key, age_key, info in buck:
                item.append((name_key, age_key, info))
        return item
    

    # Лоад фактор таблицы
    def load_factor(self) -> float:
        return self.count_cell() / len(self.buckets)
    

    # Проверка содержимого
    def containts(self, user: HashFunc):
        if self.buckets[user.index] != []:
            return True
        return False
    
    # Очищает всю таблицу
    def clear(self):
        self.buckets = [[] for _ in range(self.size)]
        return self.buckets
    



if __name__ == '__main__':
    user1 = HashFunc("Oleg", 52, "olega@google.com", 'MurmurHash')
    user2 = HashFunc('Atom', 25, "atom@google.com", 'MurmurHash')
    user3 = HashFunc('Serega', 20, "serega@google.com", 'MurmurHash')

    hash_table = HashTable(size = 1000)

    hash_table.insert(user1)
    hash_table.insert(user2)
    hash_table.insert(user3)
    print(hash_table.get(user2))
    print(f'Количество заполненных ячеек таблицы: {hash_table.count_cell()}')
    hash_table.delete(user1)
    print(hash_table.buckets)
    print(hash_table.key())
    print(hash_table.values())
    print(hash_table.item())
    print(hash_table.load_factor())
    print(hash_table.containts(user1))
    # print(hash_table.clear())



