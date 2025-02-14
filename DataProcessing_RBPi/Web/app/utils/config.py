# Configuração do servidor
import os

class Config:
    """Configurações gerais do projeto"""
    
    # Configurações do servidor
    SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")  # Endereço do servidor (default 0.0.0.0)
    SERVER_PORT = int(os.getenv("SERVER_PORT", 8000))  # Porta do servidor (default 8000)
    
    # Configurações do banco de dados (se houver)
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # URL de conexão com o banco (Exemplo para SQLite)
    
    # Configuração de logs
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")  # Nível de log (default INFO)
    
    # Configurações de batch (se necessário para controlar os lotes de dados)
    BATCH_SIZE = int(os.getenv("BATCH_SIZE", 100))  # Tamanho do lote (default 100)
    BATCH_INTERVAL = int(os.getenv("BATCH_INTERVAL", 60))  # Intervalo entre lotes (em segundos)
    
    # Outras configurações podem ser adicionadas conforme necessidade
    @staticmethod
    def init_app(app):
        """Método para inicializar configurações no aplicativo"""
        pass


# A seguir, você pode adicionar um arquivo de configurações para ambientes de desenvolvimento, produção, etc.

class DevelopmentConfig(Config):
    """Configuração para ambiente de desenvolvimento"""
    DEBUG = True
    DATABASE_URL = "sqlite:///./dev.db"

class ProductionConfig(Config):
    """Configuração para ambiente de produção"""
    DEBUG = False
    DATABASE_URL = "postgresql://user:password@localhost/dbname"

# Seleção de ambiente
config_by_name = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig
}
