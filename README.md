(*추가)한국 기준으로 서버 시간 설정: sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
현재 상세보기 출력: ls -al
경로 이동: cd 경로
vim 편집기로 파일 전송: vim bitcoinAutoTrade.py
vim 편집기 입력: i
vim 편집기 생성: :wq!
패키지 목록 업데이트: sudo apt update
pip3 설치: sudo apt install python3-pip
pip3로 pyupbit 설치: pip3 install pyupbit
배경 실행: nohup python3 bitcoinAutoTrade.py > output.log &
실행중인지 확인: ps ax | grep .py
처리 종료(PID는 ps ax | grep .py를 해야 하는지 확인 가능): kill -9 PID
PID 설명
