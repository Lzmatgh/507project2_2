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
    # Prints a welcome message
    # Asks the user if they would like to load a tree from a file (optional, but bonus points as indicated above)
    # If the user didn't want to load from a file, the initial tree should be the smallTree.
    # Plays the game
    # Asks the user if they would like to play again, in which case we play again with the new tree
    # When the user is done playing, asks the user if they would like to save the ﬁle, in which case
    # the user is queried for a file name and the file is saved

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


    print('Welcome to 20 Questions!')
    loadornot = yes('Would you like to load a tree from a file? Enter \"yes\" or \"no\": ')
    if loadornot:
        filename = input('What\'s the name of the file? (e.g. tree1.txt) ')
        treefile = open(filename, 'r')
        tree1 = loadTree(treefile)
        treefile.close()
    else:
        tree1 = smallTree

    newtree = play(tree1)
    saveornot = yes('Would you like to save this tree for later? ')
    if saveornot:
        newfilename = input('Please enter a file name: ')
        treefile = open(newfilename, 'w')
        saveTree(newtree, treefile)
        treefile.close()
        print('Thank you! The file has been saved. ')

    print('Bye! ')




def simplePlay(tree):
    """DOCSTRING!"""
    # 1. If the tree is a leaf, ask whether the object is the object named in the leaf.
    # Return True or False appropriately.
    # 2. If the tree is not a leaf, ask the question in the tree, that is tree[0]
        # If the user answers "yes", call yourself recursively on the subtree that is the second element in the triple.
        # If the user answers "no", recur on the subtree that is the third element in the triple.
    if isLeaf(tree):
        content = input(f'I guess it is {tree[0]}, am I correct? Enter \"yes\" or \"no\": ')
        while True:
            if content == 'yes':
                return True
            elif content == 'no':
                return False
            else:
                content = input(f'Not a valid input, I guess it is {tree[0]}, am I correct? Enter \"yes\" or \"no\": ')
                continue
    else:
        content = input(f'{tree[0]} Enter \"yes\" or \"no\": ')
        while True:
            if content == 'yes':
                tree = tree[1]
                return simplePlay(tree)  # there is no return value when recursively call the function itself, so return the function
            elif content == 'no':
                tree = tree[2]
                return simplePlay(tree)
            else:
                content = input(f'Not a valid input, {tree[0]} Enter \"yes\" or \"no\": ')





def play(tree):
    """DOCSTRING!"""

    # tree_original = tree
    # index = []
    #
    # if isLeaf(tree):
    #     content = input(f'I guess it is {tree[0]}, am I correct? Enter \"yes\" or \"no\": ')
    #     while True:
    #         if content == 'yes':
    #             print('I got it!')
    #             return tree_original
    #         elif content == 'no':
    #             newleaf = playLeaf(tree[0])
    #             for idx in index:
    #                 new_tree = tree_original[idx]
    #         else:
    #             content = input(f'Not a valid input, I guess it is {tree[0]}, am I correct? Enter \"yes\" or \"no\": ')
    #             continue
    # else:
    #     content = input(f'{tree[0]} Enter \"yes\" or \"no\": ')
    #     while True:
    #         if content == 'yes':
    #             tree = tree[1]
    #             index.append(1)
    #             return simplePlay(tree)  # there is no return value when recursively call the function itself, so return the function
    #         elif content == 'no':
    #             tree = tree[2]
    #             index.append(2)
    #             return simplePlay(tree)
    #         else:
    #             content = input(f'Not a valid input, {tree[0]} Enter \"yes\" or \"no\": ')
    # tree = list(tree)
    while True:
        tree = playLeaf(tree)
        # print('This is the new tree: ')
        # printTree(tree)
        ans = yes('Would you like to play again? ')
        if not ans:
            return tree


def isLeaf(tree):
    if (tree[1] == None) and (tree[2] == None):
        return True
    else:
        return False


def yes(prompt):
    while True:
        content = input(prompt)
        if content in ['yes', 'y', 'yup', 'sure']:
            return True
        elif content in ['no', 'n', 'nope']:
            return False
        else:
            print("Not a valid input, please enter \"yes\" or \"no\": ")


def playLeaf(node):
    # question_obj = input('Drats! What was it?')
    # question_dist = input(f'What\'s a question that distinguisheds between {question_obj} and {tree[0]}?')
    # question_tf = input(f"and what\'s the answer for {question_obj}? Please enter \"yes\" or \"no\"")
    # if question_tf == yes:
    #     new_leaf = (question_dist, question_obj, tree)
    # else:
    #     new_leaf = (question_dist, tree, question_obj)
    #
    # return new_leaf

    if isLeaf(node):
        ans = yes(f'I guess it is {node[0]}, am I correct? Enter \"yes\" or \"no\": ')
        if ans:
            print("I got it!")
            return node
        else:
            ans = input('Drats! What was it? ')
            qst = input(f'What\'s a question that distinguisheds between {ans} and {node[0]}? ')
            question_tf = yes(f"and what\'s the answer for {ans}? Please enter \"yes\" or \"no\"")
            if question_tf:
                new_leaf = (qst, (ans, None, None), (node[0], None, None))
            else:
                new_leaf = (qst, (node[0], None, None), (ans, None, None))

            return new_leaf

    else:
        ans = yes(f'{node[0]} Enter \"yes\" or \"no\": ')
        if ans:
            return tuple((node[0], playLeaf(node[1]), node[2]))
        else:
            return tuple((node[0], node[1], playLeaf(node[2])))


def saveTree(tree, treeFile):
    if isLeaf(tree):
        print('Leaf', file=treeFile)
        print(tree[0], file=treeFile)
    else:
        print('Internal node', file=treeFile)
        print(tree[0], file=treeFile)
        saveTree(tree[1], treeFile)
        saveTree(tree[2], treeFile)


def loadTree(treeFile):
    while True:
        line = treeFile.readline().strip()
        if line == '':
            break
        elif line == "Leaf":
            tree = treeFile.readline().strip()
            return (tree, None, None)
        else:
            qst = treeFile.readline().strip()
            return (qst, loadTree(treeFile), loadTree(treeFile))








    
#
# The following two-line "magic sequence" must be the last thing in
# your file.  After you write the main() function, this line it will
# cause the program to automatically play 20 Questions when you run
# it.
#
if __name__ == '__main__':
    main()
