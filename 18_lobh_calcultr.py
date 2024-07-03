n1 = input("Enter your name : ")
n2 = input("Enter his/her name : ")

combine_str = n1 + n2

lower_case_str = combine_str.lower()

t = lower_case_str.count('t')
r = lower_case_str.count('r')
u = lower_case_str.count('u')
e = lower_case_str.count('e')

true = t + r + u + e

l = lower_case_str.count('l')
o = lower_case_str.count('o')
v = lower_case_str.count('v')
e = lower_case_str.count('e')

love = l + o + v + e


pyara_score = int(str(true) + str(love))

if pyara_score < 10 or pyara_score > 90:
    print(f"Your lobh skor is {pyara_score} and you go like coke and mentos")
elif pyara_score >= 40 and pyara_score <= 50:
    print(f"Your lobh skor is {pyara_score} and you fuks are alrit togther")
else:
    print(f"Your lobh skor is {pyara_score} and fuk mate")