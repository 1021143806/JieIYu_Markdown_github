guess_me = 7
number = 1
while 1 :
    if number < guess_me :
        print ('too low')
        number += 1
    elif number == guess_me:
        print ('found it!')
        break
    else :
        print ('oops')
        break