# radarbots.py
An unofficial package used to interact with the [Radar Bot Directory](https://radarbotdirectory.xyz) API

---

# Warning
This package requires you to have your bot approved on the Radar Bot Directory.

---

# Usage
```python
import radar
from discord.ext import commands
client = commands.Bot(command_prefix="!")
radar_client = radar.Client(client, "your radar bot directory token")

@client.event()
async def on_ready():
    print("The client is ready")
    radar_client.stats(len(client.guilds), 1)

client.run("your token goes here")
```

---

# Note
This package is not ready for production, bugs may occur.