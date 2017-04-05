import os

import requests


def zhua_qu_index(index, name):
    print("开始抓贴" + str(index))
    param = {"kw":"汉服天下", "ie":"utf-8", "pn":index}
    r = requests.get("http://tieba.baidu.com/f", params=param)
    content_need = r.text
    dir_name = "D:/hanfuba/hanfutianxia/" + name
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    file_name = "/index" + str(index) + ".html"
    all_name = dir_name + file_name
    print(all_name)
    fileReader = open(all_name, "w", encoding="utf-8")
    fileReader.write(content_need)


if __name__ == "__main__":
    name = "index1_10000"
    print(name)
    for i in range(0, 450, 50):
        if(i % 10000 == 0):
            name = "index" + str(i) + "_" + str(i + 10000)
        zhua_qu_index(i, name)









