letters = 'abcdefghijklmnopqrstuvwxyz'

def delete_letter(word):
    split_l = [(word[:i],word[i:]) for i in range(len(word)+1)]
    delete_l = [a+b[1:] for a,b in split_l if b]
    
    return delete_l

def switch_letter(word):    
    split_l = [(word[:i],word[i:]) for i in range(len(word))]
    switch_l = [a + b[1] + b[0] + b[2:] for a,b in split_l if len(b) >= 2]
    
    return switch_l

def replace_letter(word, verbose=False):
    split_l = [(word[:i],word[i:]) for i in range(len(word))]
    replace_l = [a + l + (b[1:] if len(b) > 1 else '') for a,b in split_l if b for l in letters]
    
    replace_set = set(replace_l)
    replace_set.remove(word)
    replace_l = sorted(list(replace_set))    
    
    return replace_l

def insert_letter(word, verbose=False):
    split_l = [(word[:i],word[i:]) for i in range(len(word)+1)]
    insert_l = [a+l+b for a,b in split_l for l in letters]
    return insert_l

def edit_one_letter(word, allow_switches = True):
    edit_one_set = set()
    
    edit_one_set.update(delete_letter(word))
    
    if allow_switches:
        edit_one_set.update(switch_letter(word))
    edit_one_set.update(replace_letter(word))
    edit_one_set.update(insert_letter(word))
    
    return edit_one_set

def edit_two_letters(word, allow_switches = True):
    edit_two_set = set()
    
    edit_one = edit_one_letter(word,allow_switches=allow_switches)
    for w in edit_one:
        if w:
            edit_two = edit_one_letter(w,allow_switches=allow_switches)
            edit_two_set.update(edit_two)

    return edit_two_set

def get_corrections(word, probs, vocab):
    try:    
        suggestions = list((word in vocab) or (edit_one_letter(word)).intersection(vocab)
                       or edit_two_letters(word).intersection(vocab))
        n_best = [[w,probs[w]] for w in suggestions]
    except:
        suggestions = [word]
        n_best = [[word,100.]]

    return suggestions,n_best

