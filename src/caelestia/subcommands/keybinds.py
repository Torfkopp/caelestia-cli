import json
import subprocess
from argparse import Namespace

from caelestia.utils.paths import cli_data_dir

class Command:
    args: Namespace

    def __init__(self, args: Namespace) -> None:
        self.args = args

    def run(self) -> None:
        if self.args.picker:
            keybinds = (cli_data_dir / "keybinds.txt").read_text()
            subprocess.check_output(
                ["fuzzel", "--dmenu", "--placeholder=Type to search keybinds"], input=keybinds, text=True)
        elif self.args.generate:
            self.generate_list()
        else:
            print((cli_data_dir / "keybinds.txt").read_text(), end="")

    def generate_list(self):
        keybinds = json.loads((cli_data_dir / "keybinds/keybinds.json").read_text())
        translation = json.loads((cli_data_dir / "keybinds/key_translation.json").read_text())

        def key_replace(s):
            for before, after in translation.items():
                s = s.replace(before, after)
            return s.replace("+", " + ")

        keys = ""
        for category, binds in keybinds.items():
            for desc, key in binds.items():
                keys += key_replace(key).ljust(15) + " | " + category.ljust(15) + " | " + desc + "\n"

        (cli_data_dir / "keybinds.txt").write_text(keys)

