class DevConfig:
    debug = True
    # Connection String for Oracle Database
    SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://mustafa:1234@24.133.185.104:1521/XE'
    SQLALCHEMY_ECHO = False  # Enable to print SQL query logs
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Keep it False for SQLAlchemy
    SQLALCHEMY_MAX_IDENTIFIER_LENGTH = 128
    SQLALCHEMY_IMPLICIT_RETURNING = True
