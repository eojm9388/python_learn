# Data Structure

### 데이터 구조 `Data Structure`
여러 데이터를 효과적으로 사용, 관리하기 위한 구조

(list, str, dict 등)

### 자료 구조
- 컴퓨터 공학에서는 '자료 구조' 라고 함
- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것

### 데이터 구조 활용
- 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 `메서드`를 호출하여 다양한 기능을 활용하기

### 메서드 `method`
객체에 속한 함수
> 객체의 상태를 조작하거나 동작을 수행

### 메서드 특징
- 메서드는 클래스 (`class`) 내부에 정의되는 함수
- 클래스는 파이썬에서 `타입을 표현하는 방법`이며 이미 은연중에 사용해왔음
- 예를 들어 `help` 함수를 통해 str을 호출해보면 class 였다는 것을 확인 가능

```python
print(help(str))

"""
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  …
"""
```

### 지금 알아야 할 것
메서드는 어딘가(클래스)에 속해 있는 함수이며, 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재

### 메서드 호출 방법
> `데이터 타입 객체.메서드()`
>
> `'hello'.capitalize()`

### 메서드 호출 예시
```python
# 문자열 메서드 예시
print('hello'.capitalize())  # Hello


# 리스트 메서드 예시
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)  # [1, 2, 3, 4]
```

## 시퀀스 데이터 구조

### 문자열

#### 문자열 조회/탐색 및 검증 메서트

#### `.index(x)`
- x의 첫 번째 위치를 반환. 없으면 오류 발생
```python
print('banana'.index('a'))  # 1

print('banana'.index('z'))  # ValueError: substring not found
```

#### `.isupper(x)/ .islower(x)`
- 문자열이 모두 대문자/소문자로 이루어져 있는지 확인
```python
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper()) # True
print(string2.isupper()) # False
print(string1.islower()) # False
print(string2.islower()) # False
```

#### `.isalpha(x)`
- 문자열이 알파벳으로만 이루어져 있는지 확인
```python
string1 = 'Hello'
string2 = '123'
print(string1.isalpha()) # True
print(string2.isalpha()) # False
```

#### `find(x)`
- x의 첫 번째 위치를 반환, 없으면 `-1`을 반환
``` python
print('banana'.find('a')) # 1

print('banana'.find('z')) # -1
```

### 문자열 조작 메서드 (새 문자열 반환)

#### `.replace(old, new[,count])`
- 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
``` python
text = 'Hello, world!'
new_text = text.replace('world', 'Python')
print(new_text) # Hello, Python!
```

#### `.strip([chars])`
- 문자열의 시작과 끝에 있는 공백 혹은 지정된 문자를 제거
``` python
text = '   Hello, world!   '
new_text = text.strip()
print(new_text) # 'Hello, world!'
```

#### `split(sep=None, maxsplit=-1)`
- 지정한 문자를 구분자로 문자열을 분리하여 문자열의 리스트로 반환

```python
text = 'Hello, world!'
words = text.split(',')
print(words) # ['Hello', ' world!']
```

#### `'separator'.join([iterable])`
- iterable 요소들을 원래의 문자열을 구분자로 이용하여 하나의 문자열로 연결
``` python
words = ['Hello', 'world!']
text = '-'.join(words)
print(text) # 'Hello-world!'
```

#### 기타
```python
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
new_text2 = text.title()
new_text3 = text.upper()
new_text4 = text.swapcase()

print(new_text1) # Hello, world!
print(new_text2) # Hello, World!
print(new_text3) # HELLO, WORLD!
print(new_text4) # HEllO, WOrLD!
```

#### 메서드 이어서 사용하기
```python
text = 'heLLo, woRld!'

new_text = text.swapcase().replace('l', 'z')

print(new_text) # HEzzO, WOrLD!
```

## 리스트

### 리스트 값 추가 및 삭제 메서드

#### `.append(x)`
- 리스트 마지막에 항목 x를 추가
```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list) # [1, 2, 3, 4]
```

#### `.extend(iterable)`
- 리스트에 다른 반복 가능한 객체의 모든 항목을 추가
```python
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list) # [1, 2, 3, 4, 5, 6]
```

#### `.insert(i, x)`
- 리스트의 지정한 인덱스 i위치에 항목 x를 삽입
```python
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list) # [1, 5, 2, 3]
```

#### `.remove(x)`
- 리스트에서 첫 번째로 일치하는 항목을 삭제
```python
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)  # [1, 3]
```

#### `.pop(i)`
- 리스트에서 지정한 인덱스의 항목을 제거하고 반환, 작성하지 않을 경우 마지막 항목을 제거
```python
my_list = [1, 2, 3, 4, 5]

item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1) # 5
print(item2) # 1
print(my_list) # [2, 3, 4]
```

#### `.clear()`
- 리스트의 모든 항목을 삭제
```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list) # []
```
### 리스트 탐색 및 정렬 메서드
#### `.index(x)`
- 리스트에서 첫 번째로 일치하는 항목의 인덱스를 반환
```python
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)  # 1
```

#### `.count(x)`
- 리스트에서 항목 x가 등장하는 횟수를 반환
```python
my_list = [1, 2, 2, 3, 3, 3]
count = my_list.count(3)
print(count)  # 3
```

#### `.sort()`
- 원본 리스트를 오름차순으로 정렬
```python
my_list = [3, 2, 1]
my_list.sort()
print(my_list)  # [1, 2, 3]
# 내림차순
my_list.sort(reverse=True)
print(my_list)  # [3, 2, 1]
```

#### `.reverse()`
- 리스트의 순서를 역순으로 변경(정렬 X)
```python
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list)  # [9, 1, 8, 2, 3, 1]
```

## 비시퀀스 데이터 구조

### 세트 `set`
고유한 항목들의 정렬되지 않은 컬렉션

### 세트 메서드

#### `.add(x)`
- 세트에 x를 추가
```python
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.add(4)
print(my_set)  # {1, 'b', 3, 2, 'c', 'd', 'a’}

my_set.add(4)
print(my_set)  # {1, 'b', 3, 2, 'c', 'd', 'a’}
```

#### `.clear()`
- 세트의 모든 항목을 제거
```python
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.clear()
print(my_set)  # set()
```

#### `.remove(x)`
- 세트에서 항목 x를 제거
```python
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.remove(2)
print(my_set)  # {'b', 1, 3, 'c', 'a'}

my_set.remove(10)
print(my_set)  # KeyError
```

#### `.discard()`
- 세트 s에서 항목 x를 제거. remove와 달리 에러 없음
```python
my_set = {1, 2, 3}

my_set.discard(2)
print(my_set)  # {1, 3, 'a', 'c', 'b’}

my_set.discard(10)
```

#### `.pop()`
- 세트에서 임의의 요소를 제거하고 반환
```python
my_set = {'a', 'b', 'c', 1, 2, 3}

element = my_set.pop()
print(element)  # 1
print(my_set)  # {2, 3, 'b', 'a', 'c'}
```

#### `.update(iterable)`
- 세트에 다른 iterable 요소를 추가
```python
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.update([1, 4, 5])
print(my_set)  # {1, 2, 3, 'c', 4, 5, 'b', 'a'}
```

### 세트의 집합 메서드

#### 세트의 집합 메서드 1
```python
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}

print(set1.difference(set2))  # {0, 2, 4}
print(set1.intersection(set2))  # {1, 3}
print(set1.issubset(set2))  # False
print(set1.issuperset(set2))  # False
print(set1.union(set2))  # {0, 1, 2, 3, 4, 5, 7, 9}
```

## 딕셔너리 `dictionary`
고유한 항목들의 정렬되지 않은 컬렉션

### 딕셔너리 메서드

#### `.clear()`
- 딕셔너리 D의 모든 키/값 쌍을 제거
``` python
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person)  # {}
```

#### `.get(key[,default])`
- 키 연결된 값을 반환하거나 키가 없으면 None 혹은 기본 값을 반환
```python
person = {'name': 'Alice', 'age': 25}

print(person.get('name'))  # Alice
print(person.get('country'))  # None
print(person.get('country', 'Unknown'))  # Unknown
```

#### `.keys()`
- 딕셔너리 키를 모은 객체를 반환
```python
person = {'name': 'Alice', 'age': 25}
print(person.keys())  # dict_keys(['name', 'age’])

for k in person.keys():
    print(k)
"""
name
age
"""
```

#### `.values()`
- 딕셔너리 값을 모은 객체를 반환
```python
person = {'name': 'Alice', 'age': 25}
print(person.keys())  # dict_keys(['name', 'age’])

for v in person.values():
    print(v)
"""
Alice
25
"""
```

#### `.items()`
- 딕셔너리 키/값 쌍을 모은 객체를 반환
```python
person = {'name': 'Alice', 'age': 25}

print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])
for k, v in person.items():
    print(k, v)
"""
name Alice
age 25
"""
```

#### `.pop(key[,default])`
- 키를 제거하고 연결됐던 값을 반환 (없으면 에러나 default 를 반환)
```python
person = {'name': 'Alice', 'age': 25}

print(person.pop('age'))  # 25
print(person)  # {'name': 'Alice'}
print(person.pop('country', None))  # None
print(person.pop('country'))  # KeyError
```

#### `.setdefault(key[,default])`
- 키와 연결된 값을 반환, 키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환
```python
person = {'name': 'Alice', 'age': 25}

print(person.setdefault('country', 'KOREA'))  # KOREA
print(person)  # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}
```

#### `.update([other])`
- other가 제공하는 키/값 쌍으로 딕셔너리를 갱신, 기존 키는 덮어씀
```python
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person)
print(person)  # {'name': 'Jane', 'age': 25, 'gender': 'Female'}

person.update(age=50)
print(person)  # {'name': 'Jane', 'age': 50, 'gender': 'Female'}

person.update(country='KOREA')
print(person)  # {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'KOREA'}
```

## 복사

### 데이터 타입과 복사
- 파이썬에서는 데이터에 분류에 따라 복사가 달라짐
- "변경 가능한 데이터 타입"과 "변경 불가능한 데이터 타입"을 다르게 다룸

```python
# 가변 데이터 타입
a = [1, 2, 3, 4]
b = a
a[0] = 100
print(a) # [100, 2, 3, 4]
print(b) # [100, 2, 3, 4]
# 불변 데이터 타입
a = 9
b = a
b = 100
print(b) # 100
print(a) # 9
```

### 복사 유형
1. 할당
- 할당 연산자 (`=`)를 통한 복사는 해당 객체에 대한 객체 참조를 복사
``` python
# 할당
original_list = [1, 2, 3]
copy_list = original_list

copy_list[0] = 'hello'
print(original_list) # ['hello', 2, 3]
```

2. 얕은 복사
```python
a = [1, 2, 3]
b = a[:] # 슬라이싱은 자른 "새로운 리스트"를 반환

b[0] = 100
print(a) # [1, 2, 3]

# 얕은 복사의 한계
a = [1, 2, [100, 200]]
b = a[:]

b[2][0] = 999
print(a) # [1, 2, [999, 200]]
# a와 b의 주소는 다르지만 내부 객체의 주소는 같기 때문에 함께 변경됨
```

3. 깊은 복사
- 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 함
```python
import copy

original_list = [1, 2, [1, 2]]
deep_copy_list = copy.deepcopy(original_list)

deep_copy_list[2][0] = 100

print(original_list) # [1, 2, [1, 2]]
print(deep_copy_list) # [1, 2, [100, 2]]
```

## 참고
문자열에 포함된 문자들의 유형을 판별하는 메서드
- `isdecimal()`
  - 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True
- `isdigit()`
  - `isdigit()`과 비슷하지만, 유니코드 숫자도 인식 ('①’ 도 숫자로 인식)
- `isnumeric()`
  - `isdigit()`과 유사하지만, 몇 가지 추가적인 유니코드 문자들을 인식, (분수, 지수, 루트 기호도 숫자로 인식)