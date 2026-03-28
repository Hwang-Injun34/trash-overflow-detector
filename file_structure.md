
[파일구조]
embedded_project/
├── main.py               # 프로그램 진입점 (CLI/GUI 실행 선택 가능)
├── config.py             # 설정값 관리 파일
├── .env                  # 이메일 전송 등 환경 변수 정의
├── requirements.txt      # 필요한 Python 패키지 목록
├── monitoring.log        # 시스템 로그 저장 파일
├── alert_images/         # 경고 상황 발생 시 저장되는 이미지 폴더

├── app/                  # 핵심 기능 모듈 디렉토리
│   ├── __init__.py       
│   ├── camera/           # 카메라 영상 캡처 관련 기능
│   ├── core/             # 모니터링 로직 실행부
│   ├── detector/         # YOLO 객체 탐지 기능
│   ├── model/            # 모델 파일(.pt) 및 프레임 저장 유틸
│   ├── sensor/           # 센서 값 읽기 및 처리
│   └── utils/            # 이메일 전송 등 기타 유틸리티

├── cli/                  # CLI (커맨드라인) 인터페이스
│   └── interface.py      # CLI 실행 진입점
├── gui/                  # GUI (그래픽 인터페이스)
│   └── interface.py      # GUI 실행 진입점




[CLI 모드]
- 사용자 인터페이스 없이 백그라운드에서 조용히 실행됩니다.
- 실시간으로 객체를 감지하고, 이상 상황 발생 시 이미지 저장 및 이메일 알림이 자동으로 이루어집니다.

python main.py --mode cli


[GUI 모드]
- 간단한 그래픽 창이 실행되며, 모니터링 상태를 시각적으로 확인할 수 있습니다.
- 실제 감지 기능만 동작합니다.

python main.py --mode gui