import gradio as gr

from util import lib_wordcloud, lib_jieba

from consts import *


def service_text2wc(
        text_file,
        text_lang,
        text_dict: str,
        background_color,
        margin,
        max_font_size,
        min_font_size,
        font_file,
        width,
        height,
        mask_image,
        mask_color,
        contour_width,
        contour_color,
):
    if not text_file:
        gr.Warning(f"请传入正确的文本文件！")
        return
    if margin < 0:
        gr.Warning(f"字体间隔配置不合法！")
        return
    if min_font_size < 0 or max_font_size < 0 or min_font_size > max_font_size:
        gr.Warning(f"字体大小配置不合法！")
        return

    try:
        with open(file=text_file.name, encoding="utf-8") as file:
            text = file.read()

        if text_lang == '中文':
            gr.Info(f"选择了中文，将使用Jieba库解析文本！")
            userdict_list = []
            if text_dict is not None:
                # userdict_list = map(lambda w: w.strip(), text_dict.split(", "))
                userdict_list = [w.strip() for w in text_dict.split(",")]
            text = lib_jieba.jieba_processing_txt(text, userdict_list)

        font_path = font_file.name if font_file else None

        if mask_image is not None:
            return lib_wordcloud.text2wordcount_mask(
                text,
                background_color,
                margin,
                min_font_size,
                max_font_size,
                font_path,
                mask_image,
                mask_color,
                contour_width,
                contour_color,
            )
        else:
            return lib_wordcloud.text2wordcount_normal(
                text,
                background_color,
                margin,
                min_font_size,
                max_font_size,
                font_path,
                width,
                height
            )
    except Exception as e:
        print(e)
        raise gr.Error("文本转词云图时，发生异常：" + str(e))


js = """
function createGradioAnimation() {
    var container = document.createElement('div');
    container.id = 'gradio-animation';
    container.style.fontSize = '2em';
    container.style.fontWeight = 'bold';
    container.style.textAlign = 'center';
    container.style.marginBottom = '20px';

    var text = '欢迎使用“词云转换器”!';
    for (var i = 0; i < text.length; i++) {
        (function(i){
            setTimeout(function(){
                var letter = document.createElement('span');
                letter.style.opacity = '0';
                letter.style.transition = 'opacity 0.5s';
                letter.innerText = text[i];

                container.appendChild(letter);

                setTimeout(function() {
                    letter.style.opacity = '1';
                }, 50);
            }, i * 200);
        })(i);
    }

    var gradioContainer = document.querySelector('.gradio-container');
    gradioContainer.insertBefore(container, gradioContainer.firstChild);

    return 'Animation created';
}
"""

with gr.Blocks(title="词云转换器", js=js) as iface:
    with gr.Row():
        with gr.Column():
            with gr.Group():
                with gr.Row():
                    input_text_file = gr.File(label="待处理的文本文件（必填）")
                    with gr.Column():
                        gr.Label(label="Tips", value="请传入正常可读的文本文件，如以.txt结尾的文档", color="#fee2e2")
                        gr.File(value=EXAMPLE_TEXT_FILE, label="文本文件的样例")
                        input_text_lang = gr.Radio(label="文本语言模式", choices=["中文", "英文"], value="中文")
                input_text_dict = gr.Textbox(label="自定义分词词典（可选）",
                                             info="中文模式使用，多个词之间用英文逗号分隔，例如'阿Ｑ, 孔乙己, 单四嫂子'")
            with gr.Tab("普通模式"):
                with gr.Row():
                    input_width = gr.Number(value=400, label="生成图像的宽", minimum=1)
                    input_height = gr.Number(value=200, label="生成图像的高", minimum=1)
                gr.Label(label="Tips", value="使用该模式时，记得清理掉“Mask模式”下的“Mask图像”", color="#fee2e2")
            with gr.Tab("Mask模式"):
                with gr.Row():
                    input_contour_width = gr.Number(value=3, label="轮廓线的粗细", minimum=0)
                    input_contour_color = gr.Textbox(value="steelblue", label="轮廓线的颜色")
                with gr.Row():
                    input_mask_image = gr.Image(label="Mask图像（决定词云的形状、颜色、宽高）")
                    input_mask_color = gr.Image(label="若传入该图，则词云的颜色由该图决定")
                # gr.Image(value=EXAMPLE_MASK_IMAGE_PATH, label="Mask图像的样例", interactive=False)
                gr.Gallery(value=[EXAMPLE_MASK_IMAGE_01, EXAMPLE_MASK_IMAGE_02, EXAMPLE_MASK_IMAGE_03, EXAMPLE_MASK_IMAGE_04],
                           label="Mask图像的样例", interactive=False)
        with gr.Column():
            with gr.Group():
                with gr.Row():
                    with gr.Group():
                        input_bg_color = gr.Textbox(value="white", label="词云图的背景色（默认为'white'）")
                        input_margin = gr.Number(value=2, label="字体间隔（默认为'2'）", minimum=0)
                        with gr.Row():
                            input_min_font_size = gr.Number(value=4, label="字体大小-最小值", minimum=1)
                            input_max_font_size = gr.Number(value=200, label="字体大小-最大值", minimum=4)
                    input_font_file = gr.File(label="词云图的字体文件（可选，如otf文件）")
                format_radio = gr.Radio(choices=["png", "jpeg", "webp", "bmp", "tiff"], label="词云图像格式",
                                        value="png")
            submit_button = gr.Button("开始处理", variant="primary")
            output_image = gr.Image(label="词云图", format="png")


    def fix_format(x):
        output_image.format = x
        return None


    format_radio.change(fn=fix_format, inputs=format_radio)

    submit_button.click(
        fn=service_text2wc,
        inputs=[
            input_text_file,
            input_text_lang,
            input_text_dict,
            input_bg_color,
            input_margin,
            input_max_font_size,
            input_min_font_size,
            input_font_file,
            input_width,
            input_height,
            input_mask_image,
            input_mask_color,
            input_contour_width,
            input_contour_color,
        ],
        outputs=output_image,
    )
