from .. import bot
from telethon import events

@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hello!")
