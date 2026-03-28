import logging
import time
import cv2
from datetime import datetime
from pathlib import Path

from app.camera.camera_capture import CameraCapture
from app.utils.email_sender import send_alert_email  # 기본 전송
from app.detector.yolo_detector import detect_overflow
from app.sensor.sensor_interface import check_status
from config import System, Model

logger = logging.getLogger(__name__)

ALERT_IMAGE_DIR = Path(System.ALERT_IMAGE_DIR)

def monitor_loop():
    """모니터링 루프: 주기적으로 카메라 작동 및 오버플로우 감지"""
    while True:
        logger.info("[카메라 시작] 카메라 작동 시작")
        with CameraCapture() as camera:
            overflow_start = None
            start_time = time.time()

            while time.time() - start_time < System.ACTIVE_DURATION:
                frame = camera.get_frame()
                if frame is None:
                    continue

                # 오버플로우 감지
                overflow_detected, detections = detect_overflow(frame)
                if overflow_detected:
                    if overflow_start is None:
                        overflow_start = time.time()
                    elif time.time() - overflow_start >= System.OVERFLOW_DURATION:
                        _handle_overflow(frame, detections)
                        break
                else:
                    overflow_start = None

        logger.info("[카메라 중지] 카메라 작동 중단")
        logger.info("[대기 중] 10분 대기 후 카메라 재시작")

        # 다음 실행까지 대기
        sleep_duration = max(0, System.MONITOR_INTERVAL - System.ACTIVE_DURATION)
        time.sleep(sleep_duration)

def _handle_overflow(frame, detections):
    """오버플로우 발생 시 이미지 저장 및 이메일 발송"""
    ALERT_IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = ALERT_IMAGE_DIR / f"overflow_{timestamp}.jpg"

    # 오버플로우 바운딩 박스 그리기
    for det in detections:
        if det["class"] == Model.CLASSES["OVERFLOW"]:
            x1, y1, x2, y2 = map(int, det["box"])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, f"{det['class']} {det['confidence']:.2f}",
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imwrite(str(filename), frame)
    logger.info(f"[이미지 저장] Overflow 감지됨 - 저장된 이미지: {filename}")

    # 센서 상태에 따라 이메일 전송 대상 분기
    if check_status():
        logger.info("[이메일 발송] 센서 정상 - 청소부에게 전송 중...")
        try:
            send_alert_email(str(filename), sensor_ok=True)
            logger.info("[이메일 발송 완료] 청소부에게 전송 완료")
        except Exception as e:
            logger.error(f"[이메일 발송 실패] {e}")
    else:
        logger.warning("[이메일 발송] 센서 실패 - 관리자에게 전송 중...")
        try:
            send_alert_email(str(filename), sensor_ok=False)
            logger.info("[이메일 발송 완료] 센서 실패 이미지 전송 완료")
        except Exception as e:
            logger.error(f"[이메일 발송 실패] {e}")
