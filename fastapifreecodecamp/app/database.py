from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time

# for local database
# sqlalchemyDatabaseUrl = 'mysql+pymysql://root:root@localhost:3306/application_layer_schema'
#for rds use this

sqlalchemyDatabaseUrl = 'postgresql://postgres:root@localhost/fastAPI'


while True:
    try:
        engine = create_engine(sqlalchemyDatabaseUrl, pool_pre_ping=True)
        print('database connection is successfull')
        break
    except Exception as e:
        print("database connection is failed because of ", e)
        time.sleep(5)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()