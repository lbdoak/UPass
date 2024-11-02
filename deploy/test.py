import psycopg2

def test_connection():
    try:
        conn = psycopg2.connect(
            dbname='sap',
            user='meli',
            password='metralleta',
            host='0.0.0.0',
            port='5432'
        )
        print("Connected successfully!")
        conn.close()
    except Exception as e:
        print("Connection failed:", e)

if __name__ == "__main__":
    test_connection()