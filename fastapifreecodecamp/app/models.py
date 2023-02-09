from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String
from sqlalchemy.sql.expression import text
from app.database import Base

class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    published = Column(Boolean, server_default = "TRUE")
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default = text('now()'))


