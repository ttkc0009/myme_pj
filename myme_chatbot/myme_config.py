import json

debug = None
db_conf = None

with open('config.json', 'r') as f:
    conf_data = json.load(f)
    # debug mode
    debug = conf_data['debug_mode']
    # database setting
    db_conf = conf_data['db_conf']
