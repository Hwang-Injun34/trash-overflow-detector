import cv2
import logging
import sys


from config import System, Model
from app.camera.camera_capture import CameraCapture
from app.detector.yolo_detector import YOLODetector

def run_gui():
    """GUI 모드로 오버플로우 모니터링 시스템 실행"""
    # 카메라 및 감지기 초기화
    cam = CameraCapture()
    detector = YOLODetector() 

    # OpenCV 윈도우 설정
    window_name = "Overflow Monitor (ESC to exit)"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    try:
        # 메인 루프 - ESC 키를 누를 때까지 계속 실행
        while True:
            # 1. 프레임 캡처
            frame = cam.get_frame()
            if frame is None: # 유효한 프레임이 아닌 경우 건너띔
                continue
            
            # 2. 객체 감지
            detections = detector.detect(frame)

            # 3. 감지 결과 표시
            for det in detections:
                # 색상 설정: 오버플로우(빨강), 기타(초록)
                color = (0, 0, 255) if det["class"] == Model.CLASSES["OVERFLOW"] else (0, 255, 0)

                # 바운딩 박스 좌표 추출
                x1, y1, x2, y2 = map(int, det["box"])

                # 바운딩 박스 라벨 그리기
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

                # 클래스 이름과 신뢰도 텍스트 표시
                cv2.putText(frame, f"{det['class']} {det['confidence']:.2f}",
                           (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
            # 4. 프레임 출력
            cv2.imshow(window_name, frame)

            # 5. ESC 키 입력 시 종료
            if cv2.waitKey(1) == 27:
                break

    finally:
        cam.release() # 카메라 지원 해제
        cv2.destroyAllWindows() # 모든 OpenCV 윈도우 닫기