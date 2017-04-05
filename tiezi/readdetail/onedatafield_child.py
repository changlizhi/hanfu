
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
                if html.find("read") != 0:  # 不是以read开头的文件名
                    path_html = path_son + "/" + html
                    html_file = open(path_html, encoding="utf-8")
                    soup_content = BeautifulSoup(html_file, "html.parser")
                    j_p_postlist = soup_content.find(id="j_p_postlist")
                    # 这里只有一个属性值得入库，我就把里面所有的数据循环出来
                    louceng = 0
                    insert_childelement_sql = ""
                    insert_childelement_sql_before = "insert into childelement(tie_id,louceng,neirong)values('" + html + "',"
                    
                    if j_p_postlist is not None:
                        for child in j_p_postlist.children:
                            datafield_name_list = ["tie_id"]
                            datafield_value_list = [html]
                            if isinstance(child, bs4.element.Tag):
                                if child.attrs.get("data-field") is not None:
                                    json_data = json.loads(child.attrs.get("data-field"))
                                    lie_num = 0
                                    for attr in json_data:
                                        data_sun = json_data.get(attr)
                                        if data_sun.get("post_no") is not None:
                                            louceng = data_sun.get("post_no")
                                            insert_childelement_sql = insert_childelement_sql_before + str(louceng)
                                        for att in data_sun:
                                            lie_num = lie_num + 1
                                            datafield_name_list.append("lie_" + str(lie_num))
                                            datafield_value_list.append(att + ":" + str(data_sun.get(att)))
                                    columns = str(tuple(datafield_name_list))
                                    columns = columns.replace("'", "")
                                    insertdata = "insert into datafield" + columns + "  values" + str(tuple(datafield_value_list)) + ";"
                                    cur.execute(insertdata)
                                for sunzi in child.children:
                                    str_sunzi = str(sunzi).replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "")
                                    if len(str_sunzi) > 1 :
                                        insertchild = insert_childelement_sql + ",'" + str_sunzi.replace("'", "") + "');"
                                        
                                        cur.execute(insertchild)
                    conn.commit()
                    html_file.close()
                    html_read = path_son + "/read_" + html
                    os.rename(path_html, html_read)
                    print(path_html, "----------readed")
            except :
                print(traceback.print_exc())
                print(path_son + "/" + html, "---->errord")
                html_file.close()
                html_read = path_son + "/read_err_" + html
                os.rename(path_html, html_read)
                cur.close()
                conn.close()
                read_one_html()
if __name__ == "__main__":
    read_one_html()
    
