# 🛡️ Telegram Admin Panel Template (Aiogram 3)

A simple, secure, and ready-to-use Admin Panel template for Telegram bots built with **Aiogram 3** and **SQLite**. 

Easily integrate a hidden admin menu into your existing bot to search and view user data without rewriting your core logic.

## ✨ Features
* **Secure Access:** Hidden `/admin` command accessible only to the specified `ADMIN_ID`.
* **User Lookup:** Search for users by their Telegram `@username`.
* **FSM Integration:** Uses Finite State Machine to wait for admin input without breaking your bot's main flow.
* **Robust Error Handling:** Gracefully handles cases where the user is not found in the database or has no username.
* **Plug-and-Play:** Designed to be easily copied and adapted into any existing Aiogram 3 project.

## 🛠 Tech Stack
* Python 3
* Aiogram 3
* SQLite3

## 🚀 How to Integrate (Step-by-Step)

To add this admin panel to your existing bot, follow these steps:

1. **Copy the files:** 
   Copy `admin_handlers.py` (or the admin parts of `handlers.py`), `admin_states.py` (or `states.py`), and the admin keyboards into your project.

2. **Add your Admin ID:**
   In your config file (e.g., `config.py`), add your personal Telegram ID:
   ```python
   ADMIN_ID = 123456789 # Replace with your actual Telegram ID
