import os
from twts_api.repositories import DbConfig

def test_db_config_from_env():
    os.environ['dbconfig_host'] = 'distant-host'

    dbconfig = DbConfig.from_env()
    assert dbconfig.host == 'distant-host'
