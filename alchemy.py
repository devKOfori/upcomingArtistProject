from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

with engine.begin() as conn:
    conn.execute(text("CREATE TABLE coordinates (x int, y int)"))
    conn.execute(
        text("INSERT INTO coordinates (x, y) VALUES (:x, :y)"), 
        [{"x": 1, "y": 2}, {"x": 0, "y": 1}]
    )

with engine.begin() as conn:
    # results = conn.execute(text("select * from coordinates"))
    results = conn.execute(text("select * from coordinates where y = :y"), {"y": 2})
    for row in results: 
        print("x = ", row.x, "y = ", row.y)
        