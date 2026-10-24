class DevelopmentConfig():
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='john'
    MYSQL_PASSWORD='john'
    MYSQL_DB='api_utl'
    MYSQL_CURSORCLASS='Cursor'

config={
    'development':DevelopmentConfig
}