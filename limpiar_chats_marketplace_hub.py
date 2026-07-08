import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "backend" / "marketplace_hub.db"
if not DB_PATH.exists():
    DB_PATH = Path(__file__).resolve().parent / "marketplace_hub.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

for table in [
    "mensajes_pendientes",
    "notificaciones",
    "mensajes",
    "conversaciones",
    "clientes",
    "productos",
]:
    cur.execute(f"DELETE FROM {table}")

cur.execute("""
    UPDATE sqlite_sequence
    SET seq = 0
    WHERE name IN (
        'mensajes_pendientes',
        'notificaciones',
        'mensajes',
        'conversaciones',
        'clientes',
        'productos'
    )
""")

conn.commit()
conn.close()

print("Listo: chats, mensajes, clientes y productos sincronizados fueron borrados.")
print("Los perfiles se conservaron.")
