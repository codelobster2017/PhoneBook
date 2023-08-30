class Human:
    def __init__(self, name: str, age: int, work='GB'):
        self.name = name
        self.age = age
        self.work = work
    
    def __str__(self) -> str:
        return f'Человек по имени {self.name}, {self.age} лет от роду, трудится на {self.work} '

    def greetings(self):
        return f'{self.name} приветствует тебя!'

stone = Human('Андрей', 28, 'DP')

print(stone)