# 🛡️ Telegram Admin Panel Template (Aiogram 3)

A simple, secure, and evolving Admin Panel template for Telegram bots built with **Aiogram 3** and **SQLite**. 

Easily integrate a hidden admin menu into your existing bot to view registered users. Perfect for beginners looking to understand how to build admin interfaces and dynamic inline keyboards.

## ✨ Features
* **User Registration:** Multi-step registration (Name, Surname) using a Finite State Machine (FSM).
* **Secure Access:** Hidden `/admin` command accessible only to the specified `ADMIN_ID`.
* **Dynamic Keyboards:** Automatically generates an inline keyboard with all registered usernames using `InlineKeyboardBuilder`.
* **Database Integration:** Saves and retrieves user data (ID, username, name, surname) securely using SQLite.

## 🚀 Roadmap
* [X] **View User Data:** Connect the generated inline buttons to callback data to display detailed user profiles.
* [X] **Delete Action:** Add ability to delete users directly from the admin panel.
* [X] **Edit Action:** Add Ability to edit users data directly from admin panel.

## 🛠 Tech Stack
* Python 3
* Aiogram 3
* SQLite3

## 📁 Project Structure
* `main.py` — Entry point, bot startup, and database initialization.
* `app/handlers.py` — Handlers for commands, registration, and admin callbacks.
* `app/database.py` — Database functions (SQL queries for registration and data retrieval).
* `app/keyboards.py` — Reply and inline keyboards (including dynamic builder).
* `app/states.py` — FSM states for registration.
* `assets/config.py` — Configuration file with the bot token, DB path, and admin ID.

## ⚙️ How to Run Locally
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install aiogram
