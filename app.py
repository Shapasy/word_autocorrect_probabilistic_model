from preprocessing import preprocessing_data
from model import get_corrections
from operator import itemgetter

vocab,probs = preprocessing_data('./dataset/',print_info=True)
print("------------------------------------------")

test_words = ["welczme","wklx","ocay","whag","lbve","how"]

for word in test_words:
    suggestions,n_best = get_corrections(word,probs,vocab)
    n_best.sort(key = itemgetter(1))
    print("Word :",word)
    print("Suggestions :")
    for suggest in n_best[::-1]:
        print(suggest)
    print("------------------------------------------")
    

