from sqlalchemy import (
    Boolean,
    Column,
    INTEGER,
    TIMESTAMP,
    VARCHAR,

)
from sqlalchemy.sql.functions import (
    current_timestamp,
)

from db.db_connect import (
    Base,
    engine,
)


class Users(Base):  # Таблица пользователей
    __tablename__ = "users"

    id = Column(INTEGER, primary_key=True)
    first_name = Column(VARCHAR)
    last_name = Column(VARCHAR)
    created_at = Column(TIMESTAMP, nullable=False, default=current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, default=current_timestamp())
    status = Column(INTEGER, default=1)
    is_deleted = Column(Boolean, default=False)
    username = Column(VARCHAR)
    password = Column(VARCHAR)
    avatar = Column(VARCHAR)
    email = Column(VARCHAR)

    def __repr__(self):
        return f"{self.id}, {self.username}"
    

class Signals(Base):  # Таблица Signals(Постов)
    __tablename__ = "signals"

    id = Column(INTEGER, primary_key=True)
    author = Column(INTEGER)
    count_likes = Column(VARCHAR)
    signal = Column(VARCHAR)
    created_at = Column(TIMESTAMP, nullable=False, default=current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, default=current_timestamp())
    status = Column(INTEGER, default=1)
    is_deleted = Column(Boolean, default=False)


def __repr__(self):
    return f"{self.id}, {self.author}"


class Comments(Base):  # Таблица комментов
    __tablename__ = "comments"

    id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER)
    signal_id = Column(INTEGER)
    created_at = Column(TIMESTAMP, nullable=False, default=current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, default=current_timestamp())
    comment = Column(VARCHAR)
    is_deleted = Column(Boolean, default=False)

    def __repr__(self):
        return f"{self.id}, {self.signal_id}"


class Like(Base):  # Таблица лайков
    __tablename__ = "like"

    id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER)
    created_at = Column(TIMESTAMP, nullable=False, default=current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, default=current_timestamp())
    signal_id = Column(INTEGER)
    is_deleted = Column(Boolean, default=False)
    status = Column(Boolean)

    def __repr__(self):
        return f"{self.id}, {self.username}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
