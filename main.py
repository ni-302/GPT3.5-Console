try:
    import sys
    import gpt
    from config import token

    while True:
        user_input = input("メッセージを入力 : ")
        gpt.chatgpt(user_input, token)

except KeyboardInterrupt:
    sys.exit()