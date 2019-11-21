

from Models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random 




engine = create_engine('oracle+cx_oracle://mustafa:1234@24.133.185.104:1521/XE')
Base = declarative_base()
