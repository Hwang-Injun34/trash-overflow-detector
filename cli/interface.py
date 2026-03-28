import logging
import sys


from app.core.monitor import monitor_loop
from config import System

def run_cli():
    """CLI 모드로 시스템을 실행하는 함수"""
    # 모니터링 메인 루프 실행
    monitor_loop()