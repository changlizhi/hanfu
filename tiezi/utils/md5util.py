"""
Created on 2016年7月12日

@author: Administrator
"""
import hashlib

def md5_jiami(str):
    jia_mi = hashlib.md5()
    jia_mi.update(str.encode(encoding="utf_8", errors="strict"))
    return jia_mi.hexdigest()

if __name__ == "__main__":
    print(md5_jiami("10195508524713"))