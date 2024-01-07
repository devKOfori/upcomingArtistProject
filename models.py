from datetime import date
from typing import List
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass

class SocialMedia(Base):
    __tablename__ = "socialmedia"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    url: Mapped[str]
    artist_id: Mapped[int] = mapped_column(ForeignKey("artist.id_artist"))
    artist: Mapped["Artist"] = relationship(back_populates="socialmedia")

class Gender(Base):
    __tablename__ = "gender"

    id_gender: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    artists: Mapped[List["Artist"]] = relationship(back_populates="gender")

class Artist(Base):
    __tablename__ = "artist"

    id_artist: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str]
    stage_name: Mapped[str]
    gender_id: Mapped[int] = mapped_column(ForeignKey("gender.id_gender"))
    gender: Mapped[Gender] = relationship(back_populates="artists")
    email_address: Mapped[str | None]
    phone: Mapped[str | None]
    biography: Mapped[str] = mapped_column(Text, deferred=True)
    social_media: Mapped[List[SocialMedia]] = relationship(back_populates="artists")
    songs: Mapped[List["Song"]] = relationship(back_populates="artist")
    collaboration: Mapped["Collaboration"] = relationship(back_populates="artists", secondary="CollaborationArtists")

class Album(Base):
    __tablename__ = "album"

    id_album: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    songs: Mapped[List["Song"]] = relationship(back_populates="album")

class Genre(Base):
    __tablename__ = "genre"

    id_genre: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    songs: Mapped[List["Song"] | None] = relationship(back_populates="genre")

class SongType(Base):
    __tablename__ = "songtype"

    id_song_type: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    songs: Mapped[List["Song"]] = relationship(back_populates="songtype")

class Song(Base):
    __tablename__ = "song"

    id_song: Mapped[int] = mapped_column(primary_key=True)
    artist: Mapped[Artist]  = relationship(back_populates="songs")
    title: Mapped[str] = mapped_column(String(255))
    release_date: Mapped[date | None] = mapped_column(Date)
    album_id: Mapped[int] = mapped_column(ForeignKey("album.id_album"))
    album: Mapped[Album | None] = relationship(back_populates="songs")
    songtype_id: Mapped[int] = mapped_column(ForeignKey("songtype.id_song_type"))
    songtype: Mapped[SongType| None] = relationship(back_populates="songs")
    collaboration: Mapped["Collaboration"] = relationship(back_populates="song")
    genre_id: Mapped[int] = mapped_column(ForeignKey("song.id_song"))
    genre: Mapped[int] = relationship(back_populates="songs")

class Collaboration(Base):
    __tablename__ = "collaboration"

    id_collaboration: Mapped[int] = mapped_column(primary_key=True)
    song_id: Mapped[int] = mapped_column(ForeignKey("song.id_song"))
    song: Mapped[Song] = relationship(back_populates="collaborations", single_parent=True)
    artists: Mapped[List[Artist]] = relationship(back_populates="collaboration", secondary="collaboration_artists")

collaboration_artists = Table(
    "collaboration_artists",
    Base.metadata, 
    Column("id_collaboration", ForeignKey("collaboration.id_collaboration"), primary_key=True, index=True),
    Column("id_artist", ForeignKey("artist.id_artist"), primary_key=True, index=True)
)
