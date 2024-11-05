import pytz
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client
import asyncio

api_id = '7982046'
api_hash = '665da0bb262780d43f19791e954a680d'
session_string = 'BQAf70YAYd8m5X_2iA08dyZ4Om82Mw5ww14_JcJUJqtKBQEWwNGQlc_rYN2co_PR6_y9JLenaSaOwRA4EegP1sHGbSsHLST2Lnup5ScMJ901xnEWcWs0aOs8M9-pXxTIhTLubdoCFEUxbiX7Jl2_TRhiovnluZdspG-nC9sFGxESbe0YpavxNkdw7kPZjzSV5jzLHrj0WCfXKt1s26e8DczYAdcWA30AULDY_8CMDjExPXGpVBdwrvSn_gQ0_SH4Kc1F_5UGG6zEBABtG1i5SZ3PrpZZNIhnDb7IVULn9car0HHRM8gNFmdBmfs7R_zNEmT981zHadM4stqLBGCrU4i_ijVy3gAAAAFKLXutAA'

piro = Client("PiroModz", api_id=api_id, api_hash=api_hash, session_string=session_string)

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

print("Starting...Created By PiroHackz")
piro.run(update_profile_picture())