from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, ScrollableContainer
from textual.reactive import reactive
from textual.widgets import Footer, Label

from data import cargar_categorias
from widgets import CommandRow, FlagRow, CustomFooter


class CheatSheetApp(App):

    CSS_PATH = Path(__file__).parent / "styles.tcss"

    BINDINGS = [
        ("a",     "prev_tab", "Anterior"),
        ("d",     "next_tab", "Siguiente"),
        ("left",  "prev_tab", ""),
        ("right", "next_tab", ""),
        ("q",     "quit",     "Salir"),
    ]

    current: reactive[int] = reactive(0)

    def __init__(self) -> None:
        super().__init__()
        self.categorias = cargar_categorias()
        self.nombres    = list(self.categorias.keys())

    def compose(self) -> ComposeResult:
        with Horizontal(id="tabs"):
            for i, nombre in enumerate(self.nombres):
                yield Label(nombre, classes="tab active" if i == 0 else "tab", id=f"tab-{i}")

        with ScrollableContainer(id="content"):
            yield Label("", id="category-title")
            yield Container(id="cmd-list")

        yield CustomFooter()

    def on_mount(self) -> None:
        self._render_page(0)

    def _render_page(self, index: int) -> None:
        # Actualizar tabs
        for i in range(len(self.nombres)):
            self.query_one(f"#tab-{i}", Label).set_class(i == index, "active")

        # Actualizar título
        nombre = self.nombres[index]
        self.query_one("#category-title", Label).update(
            f"  {nombre}  ({index + 1}/{len(self.nombres)})"
        )

        # Montar comandos y sus banderas
        cmd_list = self.query_one("#cmd-list", Container)
        cmd_list.remove_children()

        for entrada in self.categorias[nombre]:
            installable = bool(entrada.get("installable", False))
            cmd_list.mount(CommandRow(entrada["cmd"], entrada["desc"], installable))

            for bandera in entrada.get("flags", []):
                cmd_list.mount(FlagRow(bandera["flag"], bandera["desc"]))

    def watch_current(self, index: int) -> None:
        self._render_page(index)

    def action_next_tab(self) -> None:
        self.current = (self.current + 1) % len(self.nombres)

    def action_prev_tab(self) -> None:
        self.current = (self.current - 1) % len(self.nombres)


if __name__ == "__main__":
    CheatSheetApp().run()
