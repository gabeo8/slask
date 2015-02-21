"""Log all messages to the database"""

def on_message(msg, server):
    server.query("INSERT INTO log VALUES (?, ?, ?, ?, ?)", msg["text"], msg["user"], msg["ts"], msg["team"], msg["channel"])

def on_init(server):
    #TODO: create username -> userid map?
    server.query("CREATE TABLE IF NOT EXISTS log (msg STRING, sender STRING, time STRING, team STRING, channel STRING)")
