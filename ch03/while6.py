import random
want_more_advice="y"
# 답을 튜플에 넣습니다.
answers = ( "자! 해보세요!",
"됐네요, 이 사람아",
"뭐라고? 다시 생각해보세요.",
"모르니 두려운 것입니다.",
"칠푼인가요?? 제 정신이 아니군요!",
"당신이라면 할 수 있어요!",
"해도 그만, 안 해도 그만, 아니겠어요?",
"맞아요, 당신은 올바른 선택을 했어요."
)
print("MyMagicBall에 오신 것을 환영합니다.")
# 사용자의 이름을 입력받습니다 (print문의 인자로 sep="" 인자를 주면 공백 제거)
user_name = input("안녕하세요. 여러분의 이름을 입력하세요.\n")
print("만나서 반가워요", user_name, ".", sep="")
ant_more_advice="y"
while(want_more_advice == "y"):
    # 사용자의 질문을 입력 받습니다.
    question = input("조언을 구하고 싶으면 질문을 입력하고 엔터 키를 누르세요.\n")
    print("고민 중 ...\n" * 4)
    # 질문에 알맞은 답변을 하는 일에 randint() 함수를 활용합니다.
    choice=random.randint(0, 7)
    # 화면에 답변을 출력합니다.
    print(answers[choice])
    want_more_advice = input("\n다른 조언을 더 구하시겟어요?? y/n\n")
    # 이제 종료합니다.
print("\n\n안녕히가세요 ", user_name, ". 게임을 즐겨줘서 고맙습니다.", sep="")
input("\n\n마치려면 엔터 키를 누르세요.")