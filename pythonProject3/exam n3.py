def card_unseen(card):
    if len(str(card)) > 16:
        return False
    else:
        return '*' * (len(card) - 4) + card[-4:] == card
while True:
    card = input("Введите номер карты: ")
    print(f"{card}" if card_unseen(card) else "error")
# задание 1 - не работает


#задание 2
# def palindrome(s):
#     return s[::-1] == s
# while True:
#     s = input("Введите слово: ")
#     print(f"{s} is palindrome!" if palindrome(s) else "not a palindrome")