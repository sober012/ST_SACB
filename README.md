## 암호 강도 평가 도구

기능: 사용자가 입력한 암호의 강도를 평가하고 개선할 점을 제안하는 도구.

사용 방법: 사용자가 비밀번호를 입력하면, 도구가 이를 분석하여 강도(길이, 복잡성, 일반적인 패턴 사용 여부)를 평가하고 더 안전한 비밀번호를 추천.

응용 예시:

조직 내 비밀번호 보안 강화.

일반 사용자들이 강력한 비밀번호를 생성하도록 도와줌

###  evaluate_password_strength(password) 함수

함수는 GPT-4 API를 호출하여 입력된 암호의 강도를 평가합니다.

messages 리스트에는 대화의 맥락이 담기며, "system" 역할은 GPT-4에게 사이버 보안 전문가 역할을 하도록 지시하고, "user" 역할은 암호의 강도를 평가해 달라는 요청입니다.

### is_common_password(password) 함수

함수는 암호가 너무 일반적인 패턴인지 확인하는데 사용됩니다.

암호를 정규 표현식을 사용하여 "password", "123456", "qwerty" 등 일반적으로 자주 사용되는 암호 패턴과 비교합니다.

### 메인 코드 블록 (if __name__ == "__main__":) 

프로그램의 메인 부분으로, 사용자가 입력한 암호에 대해 공통 암호 여부를 확인하고, 공통 암호가 아니면 GPT-4 모델을 사용하여 암호의 강도를 평가합니다.

### 단순한 암호 입력시
![image](https://github.com/user-attachments/assets/3fd87d24-2680-4d6f-918b-f8ff00246bbb)

![image](https://github.com/user-attachments/assets/27453fa1-3be2-4e70-bf33-b93bdeecabcc)


### 강력한 암호 입력시
![image](https://github.com/user-attachments/assets/34e13eb8-5cab-427c-89a2-7046e6fbcab7)

![image](https://github.com/user-attachments/assets/cc4775e0-6abc-4623-b573-2a0ae0e96597)

