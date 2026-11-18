# 🛡️ Registration & Admin Panel Bot

A Telegram bot with a multi-step user registration system and a secure admin panel for data management, built with Aiogram 3 and SQLite.

## 🛠 Tech Stack
* **Python 3**
* **Aiogram 3** — asynchronous framework for Telegram bots
* **SQLite3** — built-in database for secure user data storage

## ✨ Features
* **User Registration:** Multi-step registration using a Finite State Machine (FSM) to collect first name and surname.
* **Data Storage:** Automatically saves the user's Telegram ID, username, name, and surname to the database.
* **Admin Panel (`/admin`):** A hidden panel accessible only to the bot administrator (verified via `ADMIN_ID`).
* **Data Lookup:** Admins can search for user data by entering their Telegram username.
* **Robust Error Handling:** The bot gracefully handles cases where an admin searches for a non-existent user or a user has hidden their username.

## 📁 Project Structure
* `main.py` — Entry point, bot startup, and database initialization.
* `app/handlers.py` — Handlers for commands, messages, and admin callbacks.
* `app/database.py` — Database functions (SQL queries for registration and data retrieval).
* `app/keyboards.py` — Inline and reply keyboards.
* `app/states.py` — FSM states for registration and admin panel operations.
* `assets/config.py` — Configuration file with the bot token, DB path, and admin ID.

## ⚙️ How to Run Locally
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install aiogram
