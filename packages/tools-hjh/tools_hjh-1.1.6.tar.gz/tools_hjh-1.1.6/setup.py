from setuptools import setup

setup (
    name='tools_hjh',
    version='1.1.6',
    author='HuaJunhao',
    author_email='1104388140@qq.com',
    install_requires=[
          'dbutils'
        , 'psycopg2'
        , 'pymysql'
        , 'cx_Oracle'
        , 'paramiko'
        , 'zipfile36'
        , 'crypto'
        , 'requests'
    ],
    packages=['tools_hjh']
)
