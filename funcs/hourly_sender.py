import os
import asyncio
from dotenv import load_dotenv

from funcs.notify import notify_wa

load_dotenv()
TARGET_CHANNEL_ID = int(os.getenv("TARGET_CHANNEL_ID", "0"))
TIMES_PER_HOUR = 8
MSG = "$wa"

async def hourly_sender(client):
    print("Hourly sender started")
    while True:
        channel = client.get_channel(TARGET_CHANNEL_ID)
        if channel:
            for _ in range(TIMES_PER_HOUR):
                await channel.send(MSG)
                await asyncio.sleep(1)

        await notify_wa()
        await asyncio.sleep(3600)