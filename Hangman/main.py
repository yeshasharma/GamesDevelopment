import  json
import  requests
import random

from ui import stages, logo

print(logo)






def getWordsThroughApi(api_key, api_id, url):
    try: 
        # url = f"https://od-api-sandbox.oxforddictionaries.com/api/v2/{endpoint}/{language_code}/{word_id}"
        # r = requests.get(url, headers = {"app_id": api_id, "app_key": api_key})
    
        res = requests.get(url)
        # print("code {}\n".format(r.status_code))
        # print("text \n" + r.text)
        
        if res.status_code == 200:
            return res.json()
    except Exception as e:
            print(f"API error: {e}")
            return ["Money", "Monkey", "Title", "Total", "Yes", "No"]

def hangman():
    api_key = "49fceae9fc1be49170263d257885fc08"
    api_id = "c83e52be"
    # endpoint = "entries"
    # language_code = "en-us"
    # word_id = "ace"
    # letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    url = "https://random-word-api.herokuapp.com/word?number=102"
    words_list = getWordsThroughApi(api_key, api_id, url)

    word = random.choice(words_list).lower()
    print("word>>>>>", word, words_list)

    placeholder = ""
    for letter in range(len(word)):
        placeholder += " _ "

    print(placeholder)

    lives = 6

    correct_guessed_letters = []
    incorrect_guessed_letters = []

    game_over = False

    while not game_over:
        guess = input("Enter your guess: ")

        correct_guess = ""
        for letter in word:
            if letter == guess:
                correct_guess += letter
                correct_guessed_letters.append(letter)
            elif letter in correct_guessed_letters:
                correct_guess += letter
            else:
                correct_guess += " _ "

        if guess not in word:
            lives -= 1
            if guess in incorrect_guessed_letters:
                    print(f"You have already guessed {guess}, we are not deducting the life")
            incorrect_guessed_letters.append(guess)
            if lives == 0:
                game_over = True
                print(f"You loose.{word}")
            
        print(stages[lives])
        
        if " _ " not in correct_guess:
            game_over = True
            print("You win.")
        
        print(correct_guess, lives)


if __name__ == "__main__":
     hangman()
