# Telegram Dictionary Bot

This is a simple Telegram bot that provides definitions for words, supports inline queries, and offers an administrator-only statistics feature.

## Features

- **Word Definitions**: Get definitions for any word by sending it to the bot.
- **`/start` Command**: Greets new users and automatically tracks unique user IDs.
- **`/help` Command**: Provides contact information for admin and owner.
- **Inline Mode**: Query word definitions directly from any chat by typing `@your_bot_username <word>`.
- **Admin Statistics (`/admin_stats`)**: (Admin-only) View the total count of unique users who have interacted with the bot.

## Setup and Installation

To run this bot, you'll need a Telegram Bot Token and an Admin User ID. Follow these steps:

1.  **Clone the Repository**:
    ```bash
    git clone <your_repository_url>
    cd telegram-dictionary-bot # Or whatever your repository name is
    ```

2.  **Install Dependencies**:
    Ensure you have Python 3.9+ installed. Then install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Environment Variables**:
    You need to set two environment variables:
    - `BOT_TOKEN`: Your Telegram Bot API token, obtained from BotFather.
    - `ADMIN_ID`: Your Telegram User ID, which will be the administrator for `/admin_stats`.

    **Example (for Linux/macOS)**:
    ```bash
    export BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
    export ADMIN_ID="YOUR_TELEGRAM_ADMIN_ID"
    ```
    (Replace `YOUR_TELEGRAM_BOT_TOKEN` and `YOUR_TELEGRAM_ADMIN_ID` with your actual values.)

    **For persistent environment variables**, you might add these lines to your `.bashrc`, `.zshrc`, or `.profile` file, or configure them through your hosting provider's interface.

4.  **Run the Bot**:
    ```bash
    python main.py
    ```
    The bot will start polling for updates.

## Usage

- **Start the bot**: Send `/start` to the bot.
- **Get a definition**: Send any word (e.g., `hello`) to the bot.
- **Get help**: Send `/help` to the bot.
- **Inline query**: In any chat, type `@your_bot_username <word>` (e.g., `@MyDictBot example`) to get a quick definition.
- **Admin stats**: (Only for `ADMIN_ID`) Send `/admin_stats` to the bot to see the total unique users.

## File Structure

- `main.py`: The main script containing the bot's logic.
- `requirements.txt`: Lists all Python dependencies.
- `users.txt`: Stores unique user IDs for statistics (automatically created).
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: This file, providing project information.

## Contact

- **Admin**: @EnglishDictionaryHelper
- **Owner/Advertising**: @mirjalolvalijonov
