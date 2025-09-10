from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Criar variável com a URL do arquivo do banco de dados
BD_DEV_VENDAS_URL = "sqlite:///./bd_dev_vendas.db"

# Cria uma conexão entre o ORM e o Banco 
engine = create_engine(
    BD_DEV_VENDAS_URL, connect_args={"check_same_thread": False}
)

# Cria uma sessão para interação com o Banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()