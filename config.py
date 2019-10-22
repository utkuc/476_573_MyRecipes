class DevConfig:
    debug = True
    # Connection String for Oracle Database
    SQLALCHEMY_DATABASE_URI = "oracle+cx_oracle://db_admin:123456789@localhost:1521/orcl"
    SQLALCHEMY_ECHO = False  # Enable to print SQL query logs
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Keep it False for SQLAlchemy
    SQLALCHEMY_MAX_IDENTIFIER_LENGTH = 128
    SQLALCHEMY_IMPLICIT_RETURNING = True
