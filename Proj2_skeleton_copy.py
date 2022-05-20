#
# Name: Zimin Lu
#

from Proj2_tree import printTree

#
# The following two trees are useful for testing.
#
smallTree = \
    ("Is it bigger than a breadbox?",
        ("an elephant", None, None),
        ("a mouse", None, None))
mediumTree = \
    ("Is it bigger than a breadbox?",
        ("Is it gray?",
            ("an elephant", None, None),
            ("a tiger", None, None)),
        ("a mouse", None, None))

def main():
    """DOCSTRING!"""
    # Write the "main" function for 20 Questions here.  Although
    # main() is traditionally placed at the top of a file, it is the
    # last function you will write.

    # if isLeaf(mediumTree[1][2]):
    #     print('is a leaf')
    # else:
    #     print('is not a leaf')

    # if yes():
    #     print('yes')
    # else:
    #     print('no')

    # printTree(mediumTree)
    TF = simplePlay(mediumTree)

    print(TF)



def simplePlay(tree):
    """DOCSTRING!"""
    # 1. If the tree is a leaf, ask whether the object is the object named in the leaf.
    # Return True or False appropriately.
    # 2. If the tree is not a leaf, ask the question in the tree, that is tree[0]
        # If the user answers "yes", call yourself recursively on the subtree that is the second element in the triple.
        # If the user answers "no", recur on the subtree that is the third element in the triple.
    while True:
        if isLeaf(tree):
            content = input(f'I guess it is {tree[0]}, am I correct? Enter \"yes\" or \"no\": ')
            while True:
                if content == 'yes':
                    return True
                    break
                elif content == 'no':
                    return False
                    break
                else:
                    content = input(f'Not a valid input, I guess it is {tree[0]}, am I correct? Enter \"yes\" or \"no\": ')
                    continue
        else:
            # content = input(f'{tree[0]} Enter \"yes\" or \"no\": ')
            # while True:
            #     if content == 'yes':
            #         tree = tree[1]
            #         break
            #     elif content == 'no':
            #         tree = tree[2]
            #         break
            #     else:
            #         content = input(f'Not a valid input, {tree[0]} Enter \"yes\" or \"no\": ')
            content = input(f'{tree[0]} Enter \"yes\" or \"no\": ')
            if content == 'yes':
                tree = tree[1]
                simplePlay(tree)
            else:
                tree = tree[2]
                simplePlay(tree)





def play(tree):
    """DOCSTRING!"""


def isLeaf(tree):
    if (tree[1] == None) and (tree[2] == None):
        return True
    else:
        return False


def yes():
    content = input("Please enter \"yes\" or \"no\": ")  # default type: string
    while True:
        if content == 'yes':
            return True
        elif content == 'no':
            return False
        else:
            content = input("Not a valid input, please enter \"yes\" or \"no\": ")
            continue


def playLeaf(tree):
    return None

    
#
# The following two-line "magic sequence" must be the last thing in
# your file.  After you write the main() function, this line it will
# cause the program to automatically play 20 Questions when you run
# it.
#
if __name__ == '__main__':
    main()
