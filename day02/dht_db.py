import time
import adafruit_dht
import board
import mysql.connector

# DHT11 센서 객체 생성 (GPIO 23 사용)
dht = adafruit_dht.DHT11(board.D23)

# MySQL DB 연결
db = mysql.connector.connect(
    host="localhost",
    user="raspi",
    password="1234",
    database="raspi"
)
cursor = db.cursor()

try:
    while True:
        try:
            temperature = dht.temperature
            humidity = dht.humidity
            print("Temp: ", temperature)
            print("Humid:", humidity)

            # DB에 값 삽입
            query = "INSERT INTO dht (temperature, humidity) VALUES (%s, %s)"
            values = (temperature, humidity)
            cursor.execute(query, values)
            db.commit()

        except RuntimeError as error:
            print("RuntimeError:", error.args[0])
        
        time.sleep(2)  # DHT11은 최소 1~2초 간격 필요

except KeyboardInterrupt:
    print("종료 중...")

finally:
    cursor.close()
    db.close()
    print("DB 연결 종료")
