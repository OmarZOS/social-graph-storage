from nebula3.gclient.net import ConnectionPool
from nebula3.Config import Config

# define a config
config = Config()
config.max_connection_pool_size = 10
# init connection pool
connection_pool = ConnectionPool()
# if the given servers are ok, return true, else return false
ok = connection_pool.init([('127.0.0.1', 9669)], config)

# option 1 control the connection release yourself
# get session from the pool
session = connection_pool.get_session('root', 'nebula')

# select space
session.execute('USE nba')

# show tags
result = session.execute('SHOW TAGS')
print(result)

# release session
session.release()

# option 2 with session_context, session will be released automatically
with connection_pool.session_context('root', 'nebula') as session:
    session.execute('USE nba')
    result = session.execute('SHOW TAGS')
    print(result)

# close the pool
connection_pool.close()