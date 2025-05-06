# 거짓으로 처리되는 값의 판정 2

x = 0  # 거짓이 None인 것은 아니다.
if x is None:
    print("성립")
else:
    print("미성립")
