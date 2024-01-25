## 상속 `Inheritance`

기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것

### 상속이 필요한 이유
1. 코드 재사용
  - 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음
  - 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용할 수 있으며, 중복된 코드를 줄일 수 있음

2. 계층 구조
- 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
- 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음

3. 유지 보수의 용이성
- 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지 보수가 용이해짐
- 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음

### 클래스 상속

#### 상속 없이 구현하는 경우 (1/2)

- 학생/교수 정보를 나타내기 어려움
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')


s1 = Person('김학생', 23)
s1.talk() # 반갑습니다. 김학생입니다.

p1 = Person('박교수', 59)
p1.talk() # 반갑습니다. 박교수입니다.
```

#### 상속 없이 구현 하는 경우 (2/2)

- 메서드 중복 정의

```python
class Professor:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def talk(self): # 중복
        print(f'반갑습니다. {self.name}입니다.')

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def talk(self): # 중복
        print(f'반갑습니다. {self.name}입니다.')
```

### 상속을 사용한 게층구조 변경

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self): # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')


class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department


class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa


p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 Person 클래스의 talk 메서드를 활용
p1.talk() # 반갑습니다. 박교수입니다.

# 부모 Person 클래스의 talk 메서드를 활용
s1.talk() # 반갑습니다. 김학생입니다.
```

`super()`
- 부모 클래스 객체를 반환하는 내장 함수

- 사용전
``` python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id
```
- 사용후
```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # 부모클래스의 init 메서드 호출
        super().__init__(name, age, number, email)
        self.student_id = student_id
```

### 다중 상속
- 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

#### 다중 상속 예시
```python
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'


baby1 = FirstChild('아가')
print(baby1.cry()) # 첫째가 응애
print(baby1.swim()) # 첫째가 수영
print(baby1.walk()) # 아빠가 걷기
print(baby1.gene) # XY
```

### MRO (Method Resolution Order)
- 메서드 결정 순서


`super()`
- 부모 클래스 객체를 반환하는 내장 함수
- 다중 상속 시 MRO를 기반으로 현재 클래스가 상속하는 모든 부모 클래스 중 다음에 호출될 메서드를 결정하여 자동으로 호출

#### super 사용 예시 - 1
```python
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'
    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'
    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__() # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child'
    def show_value(self):
        super().show_value() # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')

child = Child()
child.show_value()

# Value from ParentA: ParentA
# Value from Child: Child
```

#### super 사용 예시 - 2
```python
class A:
    def __init__(self):
        print('A Constructor')

class B(A):
    def __init__(self):
        super().__init__()
        print('B Constructor')

class C(A):
    def __init__(self):
        super().__init__()
        print('C Constructor')
        
class D(B, C):
    def __init__(self):
        super().__init__()
        print('D Constructor')

obj = D()
print(D.mro())

# A Constructor
# C Constructor
# B Constructor
# D Constructor
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

### `mro()`메서드
- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가졌는지 확인하는 메서드
- 기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 -> 자식 클래스 -> 부모 클래스로 확장

### super 의 2가지 사용 사례
1. 단일 상속 구조
  - 명시적으로 이름을 지정하지 않고 부모 클래스를 참조할 수 있으므로, 코드를 더 유지 관리하기 쉽게 만들 수 있음
  - 클래스 이름이 변경되거나 부모 클래스가 교체되어도 `super()`을 사용하면 코드 수정이 더 적게 필요

2. 다중 상속 구조
  - `MRO`를 따른 메서드 호출
  - 복잡한 다중 상속 구조에서 발생할 수 있는 문제를 방지


## 에러와 예외

### 디버깅
#### 버그 `bug`
소프트웨어에서 발생하는 오류 또는 결함

프로그램의 예상된 동작과 실제 동작 사이의 불일치

#### 버그의 기원
- 최초의 버그는 1945년 프로그래밍 언어의 일종인 코볼 발명자 그레이스 호퍼가 발견
- 역사상 최초의 컴퓨터 버그는 Mark Ⅱ라는 컴퓨터 회로에 벌레인 나방이 들어가 합선을 일으켜 비정상적으로 동작한 것을 기록한 것
- "버그"라는 용어는 이전부터 사용되어 왔지만 이 사건을 계기로 컴퓨터 시스템에서 발생하는 오류 또는 결함을 지칭하는 용어로 널리 사용되기 시작


### Debugging
소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정

프로그램의 오작동 원인을 식별하고 수정하는 작업

### 디버깅 방법

1. print 함수 활용
  - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
2. 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
  - breakpoint, 변수 조회 등
3. Python tutor 활용 (단순 파이썬 코드인 경우)
4. 뇌 컴파일, 눈 디버깅 등

### 에러 `Error`
프로그램 실행 중에 발생하는 예외 상황

### 파이썬의 에러 유형
- 문법 에러 Syntax Error
  - 프로그램의 구문이 올바르지 않은 경우 발생 (오타, 괄호 및 콜론 누락 등의 문법적 오류)
- 예외 Exception
  - 프로그램 실행 중에 감지되는 에러


### 문법 에러 예시
- Invalid syntax (문법 오류)

`while # SyntaxError: invalid syntax`

- assign to literal (잘못된 할당)

`5=3 # SyntaxError: cannot assign to literal`
- EOL (End of Line)

`print('hello   
SyntaxError: EOL while scanning string literal)`
- EOF (End of File)

`print(
#SyntaxError: unexpected EOF while parsing)`

### 예외 `Exception`

프로그램 실행 중에 감지되는 에러

### 내장 예외 `Built-in Exceptions`
- 예외 상황을 나타내는 예외 클래스들
- 파이썬에서 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용

### 예외 예시

- ZeroDivisionError : 나누기 또는 모듈로 연산의 두 번째 인자가 0일 때 발생

`10/0 # ZeroDivisionError: division by zero`
- NameError : 지역 또는 전역 이름을 찾을 수 없을 때 발생

`print(name_error) # NameError: name 'name_error' is not defined`
- TypeError

  - 타입 불일치

   `'2' + 2  # TypeError: can only concatenate str (not "int") to str`
  - 인자 누락

  `sum()  # TypeError: sum() takes at least 1 positional argument (0 given)`
  - 인자 초과

  `sum(1, 2, 3)  # TypeError: sum() takes at most 2 arguments (3 given)`
  - 인자 타입 불일치

  ```python
  import random
  random.sample(1, 2)

  # TypeError: Population must be a sequence.  For dicts or sets, use sorted(d).
  ```
  
- ValueError

  - 연산이나 함수에 문제가 없지만 부적절한 값을 가진 인자를 받았고, 상황이 IndexError 처럼 더 구체적인 예외로 설명되지 않는 경우 발생
`  int('1.5') # ValueError: invalid literal for int() with base 10: '3.5'`

`  range(3).index(6) # ValueError: 6 is not in range`

- IndexError – 시퀀스 인덱스가 범위를 벗어날 때 발생
  ```python
  empty_list = []
  empty_list[2]
  # IndexError: list index out of range
  ```

- KeyError – 딕셔너리에 해당 키가 존재하지 않는 경우
  ```python
  person = {'name': 'Alice'}
  person['age']  # KeyError: 'age'
  ```

- ModuleNotFoundError - 모듈을 찾을 수 없을 때 발생

  `import hahaha  # ModuleNotFoundError: No module named 'hahaha'`

- ImportError – 임포트 하려는 이름을 찾을 수 없을 때 발생

  `from random import hahaha`

  `# ImportError: cannot import name 'hahaha' from 'random'`

- KeyboardInterrupt – 사용자가 Control-C 또는 Delete를 누를 때 발생

    - 무한루프 시 강제 종료
  ```python
  while True: 
      continue

  '''
  Traceback (most recent call last):
    File "...", line 2, in <module>
      continue
  KeyboardInterrupt
  '''
  ```

- IndentationError - 잘못된 들여쓰기와 관련된 문법 오류
  ```python
  for i in range(10):
  print(i) # IndentationError: expected an indented block
  ```
