import random
from disnake.ext import commands
from core.consts import ACTIVITIES


sealbot = commands.InteractionBot(
    reload=False,
    test_guilds=None,
    activity=random.choice(ACTIVITIES),
)

# sealbot.load_extension("cogs")
