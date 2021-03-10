""" Mad Libs Generator
------------------------------------
"""

loop = 1
while (loop<3):
    noun = input("Choose a noun:{} ")
    p_noun = input("Shoose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("name a place: ")
    noun3 = input("Choose a noun: ")
    print("--------------------------")
    print("Be kind to your",noun,"-footed", p_noun)
    print("For a duck may be somebody's", noun2,",")
    print("Be kind to your",p_noun,"in",place)
    print("Where the weather is always",adjective,".")
    print()
    print("You may think that is this the",noun2,",")
    print("Well it is.")
    print("-------------------------")
    loop = loop + 1      
