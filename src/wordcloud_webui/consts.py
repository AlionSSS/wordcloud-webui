import os
CURRENT_DIR = os.path.dirname(__file__)


# 样例文本
EXAMPLE_TEXT_FILE = os.path.join(CURRENT_DIR, "./resources/CalltoArms.txt")
# MASK图像样例
EXAMPLE_MASK_IMAGE_01 = os.path.join(CURRENT_DIR, "./resources/mask/parrot_mask.png")
EXAMPLE_MASK_IMAGE_02 = os.path.join(CURRENT_DIR, "./resources/mask/alice_color.png")
EXAMPLE_MASK_IMAGE_03 = os.path.join(CURRENT_DIR, "./resources/mask/alice_mask.png")
EXAMPLE_MASK_IMAGE_04 = os.path.join(CURRENT_DIR, "./resources/mask/LuXun_color.png")
# 分词器的 stop word 库
STOPWORDS_FILE = os.path.join(CURRENT_DIR, "./resources/stopwords_cn_en.txt")
# 词云图的默认字体
DEFAULT_FONT_PATH = os.path.join(CURRENT_DIR, "./resources/SourceHanSerifK-Light.otf")
