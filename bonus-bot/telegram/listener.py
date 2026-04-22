from telethon import TelegramClient, events
from config import API_ID, API_HASH, CHANNEL_USERNAME
from processor.router import handle_message
from utils.logger import log

log("MESSAGE RECEIVED")
log(msg.message)

client = TelegramClient("session", API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHANNEL_USERNAME))
async def handler(event):
    msg = event.message

    # 🧪 DEBUG / VALIDATION LAYER (ADD HERE)
    print("\n📩 MESSAGE RECEIVED")
    print("Chat:", event.chat_id)
    print("Text:", msg.message)
    print("Has video:", bool(msg.video))

    # optional: early filter sanity check
    if not msg.message and not msg.video:
        print("⚠️ Empty or unsupported message type")
        return

    # pass to main pipeline
    await handle_message(msg)

def start_listener():
    client.start()
    print("Listening to Telegram channel...")
    client.run_until_disconnected()