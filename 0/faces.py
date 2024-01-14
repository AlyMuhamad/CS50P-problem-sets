def main():
    emotion = input('what is your current emotions? ')
    convert(emotion)

def convert(revealed):
    revealed = revealed.replace(':)', '🙂').replace(':(', '🙁')
    print(revealed)

main()