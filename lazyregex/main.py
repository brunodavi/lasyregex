import re

from textual.app import App
from textual.containers import Container, Horizontal
from textual.css.query import DOMQuery
from textual.widgets import Input, Button, Label


class RegexSearch(App):
    CSS_PATH = 'css/regex_search.css'

    def compose(self):
        yield Input(placeholder='Regex', classes='regex')
        yield Input(placeholder='Text', classes='text')

        with Container(classes='box'):
            with Horizontal(classes='box_search'):
                yield Label('Matches: 0', classes='matches')

            yield Button('Search')

    def _get_inputs(self):
        for input in self.query('Input'):
            yield input.value

    def _uptade_matches(self, matches_count: int):
        label: Label = self.query_one('Label')
        label.update(f'Matches: {matches_count}')


    def on_button_pressed(self):
        [regex, text] = self._get_inputs()
        result = re.findall(regex, text)
        self._uptade_matches(len(result))

        self.bell()


def main():
    app = RegexSearch()
    app.run()


if __name__ == "__main__":
    main()
