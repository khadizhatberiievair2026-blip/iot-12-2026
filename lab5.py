
class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        """Конструктор класу з валідацією вхідних значень часу."""
        self._validate_time(hours, minutes, seconds)
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    @staticmethod
    def _validate_time(hours, minutes, seconds):
        """Перевіряє типи (тільки int, без bool) та допустимі діапазони часу."""
        for name, value in (("hours", hours), ("minutes", minutes), ("seconds", seconds)):
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError(f"Параметр '{name}' має бути цілим числом (int).")

        if not 0 <= hours < 24:
            raise ValueError("Години мають бути в діапазоні від 0 до 23.")
        if not 0 <= minutes < 60:
            raise ValueError("Хвилини мають бути в діапазоні від 0 до 59.")
        if not 0 <= seconds < 60:
            raise ValueError("Секунди мають бути в діапазоні від 0 до 59.")
            
    def __del__(self):
        pass

    def get_hours (self):
        return self.__hours

    def get_inutes(self):
        return self.__minutes

    def get_seconds(self):
        return self.__seconds


    def output_converted_time(self, value):
        if isinstance(value, bool):
            raise TypeError("Значення не може бути булевим типом (bool).")

        if isinstance(value, int):
            if value < 0:
                raise ValueError("Кількість секунд не може бути від'ємною.")
            hours = (value // 3600) % 24
            minutes = (value % 3600) // 60
            seconds = value % 60
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

       elif isinstance(value, str):
            parts = value.split(":")
            if len(parts) != 3:
                raise ValueError(f"Invalid time format: '{value}'. Expected 'HH:MM:SS'.")

            try:
                hours, minutes, seconds = map(int, parts)
            except ValueError as err:
                raise ValueError(f"Time components must be integers: '{value}'") from err

            if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
                raise ValueError(f"Time values out of range: '{value}'")

            result = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    def convertedTime(self, value):
        if isinstance(value, int):
            hours = value // 3600
            minutes = (value % 3600) // 60
            seconds = value % 60
            result = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def __str__(self):
        return f"Час: {self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"

def main():
    converter = TimeConverter(2, 30, 45)

    print("Початкові дані:")
    print(converter)

    time_str = "02:30:45"
    result1 = converter.outputConvertedTime(time_str)
    print(f"\n{time_str} = {result1} секунд")

    seconds = 9045
    result2 = converter.outputConvertedTime(seconds)
    print(f"{seconds} секунд = {result2}")

    print("\nОкремі поля:")
    print("Години:", converter.getHours())
    print("Хвилини:", converter.getMinutes())
    print("Секунди:", converter.getSeconds())


if __name__ == "__main__":
    main()

