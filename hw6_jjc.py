#
# Name: Jiachen Jiang
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

    # print('Small Tree:')
    # printTree(smallTree)
    # print('Medium Tree:')
    # printTree(mediumTree)
    # print('Sub tree of Medium Tree:')
    # printTree(mediumTree[1])

    # print(simplePlay(mediumTree))
    # newTree = play(smallTree)
    # printTree(newTree)
    #
    # treeFile = open("tree1.txt", "w")
    # saveTree(smallTree,treeFile)
    # treeFile.close()
    # #
    # treeFile = open("tree2.txt", "w")
    # saveTree(newTree, treeFile)
    # treeFile.close()

    # treeFile = open("tree1.txt", "r")
    # tree1 = loadTree(treeFile)
    # treeFile.close()
    # print(tree1)
    print("Welcome to 20 Questions!")
    load = yes("Would you like to load a tree from a file?")
    if load:
        treeFile = input("What's the name of the file?")
        treeFile = open(treeFile, "r")
        tree = loadTree(treeFile)
        treeFile.close()
        printTree(tree)
    else:
        tree = smallTree

    new_tree = play(tree)

    while yes("Would you like to play again?"):
        new_tree = play(new_tree)

    save = yes("Would you like to save this tree for later?")
    if save:
        file_name = input("Please enter a file name:")
        treeFile = open(file_name, "w")
        saveTree(new_tree, treeFile)
        treeFile.close()
        print("Thank you! The file has been saved.")
    print("Bye!")




def isLeaf(tree):
    return tree[1] is None and tree[2] is None

def yes(prompt):
    while True:
        ans = input(prompt)
        if(ans in ['yes' ,'yup','y','sure','Y','YES']):
            return True
        elif(ans in ['no' ,'n', 'nope','N','NO']):
            return False
        else:
            print('Input yes or no.')

def playLeafSimple(tree):
    return yes(tree[0])

def playLeaf(tree):
    result = yes(tree[0])
    if result:
        print("I got it!")
        return tree
    else:
        new_answer = input("Drats! What was it?")
        new_question = input("What's a question that distinguishes between a " + new_answer +"and an " + tree[0]+"?")
        new_label = yes("And what's the answer for a "+new_answer+" ?")
        if new_label:
            new_tree = (new_question, (new_answer,None,None), (tree[0],None,None))
        else:
            new_tree = (new_question, (tree[0],None,None), (new_answer,None,None))

        return new_tree

def simplePlay(tree):
    """
    :param tree: a tree (or a sub-part of a tree), 3-tuple (also called a "triple")
    :return: It returns True/False if the computer guessed the answer or not.
    It plays the game once by using the tree to guide its questions.
    """
    if isLeaf(tree):
        return playLeaf(tree)
    else:
        ans = yes(tree[0])
        if ans is True:
            return simplePlay(tree[1])
        else:
            return simplePlay(tree[2])

    
def play(tree):
    """
    :param tree:  a tree (or a sub-part of a tree), 3-tuple (also called a "triple")
    :return: returns a new tree that is the result of playing the game on the original tree and learning from the answers.
    If the computer doesn't guess the object correctly, it will ask the user for the name of the object and a question
    that will distinguish it (see below for an example).
    """
    if isLeaf(tree):
        return playLeaf(tree)
    else:
        ans = yes(tree[0])
        if ans is True:
            return (tree[0],play(tree[1]),tree[2])
        else:
            return (tree[0],tree[1],play(tree[2]))


def saveTree(tree, treeFile):
    if isLeaf(tree):
        print("Leaf\n"+ tree[0], file = treeFile)
    else:
        print("Internal node\n" + tree[0] , file = treeFile)
        saveTree(tree[1], treeFile)
        saveTree(tree[2], treeFile)


def loadTree(treeFile):
    while True:
        line = treeFile.readline().strip()
        if line == '':
            break
        elif line == "Leaf":
            leaf = treeFile.readline().strip()
            return (leaf, None, None)
        else:
            question = treeFile.readline().strip()
            return (question,loadTree(treeFile),loadTree(treeFile))

#
# The following two-line "magic sequence" must be the last thing in
# your file.  After you write the main() function, this line it will
# cause the program to automatically play 20 Questions when you run
# it.
#
if __name__ == '__main__':
    main()
