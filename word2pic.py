import random
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from concurrent.futures import ThreadPoolExecutor


def generate_page(string, font, page_num, size=4):
    lenstr = len(string)
    flag = (page_num - 1) * 28 * 38
    img = Image.open('./src/background.png')
    draw = ImageDraw.Draw(img)
    for i in range(28):
        for j in range(38):
            if flag >= lenstr:
                break
            if string[flag] == '\n':
                flag += 1
                break
            draw.text((70 + random.random() * size / 2 + 25 * j, 83 + random.random() * size + i * 48),
                      string[flag], (0, 0, 0),
                      font=font)
            flag += 1
        if flag >= lenstr:
            break
    img.save(f"./result/{page_num}.png")
    # img.show()
    print(f'第{page_num}张')


def word2pic(string, ttf_path="./src/test.TTF", save_path="./result/", size=4, num_pages=1):
    font = ImageFont.truetype(ttf_path, 25)  # 设置字体
    with ThreadPoolExecutor() as executor:
        for i in range(1, num_pages + 1):
            executor.submit(generate_page, string, font, i, size)


if __name__ == "__main__":
    size = 4  # 整齐度
    txt_path = './Content.txt'  # 文档位置
    ttf_path = "src/李国夫手写体.TTF"  # 字体位置
    save_path = "./result/"  # 储存文件夹 若没有不会自动生成
    with open(txt_path, 'r', encoding='utf-8') as f:
        string = f.read()
    num_pages = (len(string) + 28 * 38 - 1) // (28 * 38)
    word2pic(string, ttf_path, save_path, size, num_pages)
