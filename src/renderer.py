import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INTER_PATH = os.path.join(BASE_DIR, "assets", "fonts", "inter.ttf")
INTER_SEMI_BOLD = os.path.join(BASE_DIR, "assets", "fonts", "inter_semi_bold.ttf")
INTER_BOLD = os.path.join(BASE_DIR, "assets", "fonts", "inter_bold.ttf")

HEADER_FONT_SIZE = 36
BODY_FONT_SIZE = 16

HEADER_FONT = ImageFont.truetype(INTER_BOLD, HEADER_FONT_SIZE)
BODY_FONT = ImageFont.truetype(INTER_SEMI_BOLD, BODY_FONT_SIZE)

def load_icon(path, size):
    icon = Image.open(path)

    if icon.mode != "RGBA":
        icon = icon.convert("RGBA")

    return icon.resize(size)

QR_CODE_SIZE = (150, 150)
SMALL_ICON_SIZE = (25, 25)

QR_CODE = load_icon(os.path.join(BASE_DIR, "assets", "images", "qr_code.png"), QR_CODE_SIZE)
CODING_ICON = load_icon(os.path.join(BASE_DIR, "assets", "icons", "comment_code.png"), SMALL_ICON_SIZE)
    
PADDING = 5



def paste_icon(image, icon, x, y):
    image.paste(icon, (x, y), icon)

def draw_card(draw, image):
    

    paste_icon(image, QR_CODE, 5, 5)
    
    draw.multiline_text((226, 5), "Phillip\nSwann", anchor="ma", align="center", font=HEADER_FONT, fill="black", spacing=4)    
    draw.line([(160,93),(291,93)], fill="red")
    
    draw.rectangle([(160,102),(291,155)], fill="yellow")
    paste_icon(image, CODING_ICON, 165, 116)
    draw.line([(195,110),(195,148)], fill="black")
    draw.multiline_text((200,112), "Junior\nDeveloper", font=BODY_FONT, fill="black", spacing=0)

def render_dashboard():
    image = Image.new("RGB", (800, 480), "white") # TODO: Change to 296 x 160
    draw = ImageDraw.Draw(image)

    draw_card(draw, image)
    
    return image

if __name__ == "__main__":

    image = render_dashboard()
    image.save(os.path.join(BASE_DIR, "images", "output.png"))