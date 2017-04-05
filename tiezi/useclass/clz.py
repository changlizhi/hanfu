'''
@author: me
'''

class use_init(object):
    def __init__(self,x,y):  # @DontTrace
        self.x = x
        self.y = y
    def nomal_fun(self):
        me = "changlizhi"
if __name__ == '__main__':
    uis = use_init(3,32)
    print(uis.y)
