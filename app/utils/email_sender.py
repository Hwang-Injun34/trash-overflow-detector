import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import logging
from datetime import datetime
from pathlib import Path

# 커스텀 설정 모듈에서 이메일 설정, 이미지 디렉토리 경로 불러오기
from config import Email, ALERT_IMAGE_DIR

def send_alert_email(image_path: Path, sensor_ok: bool = True) -> bool:
    """
    오버플로우 감지 시 이메일을 발송

    Args:
        image_path (Path): 첨부할 이미지 파일 경로
        sensor_ok (bool): 센서가 정상 동작했는지 여부

    Returns:
        bool: 이메일 전송 성공 여부
    """
    image_path = Path(image_path)

    # 이메일 메시지 구성(HTML + 이미지 첨부)
    msg = MIMEMultipart('related')
    msg['Subject'] = f"[모니터링 알림] {Email.SUBJECT} - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    msg['From'] = Email.SENDER
    msg['To'] = Email.RECEIVER
    msg['Cc'] = getattr(Email, 'CC_RECEIVER', '')
    msg.add_header('Content-Type', 'text/html; charset=utf-8')

    # 센서 상태에 따라 본문 내용 변경
    if sensor_ok:
        sensor_message = "센서와 카메라 모두 쓰레기통이 꽉 찬 것으로 판단했습니다."
    else:
        sensor_message = "카메라는 쓰레기통이 꽉 찬 것으로 판단했지만, 센서에서 응답이 없습니다."

    # 이메일 본문(HTML 형식)
    body = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: Arial, '맑은 고딕', sans-serif;
            font-size: 14px;
            color: #333;
            background-color: #ffffff;
            padding: 20px;
        }}
        .container {{
            max-width: 700px;
            margin: auto;
            padding: 20px;
            border: 1px solid #dddddd;
            background-color: #fefefe;
        }}
        h2 {{
            font-size: 18px;
            border-bottom: 1px solid #ccc;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        .info-block {{
            background-color: #f6f6f6;
            padding: 15px;
            border: 1px solid #e0e0e0;
            margin-bottom: 20px;
        }}
        .info-block p {{
            margin: 6px 0;
        }}
        .image-section {{
            text-align: center;
            margin-top: 20px;
        }}
        .footer {{
            font-size: 12px;
            color: #777;
            margin-top: 30px;
            border-top: 1px solid #e0e0e0;
            padding-top: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h2>오버플로우 감지 알림</h2>

        <p>아래와 같이 시스템에서 이상 상황이 감지되어 알림을 드립니다.</p>

        <div class="info-block">
            <p><strong>감지 위치:</strong> 순천향대학교 멀티미디어 5층 컴퓨터소프트웨어공학과</p>
            <p><strong>발생 일시:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p><strong>감지 내용:</strong> {sensor_message}</p>
        </div>

        <div class="image-section">
            <p><strong>감지 이미지:</strong></p>
            <img src="cid:evidence.jpg" alt="오버플로우 이미지" style="max-width: 100%; height: auto; border: 1px solid #ccc;">
        </div>

        <p>확인 후 조치 부탁드립니다. 본 메일은 자동 발송된 것으로 회신은 처리되지 않습니다.</p>

        <div class="footer">
            ⓒ {datetime.now().year} 시스템 모니터링 자동화. All rights reserved.
        </div>
    </div>
</body>
</html>
"""
    # 본문 메시지 첨부
    msg.attach(MIMEText(body, 'html'))

    # 첨부 이미지 읽어서 이메일에 추가
    try:
        with open(image_path, 'rb') as f:
            img = MIMEImage(f.read())
            img.add_header('Content-ID', '<evidence.jpg>')
            img.add_header('Content-Disposition', 'inline', filename=image_path.name)
            msg.attach(img)
    except Exception as e:
        logging.error(f"이미지 첨부 실패: {e}", exc_info=True)
        return False


    # 이메일 전송 시도(최대 3회 재시도)
    for attempt in range(3):
        try:
            with smtplib.SMTP(Email.SMTP_SERVER, Email.SMTP_PORT) as server:
                server.starttls()
                server.login(Email.SENDER, Email.PASSWORD)
                recipients = [Email.RECEIVER]
                if hasattr(Email, 'CC_RECEIVER'):
                    recipients.append(Email.CC_RECEIVER)
                server.sendmail(Email.SENDER, recipients, msg.as_string())
            logging.info(f"이메일 전송 성공: {image_path}")
            return True
        except Exception as e:
            logging.warning(f"이메일 전송 실패 ({attempt + 1}회 시도): {e}", exc_info=True)
            time.sleep(5)

    #최종 실패 처리
    logging.error(f"이메일 전송 최종 실패: {image_path}")
    return False
