import redis

r = redis.Redis(host='', prot=6379)
r.set('foo', 'Bar')

print(r.get('foo'))


# ##分割线## #
'''
带连接池的redis conn
'''

pool = redis.ConnectionPool(host='', port=6379)

r = redis.Redis(connection_pool=pool)
r.set('foo', 'Bar')

print(r.get('foo'))
