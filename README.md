
# Gotify Telegram Bot Reflector
A Gotify client that broadcast notifications to a specific Telegram Bot (user driven) thats talk to a specific Telegram user.


## Features
- Broadcast Gotify notifications to Telegram
- Filter Gotify application with notifications
- Receive notifications of multi gotify servers on same Telegram Bot


## Requirements
* Gotify deployment
* Gotify Client Token
* (_Optional_) Gotify App names for watch
* Telegram Bot Token [gen with @BotFather]
* Telegram Chat ID [for receive notifications]

## Environment Variables
To run this project, you will need to add the following environment variables.
| Variable | Default value | Description |
| -------- | ----- | ---------- |
| `GOTIFY_URL` | `127.0.0.1`  | Gotify address |
| `GOTIFY_PORT` | `80`  | Gotify port |
| `GOTIFY_WS_SEC` |  `True` | Using `WSS` or `WS` protocol for Gotify |
| `GOTIFY_HTTP_SEC` |  `True` | Using `HTTPS` or `HTTP` protocol for Gotify |
| `GOTIFY_APPS` |  `''` | List of reflected Gotify Applications (empty for all apps). Example: `HA,Proxmox,Uptime-Kuma` |
| `GOTIFY_CLIENT_TOKEN` |  `''` | Click `Create Client` in Gotify |
| `TELEGRAM_TOKEN` |  `''` | Create with __@BotFather__ |
| `TELEGRAM_CHAT_ID` |  `''` | Start bot, send any message and run `curl https://api.telegram.org/botTELEGRAM_TOKEN/getUpdates` |
