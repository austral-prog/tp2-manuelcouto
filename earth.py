def earth():
    x = "Bangladesh"
    y = "Barbados"

    isXlower=x<y
    isYlower=y<x

    message1=f"The result of {x} comes first in the dictionary than {y} is {isXlower}."
    message2=f"The result of {y} comes first in the dictionary than {x} is {isYlower}."

    print(message1)
    print(message2)
