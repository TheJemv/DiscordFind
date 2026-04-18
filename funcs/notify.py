import os
from typing import Optional

import aiohttp
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")
ME_ID = int(os.getenv("ME_ID", "0"))


async def _send_webhook(content: str):
    if not WEBHOOK_URL:
        print("WEBHOOK_URL vacío")
        return

    payload = {
        "content": content,
        "allowed_mentions": {"users": [str(ME_ID)]},  # solo permite ping a tu usuario
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(WEBHOOK_URL, json=payload) as resp:
            if resp.status >= 400:
                print("Webhook error:", resp.status, await resp.text())


async def notify_wa():
    print("Notifying wa")
    await _send_webhook("Se ha hecho un `$wa`")


async def notify_claim(claimed_name: str):
    print("Notifying claim")
    await _send_webhook(f"<@{ME_ID}> alguien reclamó **{claimed_name}**")
