from tiezi.mulu import muluindex

__author__ = 'Administrator'
import sys
import re


class leixing():
    def shuzi(self):
        vx = 1
        vy = 2
        print(vx)
        print(vy)
        del vx
        print(vx)
        print(vy)

    def fushu(self):
        vx = complex(3, 4)
        print(vx.imag)

    def zifu(self):  # 只会包含前下标。
        vx = "abcdefg"
        print(vx[1])  #b
        print(vx[-1])  #g
        print(vx[2:-1])  #cdef不包含最后一个
        print(vx[2:3])  #c
        print(vx[2:])  #包含最后一个
        print(vx[-1:])
        print(vx[-2:])
        print(vx[-2:-2])

    def liebiao(self):
        vx = ['abcd', 786, 2.23, 768, 'john', 70.2]
        vy = set(vx)
        vz = frozenset(vx)
        print(vx[3])
        print(type(vx))
        print(type(vy))
        print(type(vz))
        print(vx)
        print(vy)
        print(vz)
        print(type(repr(vx)))

    def unizifu(self):
        vx = u"言诺"
        vy = "this""is""str"  # 级联一个字符串。
        vz = "xxd"
        vz = "444"

        print(vx)
        print(vy)
        print(vz)
        print(vx.encode("utf8"))

    def ceshi_set(self):
        student = {"x", "y", "z", "x", "y"}
        teacher = set({"a", "b", "a", "z"})
        print(student ^ teacher)
        print(student | teacher)
        print(student - teacher)
        print(student & teacher)
        print(ord("9"))

    def ceshi_is(self):
        vx = 30
        vy = 50
        vz = 30
        vf, vv, vq = 12, 22, 33
        print(vf, vv, vq)
        # print(vx is vz)
        # print(id(vy))
        # print(id(vz))
        # print("\a")
        # vxx = "fff aas \n"
        # print(vxx)
        # print(repr(vxx))
        # print ("我叫 %s 今年 %d 岁!" .format('小明', 10))

    def shengchengqi(self, n):
        a, b, counter = 0, 1, 0
        while True:
            if (counter > n):
                return
            yield a
            print(a)
            a, b = b, a + b
            counter += 1

    def ceshi_shengchengqi(self, n):
        l = leixing()
        f = l.shengchengqi(n)
        for x in f:
            print(x)

    def bianli_zip(self):
        for q, v in zip([1, 2, 3], [4, 5, 6]):
            print(q * v)

    def budingchang(self, v, *x):
        print(v)
        for xx in x:
            print(xx)

    def dayin_sys(self):
        print(sys.path)

    def ceshi_re(self):
        restr = "[abc]"
        str = "a"
        str2 = "ka"
        str3 = re.match(restr, str)
        str4 = re.search(restr, str2)
        print(str3, str4)

    def ceshi_ren(self):
        restr = "[abc]{3,4}"
        restr2 = "[abc]+"
        restr2 = "[^abc]{1}"
        str1 = "d"
        str2 = "aaa"
        str3 = "aabbbb"
        str4 = "abb"

        print(re.match(restr2, str1), re.match(restr, str2), re.match(restr, str3), re.match(restr, str4))


if __name__ == "__main__":
    l = leixing()
    l.ceshi_ren()
    # print(dir(muluindex))