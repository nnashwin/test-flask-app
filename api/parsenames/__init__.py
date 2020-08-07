import basictrie as trie 
import json

'''
 Module that takes a list of strings, reads them into a simple trie, and creates a json object with keys and values based on the
 longest common prefix found inside of the trie
'''
def toJson(strList):
    root = trie.TrieNode('*')

    dict = {}
    for str in strList:
        trie.add(root, str)

    for str in strList:
        lPrefix = trie.longest_prefix(root, str)
        if lPrefix in dict:
            dict[lPrefix].append(str)
        else:
            dict[lPrefix] = [str]

    return json.dumps({'data': dict})
