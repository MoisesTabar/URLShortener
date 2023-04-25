from dataclasses import dataclass
import validators

@dataclass(slots=True)
class Url:

    value: str

    def __post_init__(self) -> None:

        if not validators.url(self.value):
            raise ValueError(f"The URL: {self.value} is not a value URL, please try again.")