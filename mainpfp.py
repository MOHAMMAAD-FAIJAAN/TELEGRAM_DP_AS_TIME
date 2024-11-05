import pytz
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client
import asyncio

api_id = 'your api id'
api_hash = 'your hash id'
session_string = 'your session id'

piro = Client("FAIZU", api_id=api_id, api_hash=api_hash, session_string=session_string)

def create_black_image_with_time():
    img = Image.new('RGB', (512, 512), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    pirohackz = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(pirohackz).strftime('%H:%M')
    font_large = ImageFont.truetype("font-PiroHackz.ttf", 220)
    bbox_large = draw.textbbox((0, 0), current_time, font=font_large)
    text_width_large, text_height_large = bbox_large[2] - bbox_large[0], bbox_large[3] - bbox_large[1]
    position_large = ((512 - text_width_large) // 2, (512 - text_height_large) // 2)
    draw.text(position_large, current_time, fill=(255, 255, 255), font=font_large)
    img_path = "profile_time.png"
    img.save(img_path)
    return img_path

async def update_profile_picture():
    async with piro:
        while True:
            # Wait until the start of the next minute
            tz = pytz.timezone('Asia/Kolkata')
            now = datetime.now(tz)
            wait_time = 60 - now.second
            await asyncio.sleep(wait_time)

            # Create and upload new profile image
            image_path = create_black_image_with_time()
            photos = [p async for p in piro.get_chat_photos("me")]
            if photos:
                await piro.delete_profile_photos(photos[0].file_id)
                if len(photos) > 1:
                    await piro.delete_profile_photos([p.file_id for p in photos[1:]])
            await piro.set_profile_photo(photo=image_path)

print("Starting...Created By MOHAMMAD-FAIJAAN")
piro.run(update_profile_picture())
