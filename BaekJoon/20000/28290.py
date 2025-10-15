typing = input()

if typing in ("fdsajkl;", "jkl;fdsa"):
    print("in-out")
elif typing in ("asdf;lkj", ";lkjasdf"):
    print("out-in")
elif typing == "asdfjkl;":
    print("stairs")
elif typing == ";lkjfdsa":
    print("reverse")
else:
    print("molu")