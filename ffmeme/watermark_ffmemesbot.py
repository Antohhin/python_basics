import httpx
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont

# res = httpx.get("https://cdn4.cdn-telegram.org/file/eO_mnYIczlZblniCmBmpeHzibPnz4rBFkaVKSuIX4Lb3RPNCVMvVT9oQtqqLreaG0uasLp-Qs9yqNbHiUkwcc8ji4OE_nK6NPKzAdePbjCvQQLix0_DXXCyrw53UeRX8C4KDLl14rCtGHC4YYY9yH1YrW4PJBsJF9O9TyYIB0bjFW2CJSe6c7FUhbvbzzCKpZUdxUVsc64W9jb4XsAhywK-q0SsdGqDWeojqG4L03JbIGuneJNyvnQstyI5U4x-1umZH5FIsXutfcoVdKwWEXZG047lWlmhaGLkZbifoZVCkJbk8AAmSTReflGoB6NB4MCjj3FJZjFc1HusZ5zt3dg.jpg")
res = httpx.get("https://as.fishki.net/upload/post/2020/11/01/103861430/gallery/tn/694671836.jpg")
img = Image.open(BytesIO(res.content))
print(BytesIO(res.content))
# img = Image.open(res.content)

img = img.convert("RGBA")

# Display the image
# img.show()

# Create drawable canvas
draw = ImageDraw.Draw(img)
text = "@ffmemesbot"
font = ImageFont.load_default()#.font_variant(size=30)

draw.textsize(text, font=font)
width, height = draw.textsize(text, font=font)

# Define watermark label

# Load default font, set size to 30 (You might need to specify full path to a ttf font file if you want to use custom font)

# Calculate text size and position
x, y = img.size
text_x = x - width - 10  # 10 pixels margin from right
text_y = y - height - 10  # 10 pixels margin from bottom

# Apply watermark
draw.text((text_x, text_y), text, fill=(255,255,255,128), font=font)
# Display the image
img.show()