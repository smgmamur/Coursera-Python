import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('ibr_damage.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS ibr_region;
DROP TABLE IF EXISTS ibr_damage;
DROP TABLE IF EXISTS damage_type;
DROP TABLE IF EXISTS repair_type;
DROP TABLE IF EXISTS repair_tool;
DROP TABLE IF EXISTS nde_method;
DROP TABLE IF EXISTS member_1;
DROP TABLE IF EXISTS member_2;
DROP TABLE IF EXISTS member_3;

CREATE TABLE ibr_region (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE ibr_damage (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    length    INTEGER,
    depth   INTEGER,
    loc_x   INTEGER,
    loc_y   INTEGER,
    loc_z   INTEGER,
    damage_type_id   INTEGER,
    repair_id   INTEGER
);

CREATE TABLE damage_type (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE repair_type (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE,
    tool_id   INTEGER,
    nde_id   INTEGER
);

CREATE TABLE repair_tool (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE nde_method (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE member_1 (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    repair_type_id    INEGER,
    repair_id_id   INTEGER
);

CREATE TABLE member_2 (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    tool_id_id    INTEGER,
    repair_tool_id   INTEGER
);

CREATE TABLE member_3 (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    nde_id_id    INTEGER,
    nde_method_id   INTEGER
);
''')

input("Press Enter to close this window")
