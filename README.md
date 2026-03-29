# 📁 trash-overflow-detector

> 임베디드 기반 쓰레기통 Overflow 감지 및 알림 시스템 학습 및 프로젝트입니다.
> 
> 이론/설명은 Notion(또는 파일), 실습/코드는 GitHub 저장소로 관리합니다.

---

## 📌 프로젝트 설명

- 주제: 임베디드 기반 쓰레기통 Overflow 감지 및 알림 시스템
- 목표:
    - 카메라를 통해 쓰레기통 상태를 주기적으로 모니터링
    - Overflow 상태를 자동으로 감지하고 관리자에게 이메일 알림 전송
    - 엣지 컴퓨팅 기반 독립 운영으로 서버/네트워크 의존 최소화
 - 시스템 구성:
    - 라지베리파이 + HD 웹캠 기반 영상 수집
    - YOLOv5n 객체 탐지 모델로 쓰레기통 상태 분석
    - Overflow 지속 여부(30초 기준) 판단 → 사진 캡처 → 이메일 전송
  
👉 **PDF 문서**  
📄 [프로젝트 계획 보고서](https://github.com/Hwang-Injun34/trash-overflow-detector/blob/main/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8_%EA%B3%84%ED%9A%8D_%EB%B3%B4%EA%B3%A0%EC%84%9C.pdf)

---

## 🧩 주요 기능

### Raspberry Pi 단일 장치 기반 Overflow 감지

- 목표: 단일 라즈베리파이에서 Overflow 감지 및 이메일 알림 구현
- 구현 내용:
   - 카메라 90초 활성화, Overflow 감지
   - Overflow 30초 이상 지속 시 이미지 캡처 및 이메일 전송
   - 10분 대기 후 반복

👉 **PDF 문서**  
📄 [쓰레기통 Overflow 감지 시스템 작동](https://github.com/Hwang-Injun34/trash-overflow-detector/blob/main/%EC%93%B0%EB%A0%88%EA%B8%B0%ED%86%B5%20Overflow%20%EA%B0%90%EC%A7%80%20%EC%8B%9C%EC%8A%A4%ED%85%9C%20%EC%9E%91%EB%8F%99.pdf)

---

### 영상 기반 Overflow 감지 모델

- 목표: YOLOv5n 기반 객체 탐지 모델 학습 및 추론
- 구현 내용:
   - 쓰레기통 상태 3가지 분류:bin/garbage/overflow
   - 영상 수집 → 객체 탐지 → Overflow 판단
 
👉 **PDF 문서**  
📄 [YOLOv5 기반 쓰레기통 상태 감지 시스템](https://github.com/Hwang-Injun34/trash-overflow-detector/blob/main/YOLOv5%20%EA%B8%B0%EB%B0%98%20%EC%93%B0%EB%A0%88%EA%B8%B0%ED%86%B5%20%EC%83%81%ED%83%9C%20%ED%83%90%EC%A7%80%20%EC%8B%9C%EC%8A%A4%ED%85%9C.pdf)

---

## 🛠 사용 기술

- 임베디드 보드: Raspberry Pi
- 카메라: HD 웹캠 또는 Pi 전용 카메라
- 영상 분석: YOLOv5n, OpenCV, PyTorch
- 알림 시스템: Python(smtplib, email)
- 운영 방식: 엣지 컴퓨팅 기반 독립 실행

---

## 🗂 정리 방식

- 📄 **이론 & 개념**: PDF 파일
- 💻 **실습 & 코드**: GitHub
