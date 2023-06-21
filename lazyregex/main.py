from textual.app import App
from textual.containers import Container, Horizontal
from textual.widgets import Input, Button, Label


class RegexSearch(App):
    CSS_PATH = 'css/regex_search.css'


    search_count = 0


    def compose(self):
        yield Input(placeholder='Regex')
        yield Input(placeholder='Text')

        with Container(classes='box'):
            with Horizontal(classes='box_search'):
                yield Label(f'Matches: {self.search_count}')

            yield Button('Search')


def main():
    app = RegexSearch()
    app.run()


if __name__ == "__main__":
    main()
