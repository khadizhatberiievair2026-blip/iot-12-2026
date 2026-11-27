"""Time conversion between HH:MM:SS strings and seconds."""

HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = MINUTES_PER_HOUR * SECONDS_PER_MINUTE


class TimeConverter:
    """Convert time between HH:MM:SS format and total seconds."""

    def __init__(
        self,
        hours: int = 0,
        minutes: int = 0,
        seconds: int = 0,
    ) -> None:
        """Initialize converter with validated time components."""
        self._validate_time(hours, minutes, seconds)
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def __del__(self) -> None:
        """Clean up converter instance on finalization."""

    @staticmethod
    def _validate_time(hours: int, minutes: int, seconds: int) -> None:
        """Validate integer types (excluding bool) and time bounds."""
        components = (
            ("hours", "Години", hours, HOURS_PER_DAY),
            ("minutes", "Хвилини", minutes, MINUTES_PER_HOUR),
            ("seconds", "Секунди", seconds, SECONDS_PER_MINUTE),
        )
        for name, label, value, upper_bound in components:
            if isinstance(value, bool) or not isinstance(value, int):
                msg = f"Параметр '{name}' має бути цілим числом (int)."
                raise TypeError(msg)
            if not 0 <= value < upper_bound:
                msg = f"{label} мають бути в діапазоні від 0 до {upper_bound - 1}."
                raise ValueError(msg)

    @property
    def hours(self) -> int:
        """Hours component (0 to 23)."""
        return self._hours

    @property
    def minutes(self) -> int:
        """Minutes component (0 to 59)."""
        return self._minutes

    @property
    def seconds(self) -> int:
        """Seconds component (0 to 59)."""
        return self._seconds

    def output_converted_time(self, value: int | str) -> str | int:
        """Convert seconds to HH:MM:SS or HH:MM:SS to seconds."""
        if isinstance(value, bool):
            msg = "Значення не може бути булевим типом (bool)."
            raise TypeError(msg)

        if isinstance(value, int):
            if value < 0:
                msg = "Кількість секунд не може бути від'ємною."
                raise ValueError(msg)
            total_minutes, seconds = divmod(value, SECONDS_PER_MINUTE)
            hours, minutes = divmod(total_minutes, MINUTES_PER_HOUR)
            hours %= HOURS_PER_DAY
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        if isinstance(value, str):
            parts = value.split(":")
            if len(parts) != 3 or not all(
                part.isascii() and part.isdigit() and len(part) <= 2 for part in parts
            ):
                msg = f"Некоректний формат часу: '{value}'. Очікується 'HH:MM:SS'."
                raise ValueError(msg)

            hours, minutes, seconds = map(int, parts)
            self._validate_time(hours, minutes, seconds)
            return hours * SECONDS_PER_HOUR + minutes * SECONDS_PER_MINUTE + seconds

        msg = (
            "Значення має бути цілим числом (int) або рядком (str), "
            f"отримано {type(value).__name__}."
        )
        raise TypeError(msg)

    def __str__(self) -> str:
        """Return formatted time as 'Час: HH:MM:SS'."""
        return f"Час: {self._hours:02d}:{self._minutes:02d}:{self._seconds:02d}"


def main() -> None:
    """Demonstrate TimeConverter functionality."""
    converter = TimeConverter(2, 30, 45)

    print("Початкові дані:")
    print(converter)

    time_str = "02:30:45"
    converted_seconds = converter.output_converted_time(time_str)
    print(f"\n{time_str} = {converted_seconds} секунд")

    seconds = 9045
    converted_time = converter.output_converted_time(seconds)
    print(f"{seconds} секунд = {converted_time}")

    print("\nОкремі поля:")
    print("Години:", converter.hours)
    print("Хвилини:", converter.minutes)
    print("Секунди:", converter.seconds)


if __name__ == "__main__":
    main()