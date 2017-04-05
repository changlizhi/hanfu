
import os
import bs4
from bs4 import BeautifulSoup
import json
import pymysql
import traceback
def read_one_html():
    path_parent = "E:/wendang/hanfuba/hanfubadetail"
    sons = os.listdir(path=path_parent)
    conn = pymysql.connect(host='localhost', user='root', passwd='admin', db='hanfuxin', port=3306, charset='utf8')
    cur = conn.cursor()
    for son in sons:
        path_son = path_parent + "/" + son
        htmls = os.listdir(path=path_son)
        for html in htmls:
            try:
                if html.find("read") == 0:  # 不是以read开头的文件名
                    path_html = path_son + "/" + html
                    html_file = open(path_html, encoding="utf-8")
                    soup_content = BeautifulSoup(html_file, "html.parser")
                    j_p_postlist = soup_content.find(id="j_p_postlist")
                    # 这里只有一个属性值得入库，我就把里面所有的数据循环出来
                    colum_dict = {}
                    if j_p_postlist is not None:
                        for child in j_p_postlist.children:
                            if isinstance(child, bs4.element.Tag):
                                if child.attrs.get("data-field") is not None:
                                    json_data = json.loads(child.attrs.get("data-field"))
                                    for attr in json_data:
                                        data_sun = json_data.get(attr)
                                        colum_dict.update(data_sun)
                                    con = str(colum_dict.get("content")).replace("\n", "").replace("\r", "").replace("　", "").replace(" ", "").replace("\t", "").replace("'", "\\'")
                                    insertdata = "insert into data_field(tie_id,user_id,user_name,comment_num,forum_id,thread_id,post_no,post_index,post_id,content)  values('" + html + "'," + (str(colum_dict.get("user_id")) if str(colum_dict.get("user_id")) != "None" else "0") + ",'" + str(colum_dict.get("user_name")) + "'," + str(colum_dict.get("comment_num")) + "," + str(colum_dict.get("forum_id")) + "," + str(colum_dict.get("thread_id")) + "," + str(colum_dict.get("post_no")) + "," + str(colum_dict.get("post_index")) + "," + str(colum_dict.get("post_id")) + ",'" + con + "');"
                                    if insertdata is not None:
                                        cur.execute(insertdata)
                    conn.commit()
                    html_file.close()
                    html_read = path_son + "/clz_" + html
                    os.rename(path_html, html_read)
                    print(path_html, "----------readed")
            except  :
                print(traceback.print_exc())
                print(path_son + "/" + html, "---->errord")
                html_file.close()
                html_read = path_son + "/clz_err_" + html
                os.rename(path_html, html_read)
                cur.close()
                conn.close()
                read_one_html()
if __name__ == "__main__":
    read_one_html()
    
