-- createdb.sql
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    region TEXT DEFAULT NOO
);

CREATE TABLE IF NOT EXISTS laps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    laptime INTEGER NOT NULL,
    track TEXT NOT NULL,
    car_model TEXT NOT NULL,
    date TEXT NOT NULL,
    other TEXT,
    others TEXT
);
CREATE TABLE IF NOT EXISTS tracks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    city TEXT,
    region TEXT,
    highscore TEXT,
    laps INTEGER,
    track_distance INTEGER
);
