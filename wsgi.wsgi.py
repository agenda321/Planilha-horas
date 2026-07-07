# ============================================================
# 3. wsgi.py
# ============================================================
import os
import time
from app import app, db, Pilot, povoar_dados_iniciais

def init_db():
    max_retries = 5
    for attempt in range(max_retries):
        try:
            with app.app_context():
                db.create_all()
                if Pilot.query.count() == 0:
                    povoar_dados_iniciais()
                print("✅ Banco de dados conectado e inicializado com sucesso.")
                return
        except Exception as e:
            print(f"⚠️ Tentativa {attempt+1}/{max_retries} falhou: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)
            else:
                print("❌ Não foi possível conectar ao banco após várias tentativas.")
                raise

init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
