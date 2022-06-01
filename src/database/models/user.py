"""Database models."""

from flask_login import UserMixin
from sqlalchemy import Column, DateTime, Integer, String
from werkzeug.security import check_password_hash, generate_password_hash

from src.database import Base


class User(UserMixin, Base):
    """User account model."""
    __match_args__ = ('email', 'name')

    __tablename__ = 'flasklogin-users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=False)
    email = Column(String(40), unique=True, nullable=False)
    password = Column(
        String(200), primary_key=False, unique=False, nullable=False
    )
    created_on = Column(DateTime, index=False, unique=False, nullable=True)
    last_login = Column(DateTime, index=False, unique=False, nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.name)
