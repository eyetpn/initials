
def get_initials(fullname):
    words = fullname.split()
    initials = ""
    for word in words:
      word= word.capitalize()
      initials = initials + word[0:1]
    return initials

def main():
    fullname = str(input("What is your full name?"))
    print ("The initials of", fullname,"are",get_initials(fullname))
if __name__ == '__main__':
    main ()

