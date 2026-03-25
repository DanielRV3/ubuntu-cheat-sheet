from textual.widgets import Static
from rich.text import Text


class CustomFooter(Static):

    def render(self) -> Text:
        text = Text()

        text.append("  Navegar: ", style="#565f89")
        text.append(" ← a ", style="bold #1e1e2e on #7aa2f7")
        text.append(" / ", style="#565f89")
        text.append(" d → ", style="bold #1e1e2e on #7aa2f7")
        text.append("    Salir: ", style="#565f89")
        text.append(" q ", style="bold #1e1e2e on #f7768e")

        text.append("      │      ", style="#3b4261")

        text.append("  ", style="bold #1e1e2e on #7aa2f7")
        text.append(" Comando", style="#7aa2f7")
        
        text.append("    ", style="#565f89")
        text.append("  ", style="bold #1e1e2e on #e0af68")
        text.append(" Bandera", style="#e0af68")
        
        text.append("    ", style="#565f89")
        text.append("  ", style="bold #1e1e2e on #7a58a3")
        text.append(" Necesita Instalación", style="#7a58a3")

        return text
