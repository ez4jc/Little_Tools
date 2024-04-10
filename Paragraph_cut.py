import re
import time
from tqdm import tqdm
from functools import wraps


# 定义timer
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


@func_timer
def main():
    # 正则表达式匹配指定的段落开头：\n后的数字+顿号，以及特定结尾模式
    regex = re.compile(
        r'(\n[一二三四五六七八九十]+、)'  # 开头的一、二、三、等等
        r'([\s\S]*?)'  # 中间的任意字符（懒惰匹配）
        r'(?=(\n[一二三四五六七八九十]+、|第\s*[\u4e00-\u9fa5]{1,3}\s*章|第\s*[\u4e00-\u9fa5]{1,3}\s*节|\n第\d{1,2}节|\n第\d{1,2}章|\n([\u4e00-\u9fa5]|[a-zA-Z]|\d){1,4}\n))',
        re.DOTALL
    )

    with open('D:/Documents/1/1.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    matches = regex.findall(content)

    with open('D:/Documents/2/output.txt', 'w', encoding='utf-8') as file:
        for match in tqdm(matches, desc="运行中："):
            paragraph = match[1].strip()  # 获取段落并去除多余的空白字符
            lines = paragraph.split('\n')  # 将段落按行分割

            # 如果行数在5到100之间且段落总字数少于5000，则写入文件
            if 4 < len(lines) < 100 and len(paragraph) < 5000:
                file.write(paragraph + '\n\n')  # 末尾加上两个换行符


if __name__ == '__main__':
    main()
