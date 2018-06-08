str = "Life is too short, You need Python"

str = str.lower() # 소문자로 변경
str = str.replace(" ", "") # 공백 제거
str = str.replace(",", "") # 컴마 제거

#str = "Life is too short, You need Python"
#str = str.lower().replace(" ", "").replace(",", "")

lst = list(str) # str를 list으로 형변환
print("list:", lst)
chars = set(lst) # lst를 set으로 형변환
print("chars:", chars)
lst = list(chars) # chars를 list로 형변환

lst.sort()
print("lst", lst)
print("length fo lst:", len(lst))