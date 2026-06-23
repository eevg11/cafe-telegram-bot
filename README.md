# ☕ Async Telegram Cafe Bot

A modern, asynchronous Telegram bot for a local cafe. It features an interactive menu, a dynamic shopping cart system, and local data persistence using an SQLite database. 

This project demonstrates clean architecture, asynchronous programming with `aiogram 3`, and secure credential handling.

## 🚀 Features
* **Dynamic Menu:** Generates the cafe's menu and pricing directly from the SQLite database.
* **Smart Cart System:** Users can add items, view their cart with real-time total price calculation, and clear it using Inline Keyboards.
* **No Chat Spam:** Uses callback queries to update messages in place instead of flooding the chat.
* **Secure Configuration:** Sensitive data (API Tokens) is completely isolated using environment variables.

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **Framework:** Aiogram 3.x (Asynchronous Telegram Bot API)
* **Database:** SQLite3
* **Configuration:** Python-dotenv

## 📁 Project Structure
```text
coffee_bot/
│
├── database/
│   └── db.py          # Database connection and queries
│
├── handlers/
│   ├── common.py      # Basic commands (/start, main menu)
│   └── menu.py        # Menu browsing, cart logic, and checkout
│
├── keyboards/
│   └── inline_kb.py   # Inline keyboards & builders
│
├── .env.example       # Template for environment variables
├── bot.py             # Application entry point
└── requirements.txt   # Project dependencies

