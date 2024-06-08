from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image

from consts import *


def text2wordcount_normal(
        text: str,
        background_color: str = "white",
        margin=2,
        min_font_size=4,
        max_font_size=200,
        font_path=None,
        width: int = 400,
        height: int = 200,
):
    if not background_color or "" == str(background_color).strip():
        background_color = "white"
    if not min_font_size or min_font_size < 1:
        min_font_size = 4
    if not max_font_size or max_font_size < 4:
        max_font_size = 200
    if not font_path or "" == str(font_path).strip():
        font_path = DEFAULT_FONT_PATH
    if not width or width < 1:
        width = 400
    if not height or height < 1:
        height = 200

        # Generate a word cloud image
    wordcloud = WordCloud(
        font_path=font_path,
        width=width, height=height, background_color=background_color,
        max_words=2000,
        margin=margin, min_font_size=min_font_size, max_font_size=max_font_size,
        random_state=42
    ).generate(text)
    return wordcloud.to_image()


def text2wordcount_mask(
        text: str,
        background_color: str = "white",
        margin=2,
        min_font_size=4,
        max_font_size=200,
        font_path=None,
        mask_image=None,
        mask_color=None,
        contour_width=3,
        contour_color="steelblue",
):
    if not background_color or "" == str(background_color).strip():
        background_color = "white"
    if not min_font_size or min_font_size < 1:
        min_font_size = 4
    if not max_font_size or max_font_size < 4:
        max_font_size = 200
    if not font_path or "" == str(font_path).strip():
        font_path = DEFAULT_FONT_PATH
    if not contour_width or contour_width < 0:
        contour_width = 3
    if not contour_color or "" == str(contour_color).strip():
        contour_color = "steelblue"

    # mask_color
    if mask_color is not None:
        image_colors = ImageColorGenerator(mask_color, True)
    else:
        image_colors = ImageColorGenerator(mask_image, True)

    # Generate a word cloud image
    wordcloud = WordCloud(
        font_path=font_path,
        mask=mask_image,
        background_color=background_color,
        color_func=image_colors,
        contour_width=contour_width,
        contour_color=contour_color,
        max_words=2000,
        margin=margin, min_font_size=min_font_size, max_font_size=max_font_size,
        random_state=42
    ).generate(text)

    return wordcloud.to_image()