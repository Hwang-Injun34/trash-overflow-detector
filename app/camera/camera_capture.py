import cv2
import logging

# 커스텀 모듈
from config import System

class CameraCapture:
    """카메라 캡처를 관리하는 클래스(with 지원)"""

    def __init__(self, camera_id=System.CAMERA_ID):
        """
        카메라 초기화
        Args:
            camera_id (int/str): 카메라 ID 또는 비디오 파일 경로
        
        Raises:
            RuntimeError: 카메라 열기에 실패한 경우
        """
        # 카메라 장치 열기 시도
        self.cap = cv2.VideoCapture(camera_id)

        # 카메라 정상 오픈 확인
        if not self.cap.isOpened():
            raise RuntimeError(f"카메라 {camera_id} 열기 실패")
        logging.info("카메라 초기화 완료")

    def get_frame(self):
        """
        프레임 한장 캡처

        Returns:
            numpy.ndarray: 캡처된 프레임 (성공 시), None (실패 시)
        """
        ret, frame = self.cap.read() # 프레임 읽기 시도

        # ret 값으로 성공/실패 확인
        return frame if ret else None

    def release(self):
        """ 카메라 리소스 해제"""
        if self.cap.isOpened(): 
            self.cap.release() 
            logging.info("카메라 리소스 해제")

    # 컨텍스트 관리자 프로토콜 구현
    def __enter__(self):
        """with 문 진입 시"""
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        """with 문 종료 시"""
        self.release()