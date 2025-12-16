

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import Mapped, mapped_column

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


class Earthquake(db.Model):
    __tablename__ = "earthquakes"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    magnitude: Mapped[float] = mapped_column(db.Float)
    location: Mapped[str] = mapped_column(db.String)
    year: Mapped[int] = mapped_column(db.Integer)

    def __repr__(self):
        return f'<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>'

    def to_dict(self):
        return {
            "id": self.id,
            "location": self.location,
            "magnitude": self.magnitude,
            "year": self.year
        }