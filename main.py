WISHLIST = [
    "Bayonetta", 
    "Midna",
    "Zelda",
    "Akame",
    "Sonie",
    "Shadow",
]

import os
from dotenv import load_dotenv
import asyncio
import discord
load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    # client.on("message")
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.channel.id != int(os.getenv("TARGET_CHANNEL_ID", "0")):
            return
        if not message.embeds:
            return
        
        author_name = (message.embeds[0].to_dict().get('author', {}).get('name') or "")
        if any(w.lower() in author_name.lower() for w in WISHLIST):
            await message.components[0].children[0].click()
            await asyncio.sleep(0.1)
            await message.components[0].children[0].click()
            await asyncio.sleep(0.1)
            await message.components[0].children[0].click()
            await asyncio.sleep(0.1)
            await message.components[0].children[0].click()
            await asyncio.sleep(0.1)
            await message.components[0].children[0].click()

client = MyClient()
client.run(os.getenv("TOKEN"))