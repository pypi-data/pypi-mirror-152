# iyake_cn
# @Seon_Pan
# get key words from chinese content
# Example

from iyake_cn import get_S_t, get_key_words

txt = '这是一段简单的中文文本，可以从此提取出关键词，也可以换成其他文本，试试吧！'

df = get_S_t(txt)

words = get_key_words(df)

print(words)


# More Detail: https://blog.csdn.net/zohan134