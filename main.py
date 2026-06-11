import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind(('localhost', 1672))
    s.listen(1)
    print("Đang chiếm cổng 5432... (Script vẫn đang chạy)")
    time.sleep(60) # Giữ cổng trong 60 giây thay vì đợi Enter
except OSError as e:
    print(f"XUNG ĐỘT PHÁT HIỆN: {e}")