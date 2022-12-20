import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    __env = os.environ
    print(__env)
    db = 'postgresql://{user}:{password}@{host}:{port}/{db_name}'.format(
        
        user = __env.get('db_USER'),
        password = __env.get('PASSWORD',''),
        host = __env.get('HOST'),
        port=__env.get("PORT"),
        db_name = __env.get("DB_NAME")
    )
    
settings = Settings()