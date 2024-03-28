from typing import List, Optional
from datetime import date
from database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy import DATE, String, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Artist(Base):
    __tablename__ = "artist"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    stage_name: Mapped[str] = mapped_column(String(50))
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    date_of_birth: Mapped[date]
    songs: Mapped[Optional[List["Song"]]] = relationship(back_populates="artist")

class Song(Base):
    __tablename__ = "song"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(30)) 
    producer: Mapped[str] = mapped_column(String(255))
    release_date: Mapped[date] = mapped_column(default=date.today)
    artist_id = mapped_column(ForeignKey("artist.id"))
    artist: Mapped[Artist] = relationship(back_populates="songs")
