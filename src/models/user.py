import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, Boolean, DateTime, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text

from src.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        doc="Primary key: Universally Unique Identifier for the user.",
    )
    username = Column(
        String,
        unique=True,
        index=True,
        nullable=False,
        doc="Unique username for the user (used for login). Must have at least 4 characters.",
    )
    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False,
        doc="Unique email address of the user (used for communication).",
    )
    password = Column(
        String,
        nullable=False,
        doc="Hashed password for the user.",
    )
    first_name = Column(
        String(100),
        nullable=True,
        doc="First name of the user (optional).",
    )
    last_name = Column(
        String(100),
        nullable=True,
        doc="Last name of the user (optional).",
    )
    phone_number = Column(
        String,
        nullable=True,
        doc="Phone number of the user (optional).",
    )
    birth_date = Column(
        DateTime(timezone=True),
        nullable=True,
        doc="Birthdate of the user in DateTime format (optional).",
    )
    image = Column(
        String,
        nullable=True,
        doc="URL or path to the user's profile image (optional).",
    )
    is_active = Column(
        Boolean,
        default=True,
        server_default=text("TRUE"),
        doc="Flag indicating if the user account is active. Default is TRUE.",
    )
    created = Column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        server_default=text("CURRENT_TIMESTAMP"),
        doc="Timestamp when the user account was created. Set by the server by default.",
    )
    modified = Column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
        server_default=text("CURRENT_TIMESTAMP"),
        doc="Timestamp when the user account was last modified. Updates automatically.",
    )
    last_login = Column(
        DateTime(timezone=True),
        nullable=True,
        doc="Timestamp of the user's last login. Nullable until the first login.",
    )

    __table_args__ = (
        CheckConstraint(
            "birth_date <= current_timestamp",
            name="check_birth_date_not_in_future",
        ),
        CheckConstraint(
            "length(username) >= 4",
            name="check_username_min_length",
        ),
    )

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"

    def __str__(self):
        return f"<User(username={self.username}, email={self.email})>"
