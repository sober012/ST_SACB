import openai
import re

# OpenAI API 키 설정
openai.api_key = 'openai-api-key'

def evaluate_password_strength(password):
    """
    암호의 강도를 평가하고 개선 사항을 제안하는 함수.
    
    :param password: 평가할 암호 문자열
    :return: 암호 강도 평가 결과
    """
    messages = [
        {"role": "system", "content": "당신은 사이버보안 전문가입니다."},
        {"role": "user", "content": f"다음 암호의 강도를 평가하고, 강도를 향상시킬 수 있는 구체적인 방법을 제안해주세요.\n\n암호: {password}"}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # GPT-4 모델 사용
            messages=messages,
            max_tokens=150,
            temperature=0.3  # 응답의 일관성을 높이기 위해 낮은 값 설정
        )
        evaluation = response['choices'][0]['message']['content'].strip()
        return evaluation
    except Exception as e:
        return f"Error evaluating password: {str(e)}"

def is_common_password(password):
    """
    암호가 일반적으로 사용되는지 확인하는 함수.
    간단한 정규 표현식을 사용하여 공통 패턴을 확인합니다.
    
    :param password: 확인할 암호 문자열
    :return: 공통 암호 여부 (True/False)
    """
    common_patterns = [
        r"^(password|123456|123456789|qwerty|abc123|111111)$",
        r"^(letmein|welcome|admin|login|monkey|dragon)$"
    ]
    for pattern in common_patterns:
        if re.match(pattern, password.lower()):
            return True
    return False

if __name__ == "__main__":
    print("=== 암호 강도 평가 도구 ===")
    user_password = input("평가할 암호를 입력하세요: ")

    # 공통 암호 확인
    if is_common_password(user_password):
        print("\n경고: 입력하신 암호는 일반적으로 사용되는 암호입니다. 더 안전한 암호를 사용하시기 바랍니다.")
    else:
        # OpenAI API를 사용하여 암호 강도 평가
        result = evaluate_password_strength(user_password)
        print("\n암호 강도 평가 결과:")
        print(result)
