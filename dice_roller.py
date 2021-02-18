def main():
    import random
    dice_rolls = int(input('How many dice would you like to roll'))
    dice_size = int(input('How many sides are the dice?'))
    dice_sum = 0
    for i in range(0,dice_rolls):
    
        roll = random.randint(1,dice_size)
        dice_sum += roll
        if roll == 1: 
            print('You rolled a {0}! Critical Fail!'.format(roll))
        elif roll == dice_size:
            print('Your rolled a {0}! Critical Success!'.format(roll))
        else:
            print('You rolled a {0}'.format(roll))
    print('You have rolled a total of {0}'.format(dice_sum))

if __name__== "__main__":
    main() 
