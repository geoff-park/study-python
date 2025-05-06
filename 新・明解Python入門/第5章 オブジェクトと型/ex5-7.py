# None을 빈 문자열로 변환
x = None
s = x or ""
print(s)

# 빈 문자열은 빈 문자열 그대로
x = ""
s = x or ""
print(s)

# 이외의 문자열은 그대로
x = "ABC"
s = x or ""
print(s)
