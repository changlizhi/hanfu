import os
def get_path_use(up_dir, down_dir):
    need_dir = ''
    if '' == down_dir:
        need_dir = up_dir + '/' + down_dir
    else:
        need_dir = up_dir
    dir_list = os.listdir(path=need_dir)
    ret = []
    for i in dir_list:
        ret.append(need_dir + '/' + i)
    return ret

if __name__ == '__main__':
    root_dir = 'D:/hanfuba'
    dirs = get_path_use(root_dir, 'hanfuba')
    for i in dirs:
        next_dir = get_path_use(root_dir, '')
        print(next_dir)
