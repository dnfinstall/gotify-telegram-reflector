from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from settings import config
import logging
import asyncio
import websockets
import json
import signal
import sys


# Service Methods


def sigterm_handler(sig, frame):
    logging.info(f"Received signal {sig}. Exiting gracefully...")
    sys.exit(0)


signal.signal(signal.SIGTERM, sigterm_handler)
dispatcher = Dispatcher()


# Gotify Web Socket Methods


async def message_handler(websocket, bot: Bot) -> None:
    async for message in websocket:
        message = json.loads(message)
        logging.info(f"Gotify message: {message}")

        if not config.GOTIFY_DENY_APPS or (
            message["title"] not in config.GOTIFY_DENY_APPS.split(",")
        ):
            logging.info(
                f"Sending message to telegram: [{message["title"]}] {message["message"]}"
            )
            await bot.send_message(
                config.TELEGRAM_CHAT_ID,
                f"{message["title"]}: {message["message"]}",
            )


async def websocket_gotify(bot: Bot) -> None:
    logging.info("Starting Gotify Websocket...")
    websocket_resource_url = f"{"wss" if config.GOTIFY_WS_SEC else "ws"}://{config.GOTIFY_URL}:{config.GOTIFY_PORT}/stream?token={config.GOTIFY_CLIENT_TOKEN}"
    async with websockets.connect(websocket_resource_url) as websocket:
        logging.info(
            f"Connected to Gotify Websocket: {config.GOTIFY_URL}:{config.GOTIFY_PORT}"
        )
        await message_handler(websocket, bot)


# Telegram Bot Methods


@dispatcher.message(CommandStart())
async def send_welcome(message: types.Message):
    """Send a message when the command /start is issued."""
    logging.info(f"Welcome message to: @{message.chat.username}<{message.chat.id}>")
    await message.reply("Hi! \nI'm Gotify Bot")


async def main() -> None:
    telegram_bot = Bot(token=config.TELEGRAM_TOKEN)

    gotify_task = asyncio.create_task(
        websocket_gotify(
            bot=telegram_bot,
        )
    )
    bot_task = asyncio.create_task(
        dispatcher.start_polling(telegram_bot, handle_signals=False)
    )
    await asyncio.gather(gotify_task, bot_task)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped by user")
