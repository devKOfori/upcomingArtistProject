from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE coordinates (x int, y int)"))
    conn.execute(
        text("INSERT INTO coordinates (x, y) VALUES (:x, :y)"), 
        [{"x": 1, "y": 2}, {"x": 0, "y": 1}]
    )
    conn.commit()