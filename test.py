import redis
import json

jsonfile=open('config.json',encoding='utf-8')
jsonContent = jsonfile.read()
dbconfig = json.loads(jsonContent)

# r = redis.StrictRedis(host=dbconfig["host"], port=6379, password=dbconfig["passwd"], db=0)
# r.set('age', 123)
# ret = r.get('age')
# print(ret)

pool = redis.ConnectionPool(host=dbconfig["host"], port=6379, password=dbconfig["passwd"])
r = redis.StrictRedis(connection_pool=pool)

pipe = r.pipeline()
pipe.hset("hash_key","leizhu900516",8)
pipe.hset("hash_key","chenhuachao",9)
pipe.hset("hash_key","wanger",10)
result = pipe.execute()
print(result)