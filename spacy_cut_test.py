# -*- coding:utf-8 -*-
import spacy

# 加载中文模型
nlp = spacy.load("zh_core_web_sm")

# 假定您的文档位于当前目录下名为'document.txt'的文件
input_filepath = './1.txt'
output_filepath = './output.txt'

# 读取文档内容
with open(input_filepath, 'r', encoding='utf-8') as file:
    input_text = file.read()

# 使用spacy进行文本处理
doc = nlp(input_text)

# 将识别出的句子写入输出文件
with open(output_filepath, 'w', encoding='utf-8') as file:
    for s in doc.sents:
        file.write(str(s) + '\n')

print("句子分割完成，并已保存到文件")
