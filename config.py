import os
import logging
from pathlib import Path
from dotenv import load_dotenv


# 경로 설정
BASE_DIR = Path(__file__).parent
ALERT_IMAGE_DIR = BASE_DIR / "alert_images"
MODEL_DIR = BASE_DIR / "app" / "model"

# 디렉토리 생성
os.makedirs(ALERT_IMAGE_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

load_dotenv() 

# 시스템 설정
class System:
    CAMERA_ID = 0
    LOG_LEVEL = logging.INFO
    MONITOR_INTERVAL = 600  # 10분
    ACTIVE_DURATION = 90    # 1분30초
    OVERFLOW_DURATION = 30  # 30초
    COOLDOWN_MINUTES= 10 # 10분
    ALERT_IMAGE_DIR = str(ALERT_IMAGE_DIR)  # 이미지 저장 디렉토리 경로

# 모델 설정
class Model:
    PATH = str(MODEL_DIR / "best8.pt")
    CLASSES = {
        "OVERFLOW": "overflow",
        "BIN": "garbage_bin"
    }
    CONFIDENCE_THRESHOLD = 0.7 # 신뢰도 임계값

# 이메일 설정
class Email:
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SENDER = "ngms0304@gmail.com"
    PASSWORD = os.getenv("PASSWORD")
    RECEIVER = "ngms0304@naver.com"
    SUBJECT = "쓰레기통 꽉참 알림"