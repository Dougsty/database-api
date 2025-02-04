from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os


def sqlconnection() -> create_engine:
    """
    Establishes a connection to a SQL Server database using the provided credentials.

    Returns:
        engine (sqlalchemy.engine.Engine): The SQLAlchemy engine object representing the connection to the database.
    """

    # Login info
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")

    # Server info
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_NAME")
    port = os.getenv("DB_PORT")
    # Construct the connection string
    connection_string = (
        f"mssql+pymssql://{username}:{password}@{server},{port}/{database}"
    )

    try:
        # Create the SQLAlchemy engine
        engine = create_engine(connection_string)

        # Test the connection
        with engine.connect() as connection:
            print("Conexão bem-sucedida!")
        return engine
    except SQLAlchemyError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise
