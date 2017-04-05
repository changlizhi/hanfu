import os
if __name__ == "__main__":
    path_parent = "E:/wendang/hanfuba/hanfubadetail/100001_101001/readed"
    htmls = os.listdir(path=path_parent)
    for html in htmls:
        repla = html.replace("clz_", "")
        dir = path_parent + "/" + html
        dir_new = path_parent + "/" + repla
        print(dir + '--->' + dir_new)
        os.rename(dir,dir_new)
        
        
