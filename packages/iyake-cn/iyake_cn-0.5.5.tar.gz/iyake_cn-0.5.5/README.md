# iyake_cn
# @Seon_Pan
# get key words from chinese content
# Example

from iyake_cn import get_S_t, get_key_words

txt = '����һ�μ򵥵������ı������ԴӴ���ȡ���ؼ��ʣ�Ҳ���Ի��������ı������԰ɣ�'

df = get_S_t(txt)

words = get_key_words(df)

print(words)


# More Detail: https://blog.csdn.net/zohan134