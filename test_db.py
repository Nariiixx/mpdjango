import MySQLdb

try:
    conn = MySQLdb.connect(
        host="containers-us-west-203.railway.app",
        user="penari",
        passwd="@I91275085n",
        db="pribanco",
        port=3306
    )
    print("Conexão bem-sucedida!")
    conn.close()
except MySQLdb.Error as e:
    print(f"Erro ao conectar: {e}")
