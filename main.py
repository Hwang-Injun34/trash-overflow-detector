import argparse
import logging


from cli.interface import run_cli
from gui.interface import run_gui
from config import System


def configure_logging():
    """로깅 설정을 초기화"""
    logging.basicConfig(
        level=System.LOG_LEVEL, # 설정된 로그 레벨 사용
        format='%(asctime)s - %(levelname)s - %(message)s', # 로그 출력 형식
        handlers=[
            logging.FileHandler('monitoring.log'), # 로그 파일 저장
            logging.StreamHandler() # 콘솔 출력
        ],
        force=True
    )

def parse_arguments():
    """명령줄 인수 파싱"""
    parser = argparse.ArgumentParser(
        description="오버플로우 모니터링 시스템 (CLI/GUI 모드 지원)"
    )
    parser.add_argument(
        '--mode',
        choices=['cli', 'gui'], # 지원 모드
        default='cli', # 기본값
        help='실행 모드 선택 (기본값: cli)'
    )
    return parser.parse_args() # 실제 인수 파싱 수행

def main():
    """프로그램의 주 실행 함수"""
    # 1.인수 파싱
    args = parse_arguments()

    # 2.로깅 설정
    configure_logging()

    try:
        # 3.실행 모드에 따라 인터페이스 실행
        if args.mode == 'cli':
            logging.info("CLI 모드 시작") # 로그 기록
            run_cli() # CLI 인터페이스 실행
        else:
            logging.info("GUI 모드 시작") # 로그 기록
            run_gui() # GUI 인터페이스 실행

    except KeyboardInterrupt:
        # 사용자가 Ctrl+C로 종료할 때
        logging.info("사용자 요청으로 시스템 종료")
    except Exception as e:
        # 기타 예외 처리
        logging.critical(f"시스템 오류: {str(e)}")

if __name__ == "__main__":
    main()