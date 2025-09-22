
from pyrogram import Client, filters
from pyrogram.types import Message
from RISHUCHATBOT import RISHUCHATBOT as app

@app.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    try:
        await message.react("👍")
    except Exception as e:
        print(f"Failed to react to message: {e}")
