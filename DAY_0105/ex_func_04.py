# -----------------------------------------------------------------------------
# 다양한 함수의 형태 - (3) return 키워드
# - 함수 호출한 곳으로 돌아가게 하는 기능
#   결과값이 함께 있다면 결과값을 가지고 돌아감
#
# - 함수 생성 문법
#   def 함수이름(매개변수1, 매개변수2, ..., 매개변수n):
#       조건코드와 return 값
#       실행코드
#       실행코드
#       return 결과값
# -----------------------------------------------------------------------------
# 함수 기능 : 팩토리얼을 계산 후 계산 결과를 반환해주는 기능
#             팩토리얼이란? 3! = 3 * 2 * 1
# 함수 이름 : funcFac
# 매개 변수 : num
# 반환값    : 계산 결과
# -----------------------------------------------------------------------------
def funcFac(num: int):
    if not num:
        return 1
    ret = 1
    if num > 0:
        for n in range(num, 0, -1):
            ret *= n
    return ret


print(f'0! = {funcFac(0)}')
print(f'3! = {funcFac(3)}')
