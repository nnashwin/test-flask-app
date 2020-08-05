import basictrie as trie 
import json

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
