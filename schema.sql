DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    SepalLengthCm REAL,
    SepalWidthCm REAL,
    PetalLengthCm REAL,
    PetalWidthCm real,
    Species varchar


);