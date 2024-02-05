def isPalindrom(txt):
    text=txt[::-1]
    if(text==txt):
        print('Yes,it is palindrom')
    else:
        print("No,it is not palindrom")
isPalindrom(input())