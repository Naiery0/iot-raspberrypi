-- 스키마 생성
CREATE DATABASE IF NOT EXISTS raspi;

-- 테이블 생성
USE raspi;

CREATE TABLE IF NOT EXISTS dht (
    id INT AUTO_INCREMENT PRIMARY KEY,
    temperature FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- 계정 생성
-- 새 사용자 생성 (원한다면 기존 계정 삭제 후 진행)
CREATE USER 'raspi'@'localhost' IDENTIFIED BY '1234';

-- raspi 스키마 전체 권한 부여
GRANT ALL PRIVILEGES ON raspi.* TO 'raspi'@'localhost';

-- 변경 사항 적용
FLUSH PRIVILEGES;
