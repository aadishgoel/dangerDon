from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os 
base_path = os.path.dirname(__file__)
stopwords = set(stopwords.words('english'))

mapping = {}
def loader(file,value):
        with open(file) as fp:
                for line in fp.readlines():
                        mapping[line.strip()]=value

loader(os.path.join(base_path,'positive.txt'),1)
loader(os.path.join(base_path,'negative.txt'),-1)

def rating(comment):
        inp = set(word_tokenize(comment))
        inp -= stopwords
        ans = sum([mapping.get(i.lower(),0) for i in inp])
        return ans

if __name__=='__main__':
        print(rating(input()))        
