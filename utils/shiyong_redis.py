import redis

__author__ = "clz"

if __name__ == "__main__":
    redis_me = redis.Redis(host="127.0.0.1",port=6379,db=0)
    redis_me.set("yannuo","言诺")
    yan = redis_me.get("yannuo")
    print(yan.decode("utf-8"))
