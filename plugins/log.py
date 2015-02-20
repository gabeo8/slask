#TODO: move to utils or something?
def query(db, sql, *params):
    c = db.cursor()
    c.execute(sql, params)
    rows = c.fetchall()
    c.close()
    db.commit()
    return rows

def on_message(msg, server):
    db = server["db"]
    query(db, "INSERT INTO log VALUES (?, ?, ?, ?, ?)", msg["text"], msg["user"], msg["ts"], msg["team"], msg["channel"])

def on_init(server):
    db = server["db"]
    query(db, "CREATE TABLE IF NOT EXISTS log (msg STRING, sender STRING, time STRING, team STRING, channel STRING)")
