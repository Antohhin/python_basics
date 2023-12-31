import httpx
from io import BytesIO
import random
from random import choice
from PIL import Image, ImageDraw, ImageFont

def draw_text_with_outline(draw, position, text, font, text_colour, outline_colour):
    x, y = position
    # Draw outline
    for adj in range(-1, 2):
        for ops in range(-1, 2):
            if adj != 0 or ops != 0:  # Avoid the center pixel
                draw.text((x+adj, y+ops), text, font=font, fill=outline_colour)
    draw.text(position, text, font=font, fill=text_colour)

def select_wm_colour(base_brightness) -> tuple:

    # stat = ImageStat.Stat(base)
    if base_brightness > 178:
        # Black text for lighter background
        text_colour = (0, 0, 0, 255)
        # text_colour = (1,223,1, 255) #toxic
    else:
        # White text for darker background
        text_colour = (255, 255, 255, 255)
    
    return text_colour

def calculate_corners(img_w: int, img_h: int, text_bbox: tuple, margin: int) -> list:
    # Estimate text size rely on font and text box
    # the (0, 0) is the starting position. return tuple (x1, y1, x2, y2)
    
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    # Choose a random corner for the text
    corners = [
        (margin, margin),  # Top-left
        (img_w - text_width - margin, margin),  # Top-right
        (margin, img_h - text_height - margin),  # Bottom-left
        (img_w - text_width - margin, img_h - text_height - margin)  # Bottom-right
    ]

    return corners

def draw_corner_watermark(
        image_url: str,
        text: str,
        text_size: int=14,
        margin: int=24,
        export_filename: str='new_meme.png'):
    
    res = httpx.get(image_url)
    bytes_res = BytesIO(res.content)
    with Image.open(bytes_res).convert("RGBA") as base:
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        try:
            fnt = ImageFont.truetype('Arial.ttf', text_size)
        except IOError:
            fnt = ImageFont.load_default()
        d = ImageDraw.Draw(txt)

        # calculate size of textbox
        text_bbox = d.textbbox((0, 0), text, font=fnt)
        # Choose a random corner for the text
        text_position = choice(calculate_corners(img_w=base.size[0], img_h=base.size[1], text_bbox=text_bbox, margin=margin))
        # average brightness of pixel check and switch between black/white
        base_brightness = sum(base.getpixel(text_position)[:3]) / 3
        text_colour = select_wm_colour(base_brightness)

        # Define outline colour (opposite of text colour for contrast)
        outline_colour = (0, 0, 0, 255) if text_colour == (255, 255, 255, 255) else (255, 255, 255, 255)
        
        # Draw text with outline
        draw_text_with_outline(d, text_position, text, fnt, text_colour, outline_colour)

        # overlay image of each other
        out = Image.alpha_composite(base, txt)
        # out.show()
        out.save(export_filename)


if __name__ == '__main__':

    image_url = "https://as.fishki.net/upload/post/2020/11/01/103861430/gallery/tn/694671836.jpg"
    text = "@ffmemesbot"
    # random.seed(33)
    # for i in range(4):
    image_urls =  [
    "https://api.memegen.link/images/ugandanknuck/~hspecial_characters~q/underscore__-dash--.png?width=800&token=g1oow9vw3dw5l1iy7a9q",
    "https://i.imgflip.com/8aph11.jpg",
    "https://i.imgflip.com/8as7x1.jpg",
    "https://i.imgflip.com/8apgr2.jpg",
    "https://i.imgflip.com/8aqt1h.jpg",
    # ""
    ]

    # Fetch and display the images
    for url in image_urls:
        tail = random.randint(1, 99)
        draw_corner_watermark(url, text, export_filename=f'new_img_x_{tail}.png')
