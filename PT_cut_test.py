import re


def pt_read(text):
    with open(text, 'r', encoding='utf-8') as file:
        txt_content = file.read()

    # 使用splitlines()并结合列表推导式，将连续的非空行视为一个段落
    paragraphs = [''.join(paragraph.splitlines()) for paragraph in txt_content.split('\n\n') if paragraph.strip()]

    return paragraphs


if __name__ == '__main__':
    paragraphs = pt_read('D:/Documents/老年人能力评估.txt')
    for paragraph in paragraphs:
        print(paragraph)
    print(len(paragraphs))
