import os
import re
from collections import Counter

def preprocessing_data(path,print_info = False):    
    data = get_data(path,print_info)
    
    vocab = set(data)
    
    if(print_info):
            print("There are",len(vocab),"unique words in the vocabulary.") 
            
    probs = get_probs(data,vocab)
    
    return vocab,probs
        
def get_data(path,print_info):
    list_dir = os.listdir(path)
    
    if(print_info):
        print("Preprocessing 🎈🎈🎈")
        print("Found",len(list_dir),"files :",list_dir)
        
    data = []    
    for curr_dir in list_dir:
        if(not curr_dir.endswith(".txt")):
            print(curr_dir,"is not text file !")
            continue
        curr_data = None
        with open(path+curr_dir,encoding='cp850') as f: 
            curr_data = f.read()
        curr_data = curr_data.lower()
        curr_data = re.findall("\w+",curr_data)
        data.extend(curr_data)
        if(print_info):
            print("Found",len(curr_data),"words in",curr_dir)
    
    return data
    
def get_probs(data,vocab):
    freq = Counter(data)
    m = sum(freq.values())
    
    probs = {}
    for word in vocab:
        probs[word] = freq[word]/m    
        
    return probs
    
    
    
