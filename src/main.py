import sys
import os
import time
import logging
from logging.handlers import RotatingFileHandler

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "dashboard.log")

file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=1_000_000,  # 1MB
    backupCount=3        # keep 3 old logs
)

stream_handler = logging.StreamHandler()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[file_handler, stream_handler]
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WAVESHARE_LIB = os.path.join(BASE_DIR, "lib")

sys.path.append(WAVESHARE_LIB)

from waveshare_epd import epd7in5h

import renderer

logger = logging.getLogger(__name__)

def setup():
    epd = epd7in5h.EPD()
    epd.init()
    epd.Clear()
    time.sleep(1)
    return epd
    
def test_render():
    image = renderer.render_dashboard()
    image.save("dashboard.png")

def test_display():
    epd = setup()
    image = renderer.render_dashboard()
    epd.display(epd.getbuffer(image))

if __name__ == "__main__":
    epd = setup()
    logger.info("Dashboard Started")

    image = renderer.render_dashboard()
    epd.display(epd.getbuffer(image))
    
    epd.sleep()
    logger.info("Display Slept")