from ultralytics import YOLO
import logging

# 커스텀 모듈
from config import Model

class YOLODetector:
    """YOLOv8 기반 객체 감지기"""
    def __init__(self):
        """모델 로드 및 클래스 유효성 검증"""
        try:
            # 설정 파일에 저장된 경로에서 모델 로드
            self.model = YOLO(Model.PATH)

            # 모델 클래스 검증 수행
            self._validate_classes()
            logging.info(f"모델 로드 완료: {Model.PATH}")
        except Exception as e:
            logging.critical(f"모델 로드 실패: {str(e)}")
            raise # 초기화 실패 시 호출자에게 예외 전파

    def _validate_classes(self):
        """설정된 클래스가 모델에 존재하는지 확인"""
        # 모델에 없는 클래스 찾기
        missing = [
            cls for cls in Model.CLASSES.values() 
            if cls not in self.model.names.values()
        ]
        if missing:
            raise ValueError(f"모델에 누락된 클래스: {missing}")

    def detect(self, frame):
        """
        객체 감지 수행
        
        Args:
            frame (numpy.ndarray): 입력 이미지
            
        Returns:
            list[dict]: 감지 결과 리스트
        """
        # 모델 추론 실행
        results = self.model(frame)

        # 결과를 사용하기 쉬운 딕셔너리 형태로 변환
        return [{
            "class": self.model.names[int(box.cls)], # 클래스 이름 매핑
            "confidence": float(box.conf), # 신뢰도(확률값)
            "box": box.xyxy[0].tolist() # 바운딩 박스 좌표
        } for box in results[0].boxes] # 첫 번째 결과의 모든 박스 처리

# 전역 감지기 인스턴스(재사용 목적)
detector_instance = YOLODetector()

def detect_overflow(frame):
    """
    프레임에서 Overflow 감지 여부 반환
    Args:
        frame (numpy.ndarray): 입력 이미지

    Returns:
        (bool, list): Overflow 발생 여부, 감지 결과
    """
    results = detector_instance.detect(frame)
    is_overflow = any(obj["class"] == "overflow" for obj in results)
    return is_overflow, results
