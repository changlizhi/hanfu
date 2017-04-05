# encoding=utf-8 
import pymysql
import requests
import os
import re
from utils import changliang
def create_conn(num):
    # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
    conn = pymysql.connect(host='localhost', user='root', passwd='admin', db='hanfuxin', port=3306, charset='utf8')
    cur = conn.cursor()
    select_str = 'select * from hanfutianxia t where t.yeshu is null order by t.seq asc limit 1000'

    print(select_str)
    cur.execute(select_str)
    data = cur.fetchall()
    for d in data:
        print(d[2])
        ye_shu = create_requests(d[0], num)
        update_str = 'update hanfutianxia t set t.yeshu = ' + str(ye_shu) + ' where t.id=\'' + d[0] + '\''
        cur.execute(update_str)
        conn.commit()
    cur.close()
    conn.close()







def create_requests(id, num):
    tie_zi_url = 'http://tieba.baidu.com/p/' + id
    print(tie_zi_url)
    num_dir = num + 1000
    dir_name = 'D:/hanfuba/hanfutianxiaDetail/' + str(num) + '_' + str(num_dir) + '/'
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    print(1)
    r = requests.get(tie_zi_url)
    print(2)
    content_need = r.text
    if content_need.find('l_reply_num') != -1:
        ye_shu = get_ye_shu(content_need)
        print(ye_shu)
        file_name = dir_name + id + '_' + '1' + '.html'  # 现在就只抓取第一页的数据把页数返回留在数据库后期来补充
        fileReader = open(file_name, 'w', encoding='utf-8')
        fileReader.write(content_need)
        return ye_shu
    else:
        print(changliang.tie_ba_404)
        return 0


def get_ye_shu(content_need):
    index_of_ye_shu = content_need.index('l_reply_num')
    str_ye_shu_all = content_need[index_of_ye_shu:index_of_ye_shu + 140]
    str_ye_shu = str_ye_shu_all[str_ye_shu_all.index('red">'):str_ye_shu_all.index('页')]
    ye_shu = list(set(re.findall(r'\d*', str_ye_shu)))[1]
    return ye_shu

def di_gui():
    try:
        for i in range(0, 400, 1):
            create_conn(i)
    except:
        di_gui()
if __name__ == "__main__":
    di_gui()
    
