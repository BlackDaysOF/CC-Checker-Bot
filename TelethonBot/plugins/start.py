# By < @xditya >
# // @BotzHub //
from .. import bot
from telethon import events, Button

@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hello!",
                    buttons=[
                        [Button.url("ButtonUrl", url="https://t.me/xditya")],
                        [Button.inline("Inline Button",data="example")]
                    ])

@bot.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    await event.edit("You clicked a button!")
