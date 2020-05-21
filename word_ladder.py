

def word_diff(word1,word2):
    counter = 0
    for i in range(len(word1)):
        if word1[i]!=word2[i]:
            counter = counter+1
    return counter
start = "hit"
end = "cog"
words_dict = ["hot", "dot", "dog", "lot", "log"]
words_dict.append(end)
words_dict2 = words_dict.copy()
def get_children(parent_word,words_dict):
    children=[]
    for word in words_dict:
        if word_diff(parent_word,word) ==1:
            children.append(word)
    return children

stack = []
stack.append((start,0))

found = False
while len(stack)>0:
    word,depth = stack.pop()
    if word == end:
        print(f'reached with depth  = {depth}')
        break
    children = get_children(word,words_dict2)
    if len(children)>0:
        depth = depth+1
    for word_ in children:
        stack.append((word_,depth))
        words_dict2.remove(word_) # avoid cycles
print(f'found = {found}')