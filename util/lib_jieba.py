import jieba
# jieba.enable_parallel(4)

from consts import *

# The function for processing text with Jieba
def jieba_processing_txt(text, userdict_list=['阿Ｑ', '孔乙己', '单四嫂子']):
    if userdict_list is not None:
        for word in userdict_list:
            jieba.add_word(word)

    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr = "/ ".join(seg_list)

    with open(STOPWORDS_FILE, encoding='utf-8') as f_stop:
        f_stop_text = f_stop.read()
        f_stop_seg_list = f_stop_text.splitlines()

    for myword in liststr.split('/'):
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)
    return ' '.join(mywordlist)