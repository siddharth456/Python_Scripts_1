'''the function ask_ok is called with 1 mandatory argument and 2 optional arguments'''
def ask_ok(prompt,retries=4,reminder="Ok!!Lets try again"):
    while True:
        ok=input(prompt)
        if ok in ('Y','Ye','Yes'):
            print('You said '+ok)
            break
        elif ok in ('N','No','Nop','Nope'):
            print('You said '+ok)
        retries=retries-1
        if retries<0:
            raise ValueError("invalid user response")
        print(reminder)
ask_ok("Do you really want to Quit??? :")