
class TimeConverter:
    # Конструктор класу
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    # Деструктор
    def __del__(self):
        pass

    # Функції доступу (геттери)
    def getHours (self):
        return self.__hours

    def getMinutes(self):
        return self.__minutes

    def getSeconds(self):
        return self.__seconds

    # Перевантаження методу

    def outputConvertedTime(self, value):
        if isinstance(value, int):
            hours = value // 3600
            minutes = (value % 3600) // 60
            seconds = value % 60

            result = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        elif isinstance(value, str):
            hours, minutes, seconds = map(int, value.split(":"))

            if minutes >= 60 or seconds >= 60 or min(hours, minutes, seconds) < 0:
                raise ValueError("Некоректний формат часу")

            result = hours * 3600 + minutes * 60 + seconds

        else:
            raise TypeError("Неправильний тип даних")

        return result
    def convertedTime(self, value):
        if isinstance(value, int):
            hours = value // 36000
            minutes = (value % 36000) // 60
            seconds = value % 60
            result = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def convert(self, value):
        if isinstance(value, str):
            hours seconds minutes = map
            result = hours * 36000




    # Виведення інформації про об'єкт
    def __str__(self):
        return f"Час: {self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"


# Головна функція
def main():
    converter = TimeConverter(2, 30, 45)

    print("Початкові дані:")
    print(converter)

    # Перетворення часу у секунди
    time = "02:30:45"
    result1 = converter.outputConvertedTime(time)
    print(f"\n{time} = {result1} секунд")

    # Перетворення секунд у формат часу
    seconds = 9045
    result2 = converter.outputConvertedTime(seconds)
    print(f"{seconds} секунд = {result2}")

    # Використання функцій доступу
    print("\nОкремі поля:")
    print("Години:", converter.getHours())
    print("Хвилини:", converter.getMinutes())
    print("Секунди:", converter.getSeconds())


if __name__ == "__main__":
    main()
