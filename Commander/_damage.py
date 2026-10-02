from . import _game

from mods_base import BaseOption, HiddenOption, KeybindType, keybind


options: list[BaseOption] = []
keybinds: list[KeybindType] = []


if _game.has_damage_numbers:
    _damage_numbers = HiddenOption[bool]("DamageNumbers", True)
    options.append(_damage_numbers)

    @keybind(
        identifier="Toggle Damage Numbers",
        key="Quote",
        description=(
            "In game, tap to hide or show the numbers that pop out of anything"
            " you damage."
        ),
    )
    def _toggle_keybind() -> None:
        _damage_numbers.value = not _damage_numbers.value
        _game.set_damage_numbers(_damage_numbers.value)
        _game.mod.save_settings()

        message = "On" if _damage_numbers.value else "Off"
        _game.popup(f"Damage Numbers: {message}")

    keybinds.append(_toggle_keybind)

    def on_enable() -> None:
        _game.set_damage_numbers(_damage_numbers.value)

    def on_disable() -> None:
        _game.set_damage_numbers(True)
