import os

__author__ = 'Administrator'


if __name__ == "__main__":
    file = open(os.path.join(os.path.dirname(__file__),"ww.txt"), encoding='utf-8')
    lis = []
    for line in file:
        lis.insert(0,str(line).split(","))
    for i in range(0,len(lis)):
        if i > 0:
            print(float(lis[i][1]) - float(lis[i-1][1]))
