# -----------------------------------------------------------------------------
# [요청] 키보드로 숫자를 입력 받아서 입력 받은 숫자 만큼
#        *을 화면에 출력해 주세요~
# [해결] - (1) 숫자 입력 받기 => input()
#              str => int 형변환
#        - (2) 입력 받은 숫자 만큼 * 출력
#              '*' * 숫자
# -----------------------------------------------------------------------------
# (1) 숫자 입력 받기
num = input("정수 입력: ")

# 입력 받은 문자가 있다 => len(num)
if len(num) > 0:
    # 조건 len(num) > 0 True일 때 실행되는 코드 부분
    # (2) str 숫자 ==> int 숫자 형변환
    num = int(num)

    # (3) '*' 출력
    print('*' * num)
else:
    # 조건 len(num) > 0 False일 때 실행되는 코드 부분
    print("입력된 숫자가 없음")


# 조건에 상관없이 순서대로 실행되는 코드
print("END")
