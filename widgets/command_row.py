from textual.widgets import Static
from rich.text import Text

CMD_WIDTH  = 22
INSTALLABLE_BADGE_BG   = "#7a58a3"
BADGE_BG   = "#7aa2f7"
BADGE_FG   = "#1e1e2e"
DESC_COLOR = "#a9b1d6"


class CommandRow(Static):

    def __init__(self, cmd: str, desc: str, installable: bool, **kwargs) -> None:
        super().__init__(**kwargs)
        self.installable = installable
        self.cmd  = cmd
        self.desc = desc

    def render(self) -> Text:
        text = Text()
        BADGE_COLOR = INSTALLABLE_BADGE_BG if self.installable else BADGE_BG
        text.append(f" {self.cmd:<{CMD_WIDTH}}", style=f"bold {BADGE_FG} on {BADGE_COLOR}")
        text.append("  ")
        text.append(self.desc, style=DESC_COLOR)
        return text
