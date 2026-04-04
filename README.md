# 📁 trash-overflow-detector

> 엣지 디바이스 기반 쓰레기통 Overflow 감지 및 알림 시스템<br>
> 카메라와 객체 탐지 모델을 활용하여 실시간 상태를 분석하고<br>
> 이상 상황 발생 시 자동으로 알림을 전송하는 임베디드 시스템 프로젝트

---

## 🧾 프로젝트 정보
- 프로젝트 형태: 개인 프로젝트(임베디드 + Edge AI 시스템 구현)
- 결과
    - Raspberry Pi 단일 장치에서 Overflow 감지 및 알림 시스템 구현
    - YOLOv5n 기반 객체 탐지 모델을 활용한 상태 분류 시스템 구축
    - 엣지 컴퓨팅 기반 독립 실행 구조 설계(서버 의존 최소화)
    - 실시간 감지 → 조건 판단 → 알림 전송까지 자동화 파이프라인 구현

 📄 **PDF 문서**  
- [프로젝트 계획 보고서](https://github.com/Hwang-Injun34/trash-overflow-detector/blob/main/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8_%EA%B3%84%ED%9A%8D_%EB%B3%B4%EA%B3%A0%EC%84%9C.pdf)

---

## 📌 프로젝트 개요
Raspberry Pi와 카메라를 활용하여 <br>
쓰레기통 상태를 주기적으로 모니터링하고, <br>
Overflow 상태를 자동으로 감지 및 알림하는 시스템을 구현한 프로젝트입니다. 

영상 기반 객체 탐지를 통해 단순 센서 방식의 한계를 보완하고, <br>
엣지 컴퓨팅 구조를 통해 네트워크 의존도를 최소화하였습니다.

---

## 🚨 문제 정의
기존 쓰레기 관리 방식은 <br>
수동 점검 또는 단순 센서 기반으로 이루어져 다음과 같은 한계가 존재한다.<br>
- Overflow 상태를 실시간으로 파악하기 어려움
- 불필요한 수거 또는 지연된 수거 발생
- 쓰레기통 내부 상태를 정확히 판단하기 어려움  

특히 단순 센서 기반 시스템은
쓰레기의 양과 상태를 정확히 반영하지 못한다는 문제가 있다.

---

## 💡 해결 전략
- 카메라 기반 영상 데이터를 활용한 상태 분석
- YOLOv5n 객체 탐지 모델을 통한 쓰레기 상태 분류
- 일정 시간(30초) 이상 지속 시 Overflow로 판단
- 이미지 캡처 후 이메일 알림 자동 전송
- Raspberry Pi 단일 장치에서 모든 처리 수행(Edge AI 구조)

---

## 🧩 주요 기능

### 1️⃣ Raspberry Pi 단일 장치 기반 Overflow 감지

- 목표: 단일 라즈베리파이에서 Overflow 감지 및 이메일 알림 구현
- 구현 내용:
   - 카메라 90초 활성화, Overflow 감지
   - Overflow 30초 이상 지속 시 이미지 캡처 및 이메일 전송
   - 10분 대기 후 반복

📄 **PDF 문서**  
- [쓰레기통 Overflow 감지 시스템 작동](https://github.com/Hwang-Injun34/trash-overflow-detector/blob/main/%EC%93%B0%EB%A0%88%EA%B8%B0%ED%86%B5%20Overflow%20%EA%B0%90%EC%A7%80%20%EC%8B%9C%EC%8A%A4%ED%85%9C%20%EC%9E%91%EB%8F%99.pdf)

---

### 2️⃣ 영상 기반 Overflow 감지 모델

- 목표: YOLOv5n 기반 객체 탐지 모델 학습 및 추론
- 구현 내용:
   - 쓰레기통 상태 3가지 분류:bin/garbage/overflow
   - 영상 수집 → 객체 탐지 → Overflow 판단
 
📄 **PDF 문서**  
- [YOLOv5 기반 쓰레기통 상태 감지 시스템](https://github.com/Hwang-Injun34/trash-overflow-detector/blob/main/YOLOv5%20%EA%B8%B0%EB%B0%98%20%EC%93%B0%EB%A0%88%EA%B8%B0%ED%86%B5%20%EC%83%81%ED%83%9C%20%ED%83%90%EC%A7%80%20%EC%8B%9C%EC%8A%A4%ED%85%9C.pdf)

---

## 🛠 기술 스택

- Embedded: Raspberry Pi
- Computer Vision: YOLOv5n, OpenCV, PyTorch
- Backend Logic: Python
- Notification: smtplib, email
- Architecture: Edge Computing
---

## 🗂 정리 방식

- 📄 **이론 & 개념, 보고서**: PDF
- 🔗 **실습 & 코드**: GitHub
