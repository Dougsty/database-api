from flask import Flask, jsonify
import pandas as pd
from utils.sqlserver_conn import sqlconnection

app = Flask(__name__)


@app.route("/departments", methods=["GET"])
def get_departments():
    query = """
    SELECT 
        *
    FROM adventureworks2022.HumanResources.Department
    """

    # Estabelece a conexão com o banco de dados
    conn = sqlconnection()

    # Executa a consulta e obtém os resultados
    tables = pd.read_sql(query, conn)

    # Fecha a conexão
    conn.close()

    # Converte os resultados para JSON
    result = tables.to_dict(orient="records")

    return jsonify(result)


app.run(port=5000, host="localhost", debug=True)
