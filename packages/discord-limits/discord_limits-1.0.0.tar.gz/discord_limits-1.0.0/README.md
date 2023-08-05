[![Documentation Status](https://readthedocs.org/projects/discord-limits/badge/?version=latest)](https://discord-limits.readthedocs.io/en/latest/?badge=latest)

# discord_limits

### A simple library to asynchronously make API requests to Discord without having to worry about ratelimits.

<br>

### Currently this library has only been tested on Python 3.9

---

# Basic usage

```py
import discord_limits
import os

client = discord_limits.DiscordClient(os.environ.get('TOKEN'))

channel_id = 123456789012345678
await client.send_message(channel_id, content="Hello, world!")
```

---
### Requires:
- [aiolimiter](https://pypi.org/project/aiolimiter/)
- [aiohttp](https://pypi.org/project/aiohttp/)

---
### Based off of:
- [unbelipy](https://github.com/chrisdewa/unbelipy)
- [discord.py](https://github.com/Rapptz/discord.py)
