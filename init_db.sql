
CREATE TABLE IF NOT EXISTS vmemory (
    insert_date INTEGER,
    total INTEGER,
    available INTEGER,
    percent FLOAT,
    used INTEGER,
    free INTEGER,
    active INTEGER,
    inactive INTEGER,
    buffers INTEGER,
    cached INTEGER,
    shared INTEGER,
    slab INTEGER
);

CREATE TABLE IF NOT EXISTS cpu (
    insert_date INTEGER,
    user FLOAT,
    nice FLOAT,
    system FLOAT,
    idle FLOAT,
    iowait FLOAT,
    irq FLOAT,
    softirq FLOAT,
    steal FLOAT,
    guest FLOAT,
    guestnice FLOAT
);

