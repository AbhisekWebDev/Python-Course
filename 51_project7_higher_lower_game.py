import random

celebrities_info = [
    {
        'name': 'Cristiano Ronaldo',
        'followers': 550000000,
        'profession': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Kylie Jenner',
        'followers': 380000000,
        'profession': 'Businesswoman/Model',
        'country': 'USA'
    },
    {
        'name': 'Elon Musk',
        'followers': 150000000,
        'profession': 'CEO of Tesla/SpaceX',
        'country': 'USA'
    },
    {
        'name': 'Virat Kohli',
        'followers': 250000000,
        'profession': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Ariana Grande',
        'followers': 230000000,
        'profession': 'Singer/Actress',
        'country': 'USA'
    },
    {
        'name': 'Lionel Messi',
        'followers': 450000000,
        'profession': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Jeff Bezos',
        'followers': 3000000,
        'profession': 'Founder of Amazon',
        'country': 'USA'
    },
    {
        'name': 'Taylor Swift',
        'followers': 250000000,
        'profession': 'Singer/Songwriter',
        'country': 'USA'
    },
    {
        'name': 'Dwayne Johnson',
        'followers': 350000000,
        'profession': 'Actor/Wrestler',
        'country': 'USA'
    },
    {
        'name': 'Selena Gomez',
        'followers': 300000000,
        'profession': 'Singer/Actress',
        'country': 'USA'
    },
    {
        'name': 'LeBron James',
        'followers': 150000000,
        'profession': 'Basketball Player',
        'country': 'USA'
    },
    {
        'name': 'Oprah Winfrey',
        'followers': 43000000,
        'profession': 'TV Host/Producer',
        'country': 'USA'
    },
    {
        'name': 'Mark Zuckerberg',
        'followers': 12000000,
        'profession': 'CEO of Facebook',
        'country': 'USA'
    },
    {
        'name': 'Bill Gates',
        'followers': 60000000,
        'profession': 'Co-founder of Microsoft',
        'country': 'USA'
    },
    {
        'name': 'Shakira',
        'followers': 200000000,
        'profession': 'Singer',
        'country': 'Colombia'
    }
]


art = """
    ___ ___ .___  ________  ___ ________________________  
 /   |   \|   |/  _____/ /   |   \_   _____/\______   \ 
/    ~    \   /   \  ___/    ~    \    __)_  |       _/ 
\    Y    /   \    \_\  \    Y    /        \ |    |   \ 
 \___|_  /|___|\______  /\___|_  /_______  / |____|_  / 
       \/             \/       \/        \/         \/  
.____    ________  __      _______________________      
|    |   \_____  \/  \    /  \_   _____/\______   \     
|    |    /   |   \   \/\/   /|    __)_  |       _/     
|    |___/    |    \        / |        \ |    |   \     
|_______ \_______  /\__/\  / /_______  / |____|_  /     
        \/       \/      \/          \/         \/      
  ________    _____      _____  ___________             
 /  _____/   /  _  \    /     \ \_   _____/             
/   \  ___  /  /_\  \  /  \ /  \ |    __)_              
\    \_\  \/    |    \/    Y    \|        \             
 \______  /\____|__  /\____|__  /_______  /             
        \/         \/         \/        \/              
"""


print(art)

score = 0

def display_account_info(account):
    name = account['name']
    followers = account['followers']
    profession = account['profession']
    country = account['country']

    return f"{name} {followers} {profession} {country}\n"

def check_answer(guess, follower1, follower2):
    if follower1 < follower2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            return False

flag = True

account2 = random.choice(celebrities_info)

while flag:
    account1 = account2

    account2 = random.choice(celebrities_info)

    while account1 == account2:
        account2 = random.choice(celebrities_info)

    print(f"Compare 1 : {display_account_info(account1)}\n VS. \n\nCompare 2 : {display_account_info(account2)}")

    guess = int(input("Who has more followers? Type 1 or 2 : "))

    follower1 = account1['followers'] 
    follower2 = account2['followers']

    is_correct = check_answer(guess, follower1, follower2)

    if is_correct:
        score += 1
        print(f"\nYou right, your score is : {score} \n")
    else:
        print(f"\nYou wrong, your score is : {score} \n")

        flag = False