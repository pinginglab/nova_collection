import os

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DB_NAME', 'core_collection'),
        'USER': os.environ.get('MYSQL_DB_USER', 'root'),
        'PASSWORD': os.environ.get('MYSQL_DB_PSW', ''),
        'HOST': os.environ.get('MYSQL_DB_HOST', '172.16.236.1'),
        'PORT': os.environ.get('MYSQL_DB_PORT', 3306),
        'CONN_MAX_AGE': None,
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                    },
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        }
    },
}
