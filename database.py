import os
from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECT_STRING']

engine = create_engine(db_connection_string, connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from roles;"))
    result_dicts = []
    for row in result.all():
      result_dicts.append(dict({"title":row[1], "name":row[2]}))
    return result_dicts