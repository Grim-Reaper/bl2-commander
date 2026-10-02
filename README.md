# Borderlands Commander

[**Discord**](https://discord.gg/54DE8uXvHE)&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;[**Donate**](https://streamlabs.com/mopioid/tip)

<br />

A [PythonSDK](https://bl-sdk.github.io/) mod for Borderlands series games that provides useful functionality while in-game:
* Saving and teleporting your position in the world
* Modifying game speed
* Configuring your own hotkeys to run console commands of your choice

Borderlands Commander supports the following games:
* Borderlands GOTY
* Borderlands 2
* Borderlands: The Pre-Sequel!
* Borderlands 3
* Tiny Tina's Assault on Dragon Keep
* Tiny Tina's Wonderlands

<br />

## Installation

See [PythonSDK Installation Instructions](https://bl-sdk.github.io/) for how to get started using SDK mods.

The latest version of `Commander.sdkmod` [can be found here](https://github.com/mopioid/Borderlands-Commander/releases).

<br />

## Usage

The built-in features of Borderlands Commander are operated using key inputs during gameplay. These key bindings may be configured in game via `Mods > Commander > Key Bindings`:

| Action| Default&nbsp;Key | Usage |
|-|-|-|
| Save&nbsp;Position | <kbd>Period</kbd> | <ul><li>Tap to save your current position</li><li>Hold and press a number key to save a position for that number</li></ul> |
| Restore&nbsp;Position | <kbd>Comma</kbd> | <ul><li>Tap to teleport to your saved position</li><li>Hold and press a number key to teleport to your saved position for that number</li></ul> |
| Select&nbsp;Position | None | <ul><li>Tap to pick the numbered position (1 to `Selectable Positions`) that a tap of `Save Position` or `Restore Position` uses</li><li>While this has no key, a tap of either uses your unnumbered position</li></ul> |
| Teleport&nbsp;to&nbsp;Spawn | <kbd>Slash</kbd> | <ul><li>Tap to cycle through points of interest in the map</li><li>Hold and press a number key to teleport to a specific point of interest</li><li>Hold this key, plus the key for `Restore Position`, plus a number key, to teleport to that co-op partner in your list of partners</li></ul> |
| Teleport&nbsp;Forward | <kbd>Up</kbd> | <ul><li>Tap to teleport forward by `Teleport Distance`, without respect to solid objects</li><li>Hold and press a number key to teleport forward greater distances (2 to 11 times as far)</li></ul> |
| Teleport&nbsp;Backward | <kbd>Down</kbd> | <ul><li>As `Teleport Forward`, but backward</li></ul> |
| Change&nbsp;Game&nbsp;Speed | <kbd>Backslash</kbd> | <ul><li>Hold and scroll up with the mousewheel to increase game speed</li><li>Hold and scroll down with the mousewheel to decrease game speed</li><li>Hold and click with the mousewheel to freeze time</li></ul> |
| Halve&nbsp;/&nbsp;Double&nbsp;/&nbsp;Reset&nbsp;Game&nbsp;Speed | None | <ul><li>Tap to change the game speed in one step, down to 1/32 or up to 32 times</li></ul> |
| Toggle&nbsp;World&nbsp;Freeze | None | <ul><li>Tap to freeze or unfreeze everything except the players</li></ul> |
| Toggle&nbsp;Damage&nbsp;Numbers | <kbd>Quote</kbd> | <ul><li>Tap to hide or show the damage numbers (Borderlands 2, The Pre-Sequel and Assault on Dragon Keep)</li></ul> |

A number key that is bound to one of the keys above (or to a custom command) still does its own job: it only acts as a position number while another of those keys is held.

<br />

## Custom Commands

Borderlands Commander allows you to create hotkeys for your own custom console commands.

Included with Commander are four default commands for each game:

### Borderlands 1, Borderlands 2, The Pre-Sequel!, Attack on Dragon Keep

| Action | Description |
|-|-|
| Toggle&nbsp;HUD | Enables/Disables the HUD overlay |
| Toggle&nbsp;Third&nbsp;Person | Switches between first person and third person camera modes |
| Quit&nbsp;Without&nbsp;Saving | Leave the current game session without saving, reverting to the last saved state |
| Respawn&nbsp;Enemies | Allow nearly every enemy in a map to respawn immediately |

### Borderlands 3, Wonderlands

| Action | Description |
|-|-|
| Teleport&nbsp;to&nbsp;Ping | Teleports you to the position of the last ping |
| Respawn&nbsp;Enemies | Allow nearly every enemy in a map to respawn immediately |
| Reload&nbsp;Map | Reloads the current map, more quickly than a save-quit |
| Quit&nbsp;Without&nbsp;Saving | Leave the current game session without saving, reverting to the last saved state |

### Adding Your Own

To edit your list of custom console commands, navigate to `Mods > Commander`, and click `Edit Custom Commands`. This will open a text file with your list of console commands.

Each console command is simply denoted with the name of the command, followed by a colon (<kbd>:</kbd>), followed by the actual command to run. Multiple commands are separated with two line breaks.

Once you have saved your commands, click the `Reload Custom Commands` button in Commander's options. To manage newly added commands in the keybinds sections, you must back out of Commander's options and re-open them.

If you would like to reset your list of custom commands to the default, simply delete the file and click Reload.

For a repository of useful custom commands in various games, [check out Commander's Discord server](https://discord.gg/54DE8uXvHE).

<br />

## Upgrading from Commander 2.x

Your 2.x settings are carried over on the first start: saved positions keep their numbers (position 1 also becomes your unnumbered position), your custom commands move into `Commander.txt`, and your key bindings stay as they were. To keep using positions the 2.x way, give `Select Position` a key: taps of `Save Position` and `Restore Position` then use the position it selected.

<br />

## Other Options

| Option | Description |
|-|-|
| Teleport&nbsp;Distance | How far a tap of `Teleport Forward` or `Teleport Backward` moves you (250 to 25000 units) |
| Selectable&nbsp;Positions | How many numbered positions `Select Position` cycles through (1 to 9) |
| Edit&nbsp;Custom&nbsp;Commands | Open your `Commander.txt` file to edit your custom commands |
| Reload&nbsp;Custom&nbsp;Commands | Tell Commander to reload your `Commander.txt` after you have edited it |
| Client&nbsp;Teleporting | Whether co-op partners who join your game may use Commander to teleport (they must also be running Commander) |
| Client&nbsp;Speed&nbsp;Permissions | Whether Co-op partners who join your game cannot adjust the game speed or freeze the world |
