'''
 This modules was written to use a basic implementation of a trie in order to add values and find the most descriptive prefix possible in a simple way. 

'''
class TrieNode(object):
    """
    Basic Trie node implementation. Focused around inserting and checking prefixes only.
    """
    def __init__(self, char: str):
        self.char= char
        self.children = []
        self.word_finished = False

def add(root, word: str):
    """
    Add a word to the trie structure
    """
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char: 
                node = child
                found_in_child = True
                break

        if not found_in_child: 
            new_node = TrieNode(char)        
            node.children.append(new_node)

            # point to new node to continue nesting structure
            node = new_node

    node.word_finished = True

def longest_prefix(root, word: str) -> str:
    prefix = ''
    node = root

    # if the trie is empty, return the entire word as longest prefix
    if not node.children:
        return word

    for char in word:
        child_count = len(node.children)
        # if the character in a trie is a finished word, regardless of how many children it has
        # it should be the prefix because anything after it will be moot.
        if node.word_finished:
            return prefix

        # ignore the first character of a trie
        if child_count > 1 and node.char != '*':
            return prefix
        
        for child in node.children:
            if child.char == char:
                node = child
                prefix += char
                break
    return prefix
