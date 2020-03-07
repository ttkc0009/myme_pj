from redis import Redis
from myme_config import db_conf
from myme_common import dprint

dprint(db_conf)
connection = Redis(host=db_conf['host'], port=db_conf['port'], db=0)