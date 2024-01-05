# -----------------------------------------------------------------------------
# 다양한 함수의 형태 - (2) 반환값 없는 함수
#
# - 함수 생성 문법
#   def 함수이름(매개변수1, 매개변수2, ..., 매개변수n):
#       실행코드
#       실행코드
# -----------------------------------------------------------------------------
# 함수 기능 : 2개의 정수를 덧셈 후 출력해주는 기능
# 함수 이름 : addTwo
# 매개 변수 : x, y
# 반환값    : 없음
# -----------------------------------------------------------------------------
def addTwo(x, y):
    value = x + y
    print(f'{x} + {y} = {value}')


# 함수 사용 즉 함수 호출 ======================================================
addTwo(10, 3)

# 함수 호출 시에 매개변수 갯수와 동일하게 데이터 전달해야 함!! ----------------
# Error
# addTwo(10, 10, 10)
# addTwo(10)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# 함수 기능 : 영어 단어를 입력 받아서 모두 대문자로 변환 해주는 기능
# 함수 이름 : convertCase
# 매개 변수 : word
# 반환값    : 없음
# -----------------------------------------------------------------------------
def convertCase(word: str):
    return word.upper()


# -----------------------------------------------------------------------------
# 함수 기능 : 시퀀스 객체의 모든 원소를 대문자로 변환 해주는 기능
# 함수 이름 : convertCase2
# 매개 변수 : str 타입의 원소로 구성된 list
# 반환값    : 없음
# -----------------------------------------------------------------------------
def convertCase2(dataList: list):
    # for idx in range(len(dataList)):
    #     dataList[idx] = dataList[idx].upper()

    for idx, data in enumerate(dataList):
        dataList[idx] = data.upper()


# 함수 사용 즉, 함수 호출 -----------------------------------------------------
datas = ['Apple', 'Banana', 'Mango']
print(f'[BF] {datas}')

# convertCase2(datas)
datas[0] = convertCase(datas[0])

print(f'[AF] {datas}')

for data in datas:
    print(data, data.upper())

# for idx in range(len(datas)):
#     datas[idx] = datas[idx].upper()

for idx, data in enumerate(datas):
    datas[idx] = data.upper()

print(datas)
