# 🛡️ Telegram Admin Panel Template (Aiogram 3)

A simple, secure, and fully-featured Admin Panel template for Telegram bots built with **Aiogram 3** and **SQLite**. 

Easily integrate a hidden admin menu into your existing bot to manage users (view, edit, delete) without rewriting your core logic. Perfect for beginners looking to understand how to build admin interfaces, dynamic inline keyboards, and secure data manipulation.

## ✨ Features
* **User Registration:** Multi-step registration (Name, Surname) using a Finite State Machine (FSM).
* **Secure Access:** Hidden `/admin` command accessible only to the specified `ADMIN_ID`.
* **Dynamic Keyboards:** Automatically generates inline keyboards with all registered usernames using `InlineKeyboardBuilder`.
* **View User Data:** Display user ID, name, and surname by selecting them from a generated list.
* **Edit User Data:** Securely update a user's name or surname using dynamic inline buttons and FSM.
* **Delete User Data:** Remove users from the database with a secure Yes/No confirmation step.
* **Search Feature:** Find users quickly by entering their unique username.
* **Robust Error Handling:** Gracefully handles cases where users have no username or data is missing.

## 🚀 Roadmap
* [x] **View User Data:** Connect the generated inline buttons to callback data to display detailed user profiles.
* [x] **Delete Action:** Add ability to delete users directly from the admin panel.
* [x] **Edit Action:** Add ability to edit user data directly from the admin panel.
* [x] **Search Feature:** Add text-based search by username and user id.

## 🛠 Tech Stack
* Python 3
* Aiogram 3
* SQLite3

## 📁 Project Structure
* `main.py` — Entry point, bot startup, and database initialization.
* `app/handlers.py` — Handlers for commands, registration, and admin callbacks (CRUD logic).
* `app/database.py` — Database functions (SQL queries for registration, retrieval, updates, and deletion).
* `app/keyboards.py` — Reply and inline keyboards (including dynamic builders for user lists).
* `app/states.py` — FSM states for registration, deletion confirmation, editing, and searching.
* `assets/config.py` — Configuration file with the bot token, DB path, and admin ID.

## ⚙️ How to Run Locally
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install aiogram
