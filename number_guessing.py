import random
attempts_list = []
def show_score():
    if len(attempts_list) <=0:
        print("there is currently no high score, it's yours for the taking!")
    else:
            print("The current high score is{} atempts".format(min(attemptes_list)))
def start_game():
    random_number = int(random.randint(1,10))
    print("Hello traveler! Welcom to the game of guesses!")
    player_name = input("What is your name? ")
    wanna_play = input("hi, {}, would you like to play the guessing game? (Enter Yes/no) ".format(player_name))
    attempts = 0
    schow_score()
    while wana_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10")
            if int(guess) < 1 or int(guess) >10:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print("Nice!you got it!")
                attempts +=1
                attempts_list.append(atempts)
                print":It took you {} attempts".format(attempts)
                play_again = unput("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("That's coolm have a good one!")
                    break
                elif int(guess) > random_number:
                    print("It's higher")
                    attempts += 1
        

    else:
        print("That's cool, have a good one!")
if __name__==;__main__':
    start_game()
