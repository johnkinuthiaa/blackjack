import random
from art import logo #ascii art for the name blackjack
def blackjack():
    print(logo)
    def deal_cards():
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        card = random.choice(cards)
        return card

    user_card = []
    computer_card = []
    is_game_over =False

    def calculate_score(cards):
        if sum(cards) ==21 and len(cards) ==2:
            return 0
        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "draw"
        elif computer_score == 0:
            return "lose, opponent has a blackjack"
        elif user_score == 0:
            return "win with a black jack"
        
        elif user_score >21:
            return "you went over!you loose"
        elif computer_score > 21:
            return "opponent went over! you win"
        elif user_score> computer_score:
            return"you win"
        else:
            return"you loose"


    for _ in range(2):
        user_card.append(deal_cards())
        computer_card.append(deal_cards())
    while is_game_over ==False:
        user_score = calculate_score(user_card)
        computer_score =calculate_score(computer_card)


        print(f" your cards: {user_card} and your score {user_score}")
        print(f" computer card: {computer_card[0]} ")

        if user_score ==0 or computer_score == 0 or user_score>21:
            is_game_over =True
        else:
            user_should_deal = input("type 'y' to get another card or 'n' to pass: ").lower()
            if user_should_deal =="y":
                user_card.append(deal_cards())
            else:
                is_game_over = True

    while computer_score !=0 and computer_score <17:
        computer_card.append(deal_cards)
        computer_score = calculate_score(computer_card)
    print(f"your final deck is {user_card}, and final score is {user_score}")
    print(f"computer final deck is {computer_card}, and final score is {computer_score}")
    print(compare(user_score,computer_score))
blackjack()

