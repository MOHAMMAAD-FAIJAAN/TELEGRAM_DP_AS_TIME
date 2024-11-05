# Profile Time Updater Bot

This bot updates your Telegram profile picture every minute with the current time on a black background. The script uses **Pyrogram** for Telegram interactions and **Pillow** for image processing.

## Prerequisites

- **Python 3.7** or higher
- A **Telegram** account with an **API ID**, **API Hash**, and a **Session String** (for authenticated access)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/TELEGRAM_DP_AS_TIME/profile-time-updater.git
cd profile-time-updater
```

### 2. Install Required Modules

Install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

Alternatively, you can install the required libraries manually:

```bash
pip install pyrogram pillow pytz
```

### 3. Get Your API ID, API Hash, and Session String

- **API ID** and **API Hash**: Obtain these by logging into [my.telegram.org](https://my.telegram.org) and creating a new app.
- **Session String**: Generate this by using [@StringsRobot](https://t.me/StringsRobot) on Telegram.

### 4. Font Setup

Make sure you have a font file named `your-font-name.ttf` in the same directory as the script. Update the font name in the script to match this file. This font will be used to display the time on the profile picture.

## Usage

1. Open the script and replace the placeholder values for `api_id`, `api_hash`, and `session_string` with your own credentials.
2. Update the font file name in the script to match your font of choice.
3. Run the script:

    ```bash
    python mainpfp.py
    ```

The bot will now update your profile picture every minute with the current time in the `Asia/Kolkata` timezone.

## Credits

Created by **MOHAMMAD-FAIJAAN**
