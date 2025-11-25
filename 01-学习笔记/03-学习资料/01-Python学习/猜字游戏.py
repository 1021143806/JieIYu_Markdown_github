#创建单词库
import random
words=['chicken','duck','pig','dog','cat','fish','rabbit','turtle','hamster','snake','frog','horse','cow','sheep','goat','donkey']
def pickWord():
    return random.choice(words)#随机选择一个单词
#print(pickWord())

#游戏结构
guessTimes = 14
def play():
    word = pickWord()  # 随机选择一个单词
    print(word)
    while True:
        guess = getGuess(word)  # 获取用户猜测
        if processGuess(guess,word):
            print("You win!")
            break
        if guessTimes == 0:
            print("You lose! The word was:", word)
            break
def getGuess(word):
    return 'a'
def processGuess(guess,word):
    global guessTimes
    guessTimes = guessTimes -1
    return False
play()