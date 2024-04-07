import re
from functools import wraps
import time
import os
from tqdm import tqdm


def batch_file(path, file_list):
    for file in os.listdir(path):
        fs = os.path.join(path, file)
        if os.path.isfile(fs):      # 如果是文件
            file_list.append(fs)
        elif os.path.isdir(fs):     # 文件夹
            batch_file(fs, file_list)
    return file_list


def func_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        print('[Function: {name} start...]'.format(name=function.__name__))
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print('[Function: {name} finished, spent time: {time:.2f}s]'.format(name=function.__name__, time=t1 - t0))
        return result
    return function_timer


def count_chinese_chars(text):
    """计数文本中的汉字数量"""
    chinese_char_pattern = re.compile(r'[^\u4e00-\u9fa5]')
    filtered_text = re.sub(chinese_char_pattern, '', text)
    return len(filtered_text)


def pt_read(text):
    with open(text, 'r', encoding='utf-8') as file:
        txt_content = file.read()

    # 使用splitlines()并结合列表推导式，将连续的非空行视为一个段落
    # paragraphs = [''.join(paragraph.splitlines()) for paragraph in txt_content.split('\n\n') if paragraph.strip()]
    paragraphs = [paragraph for paragraph in ["".join(paragraph.splitlines()) for paragraph in txt_content.split('\n\n') if paragraph.strip()]
                  if count_chinese_chars(paragraph) >= 35]

    return paragraphs


def pt_cut():
    file_list = []
    path = r'D:\Documents\2'
    file_path = batch_file(path=path, file_list=file_list)
    for path in file_path:
        profession_text_connect = open(path, encoding='utf-8').readlines()
        f = open(r'D:\Documents\output\2.txt', 'a', encoding='utf-8')
        keywords = ["简述", "试分析", "试述"]
        for i in tqdm(profession_text_connect):
            i = re.sub(r'\.\s*[\d[.]]+\s*\n\s*\n*', r'.\n', i)
            i = re.sub(r':\s*\n\s*\n*', r':\n', i)
            i = re.sub(r'\n(?![\d[.]]+\s).{1,100}\n', r'', i, flags=re.DOTALL)
            i = re.sub(r'\s*.\s*\?\s*\n', r'', i)       #
            i = re.sub(r'\n\s*\n*(\(\d+\))', r'\n\1', i)   #
            for keyword in keywords:
                i = re.sub(fr'\n{keyword}[^]*?\n', r'', i, flags=re.DOTALL)


            f.write(i + '\n')
        f.close()


if __name__ == '__main__':
    # txt = "是。\n\n\n1.saawdas"
    # print(txt)
    # i = re.sub(r'\.(\s*\n){2,}(\d[.])', r'.\n', txt)
    # print(i)
    i = "是。\n\n\n1.sss"
    print(i)
    i = re.sub(r'\.\s*[\d[.]]+\s*\n\s*\n*', r'.\n', i)
    print("这是结果：\n", i)
    # i = "是\n\n\n(1)"
    # print(i)
    # i = re.sub(r'\n\s*\n*(\(\d+\))', r'\n\1', i)
    # print(i)
    # pt_cut()
    text = """
    1. This is a sentence.\n\n\n2. This is another sentence.\n\n\n3. This is yet another sentence.\n\n\n
    """

    # 将1个或更多的换行符替换为一个换行符
    pattern = re.compile("\.\n{2,}(\d+\.)")
    new_text = re.sub(pattern, '.\n\g<1>', text)

    print(new_text)
