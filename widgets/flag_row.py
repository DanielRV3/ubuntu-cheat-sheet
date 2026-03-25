from textual.widgets import Static
from rich.text import Text

FLAG_WIDTH  = 20
FLAG_COLOR  = "#e0af68"
DESC_COLOR  = "#565f89"   


class FlagRow(Static):
    def __init__(self, flag: str, desc: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.flag = flag
        self.desc = desc

    def render(self) -> Text:
        text = Text()
        text.append("    ")                                    # sangría
        text.append(f"{self.flag:<{FLAG_WIDTH}}", style=f"bold {FLAG_COLOR}")
        text.append("  ")
        text.append(self.desc, style=DESC_COLOR)
        return text
