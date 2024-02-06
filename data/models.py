from datetime import date
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from typing import Optional, List
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass

class Gender(Base):
    __tablename__ = "gender"

    gender_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    artists: Mapped[List["Artist"]] = relationship(back_populates="gender")

class Genre(Base):
    __tablename__ = "genre"

    genre_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    artists: Mapped[Optional[List["Artist"]]] = relationship(back_populates="genres")
    songs: Mapped[Optional[List["Song"]]] = relationship(back_populates="genre")
    albums: Mapped[Optional[List["Album"]]] = relationship(back_populates="genre")

# class Genre(Base):
#     __tablename__ = "genre"

#     genre_id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str]
#     artists: Mapped[List["Artist"]] = relationship(back_populates="genres")
#     songs: Mapped[List["Song"]] = relationship(back_populates="genre")
#     albums: Mapped[List["Album"]] = relationship(back_populates="genre")

class Artist(Base):
    __tablename__ = "artist"

    artist_id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str]
    stage_name: Mapped[str]
    gender_id = mapped_column(ForeignKey("gender.gender_id"))
    gender: Mapped[Gender] = relationship(back_populates="artists")
    email: Mapped[str]
    phone_number: Mapped[str]
    biography: Mapped[str]
    social_media_handles: Mapped[List["SocialMediaHandle"]] = relationship(back_populates="artist")
    genre_id: Mapped[Optional[int]] = mapped_column(ForeignKey("genre.genre_id"))
    genres: Mapped[Optional[List[Genre]]] = relationship(back_populates="artists")
    songs: Mapped[Optional[List["Song"]]] = relationship(back_populates="artist")
    albums: Mapped[Optional[List["Album"]]] = relationship(back_populates="artist")
    collaborations: Mapped[Optional[List["Collaboration"]]] = relationship(back_populates="artists", secondary="artist_collaboration")

class Song(Base):
    __tablename__ = "song"

    song_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    artist_id = mapped_column(ForeignKey("artist.artist_id"))
    artist: Mapped[Artist] = relationship(back_populates="songs")
    genre_id: Mapped[Optional[int]] = mapped_column(ForeignKey("genre.genre_id"))
    genre: Mapped[Optional[Genre]] = relationship(back_populates="songs")
    release_date: Mapped[date] 
    duration: Mapped[Optional[float]]
    collaboration: Mapped[Optional["Collaboration"]] = relationship(back_populates="song")

class Album(Base):
    __tablename__ = "album"

    album_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    artist_id = mapped_column(ForeignKey("artist.artist_id"))
    artist: Mapped[Artist] = relationship(back_populates="albums")
    genre_id: Mapped[Optional[int]] = mapped_column(ForeignKey("genre.genre_id"))
    genre: Mapped[Optional[Genre]] = relationship(back_populates="albums")
    release_date: Mapped[date]


class SocialMediaPlatform(Base):
    __tablename__ = "socialmediaplatform"

    social_media_platform_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    social_media_handles: Mapped[List["SocialMediaHandle"]] = relationship(back_populates="platform")

class SocialMediaHandle(Base):
    __tablename__ = "socialmediahandle"

    social_media_handle_id: Mapped[int] = mapped_column(primary_key=True)
    artist_id = mapped_column(ForeignKey("artist.artist_id"))
    artist: Mapped[Artist] = relationship(back_populates="social_media_handles")
    platform_id = mapped_column(ForeignKey("socialmediaplatform.social_media_platform_id"))
    platform: Mapped[SocialMediaPlatform] = relationship(back_populates="social_media_handles")
    handle: Mapped[str]

class Collaboration(Base):
    __tablename__ = "collaboration"

    collaboration_id: Mapped[int] = mapped_column(primary_key=True)
    song_id = mapped_column(ForeignKey("song.song_id"), unique=True)
    song: Mapped[Song] = relationship(back_populates="collaboration")
    artists: Mapped[List[Artist]] = relationship(back_populates="collaborations", secondary="artist_collaboration")


artist_collaboration = Table(
    "artistcollaborations",
    Base.metadata,
    Column("artist_id", ForeignKey("artist.artist_id"), primary_key=True),
    Column("collaboration_id", ForeignKey("collaboration.collaboration_id"), primary_key=True)
)