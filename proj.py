#https://blog.dataiku.com/2016/10/08/machine-learning-markov-chains-generate-clinton-trump-quotes
#TODO: get a lot more text for each author, 
#implement starting a phrase with a <sentence begin> and ending it with a <sentence end>
#implement Backoff, 
#implement word weights (right now the ngram densities are too low for weights to do much)
import nltk
import random
grams1 = {}
grams2 = {}
N = 2
def initialize_grams(grams, textfile): #initialize the dicts that store the markov probabilities for N-word chains
    f = open(textfile)
    s = f.read().replace('(','').replace(')','')
    t = nltk.word_tokenize(s)
    for i in range(len(t)-(N+2)):
        trigram = tuple(t[i:i+N])
        if trigram in grams.keys():
            grams[trigram].add(t[i+N])
        else:
            grams[trigram] = set([t[i+N]])

            
def ngram_generate(grams): #generate text from a dict passed in
    nwords = 0
    start = random.choice(list(grams.keys()))
    res = list(start)
    while(nwords < 50):
        pre = tuple(res[(-1*N):])
        res.append(random.choice(list(grams[pre])))
        nwords +=1
    return " ".join(res).replace(' .', '.').replace(' ,', ',').replace(' ;',';').replace(' ?', '?').replace(' \'', '\'').replace(' !', '!')

def solve_density(grams): #On average, how many words are in the dict for each ngram?
    total = 0.0
    for word in grams.keys():
        total += len(grams[word])
    return total/len(grams)

def convo(text1, text2, author1, author2):
    initialize_grams(grams1, text1)
    initialize_grams(grams2, text2)
    print('first ngram density: '+ str(solve_density(grams1))+ '\n')
    print('second ngram density: '+ str(solve_density(grams2))+ '\n')
    for i in range(5):
        print(author1 + ':')
        speech1 = ngram_generate(grams1)
        print(speech1)
        print('\n')
        speech2 = ngram_generate(grams2)
        print(author2 + ':')
        print(speech2)
        print('\n')
        i+=1

convo('augustine.txt', 'zhuangzi.txt', 'Augustine', 'Zhuangzi')
