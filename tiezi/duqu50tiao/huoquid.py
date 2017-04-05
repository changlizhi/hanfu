# encoding =utf-8
from _io import open
from os.path import os
from urllib.request import Request
import pymysql
from bs4 import BeautifulSoup
import json

def get_dir_list(base_dir, son_dir):
    path_use = os.path.join(base_dir, son_dir)
    ret = os.listdir(path=path_use)
    return ret
    

if __name__ == '__main__':
    fileDir = 'D:/hanfuba/hanfutianxia'
    ziMuLu = os.listdir(path=fileDir)
    for i in ziMuLu:
        sunDir = fileDir + '/' + i
        sunMuLu = os.listdir(path=sunDir)
        conn = pymysql.connect(host='localhost', user='root', passwd='admin', db='hanfuxin', port=3306, charset='utf8')
        cur = conn.cursor()
        for j in sunMuLu:
            htmlDir = sunDir + '/' + j
            htmlFile = open(htmlDir, encoding='utf-8')
            suo_you_nei_rong = str(htmlFile.readlines())
            soup_all = BeautifulSoup(suo_you_nei_rong, 'html.parser')
            
            all_li_need = soup_all.findAll(name="li", attrs={'class':" j_thread_list clearfix"})
            
            for k in all_li_need :
                str_data = k.get("data-field")
                data_clean = str_data.replace("\\'", "")
                data_json = json.dumps(data_clean, sort_keys=True)
                
                data_json_obj = json.JSONDecoder().decode(data_json)
                data_json_obj_second = json.JSONDecoder().decode(data_json_obj)
                idone = str(data_json_obj_second["id"])
                insert_id_sql = "insert into hanfutianxia(id) values('" + idone + "')"
                cur.execute(insert_id_sql)
            conn.commit()
        cur.close()
        conn.close()












