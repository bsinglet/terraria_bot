# terraria_bot
## Introduction and Purpose
This is an experiment with very simple botting. I chose Terraria as a starting platform for these experiments due it being resource inexpensive, having a simple UI, and still being rich enough in content to present genuine hurdles for a bot.

I've opted for a non-intrusive approach, using PyAutoGUI to send raw mouse and keyboard clicks. It would be much easier to extract information via reading process memory or intercepting traffic in local multiplayer mode, but those techniques are difficult to port from one game to the next. Additionally, while this project is for educational and research purposes only, it still needs to consider uses in future games where anti-cheat technologies would unjustly block it. I would like to transfer as much code and knowledge from this platform to other games in the future, so I've chosen methods that should bypass anti-cheat measures as much as possible.

## Use
The current state of this project has little utility, but it provides a good starting point for hobbyists. In fact, it would be fair to describe it as more of a Terraria macro-player than a bot at this point. In order to run it on your own system, simply do the following:
- Clone this repository to your system. 
- Install the Python 3 packages imported in `main.py`.
- Start Terraria on your system in Windowed mode.
  - Open a world of your choosing.
  - Make sure the character is using Smart Cursor mode.
  - Equip a pickaxe in hotkey slot 2 (or edit the constant in `main.py` accordingly.)
  - Optionally, equip a stack of torches in hotkey slot 5 (or edit the constant in `main.py` accordingly.)
- Execute the script.
- Watch the bot dig tunnels (and die often.)

## Coming Soon
I'm working on the following features to make this bot much more interesting:
- A range of new actions, such as jumping, digging in different directions, defensive moves, etc.
- Primitive vision to detect successful vs blocked movement.
- Computer vision with OpenCV to seek and take action on appropriate tiles.
- Drowning and water detection and avoidance.
