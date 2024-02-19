import random

emails = ["outlook", "gmail", "hotmail", "yahoo"]
domain = random.choice(emails)

def email(firstname, lastname, birthday, domain):
    first = str(firstname[:2])
    last = str(lastname[-2:])
    birth = str(birthday[:2])

    final_email = first + last + birth + "@"+ domain + ".com"
    print("Your email is:", final_email)

firstname = input("What's your firstname? ")
lastname = input("What's your lastname? ")
birthday = input("What's your birthday? (day/month/year) ")

email(firstname, lastname, birthday, domain)