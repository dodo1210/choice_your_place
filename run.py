import seaborn as sns
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd 
import time
import nltk
import math
from sklearn.cluster import KMeans
import numpy as np
nltk.download("all")
from nltk import tokenize
from string import punctuation
from kneed import KneeLocator
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

data = pd.read_csv("data.csv")
foo_words = nltk.corpus.stopwords.words("english")

list_new_phrase = []
list_punc_phrase = []
list_strem_phrase = []
list_adjective_phrase = []
list_other_words = []

token_space = tokenize.WhitespaceTokenizer()
token_punctuation = tokenize.WordPunctTokenizer()
stemmer = nltk.RSLPStemmer()

list_punct = ['’','.\\','n','s','–','),']
for punc in punctuation:
  list_punct.append(punc)
c = 0

list_places = []
for c in data['City']:
  if str(c) in ' ':
    words_text = token_space.tokenize(c)
    for w in words_text:
      list_places.append(str(w).lower())
  else:
    list_places.append(str(c).lower())
for c in ['Sri','Racha','philadelph','local','region','province','state','capital','italian','french','world','town','city','tourism','tourist','and','visit','visitor','visitors','place','France','Spain','United', 'States','America', 'USA', 'China', 'Italy','Turkey', 'Mexico', 'Germany', 'United', 'Kingdom', 'Thailand','Japan','Hong', 'Kong','Austria', 'Greece', 'Malaysia', 'Russian','Portugal', 'Canada', 'Poland', 'Holand', 'Netherland']:
  list_places.append(c.lower())

other_words = ['one','atrations','the','many','e','é','que','com','os','you','we','i','he','she','it','yo’re','the','it’s','they']
adjetives = [x.lower() for x in ['perfect','largest','biggest','small','Defiant','Homeless','Adorable','Delightful','Homely','Quaint','Adventurous','Depressed','Horrible','Aggressive','Determined','Hungry','Real','Agreeable','Different','Hurt','Relieved','Alert','Difficult','Repulsive','Alive','Disgusted','Ill','Rich','Amused','Distinct','Important','Angry','Disturbed','Impossible','Scary','Annoyed','Dizzy','Inexpensive','Selfish','Annoying','Doubtful','Innocent','Shiny','Anxious','Drab','Inquisitive','Shy','Arrogant','Dull','Itchy','Silly','Ashamed','Sleepy','Attractive','Eager','Jealous','Smiling','Average','Easy','Jittery','Smoggy','Awful','Elated','Jolly','Sore','Elegant','Joyous','Sparkling','Bad','Embarrassed','Splendid','Beautiful','Enchanting','Kind','Spotless','Better','Encouraging','Stormy','Bewildered','Energetic','Lazy','Strange','Black','Enthusiastic','Light','Stupid','Bloody','Envious','Lively','Successful','Blue','Evil','Lonely','Super','Excited','Long','Blushing','Expensive','Lovely','Talented','Bored','Exuberant','Lucky','Tame','Brainy','Tender','Brave','Fair','Magnificent','Tense','Breakable','Faithful','Misty','Terrible','Bright','Famous','Modern','Tasty','Busy','Fancy','Motionless','Thankful','Fantastic','Muddy','Thoughtful','Calm','Fierce','Mushy','Thoughtless','Careful','Filthy','Mysterious','Tired','Cautious','Fine','Tough','Charming','Foolish','Nasty','Troubled','Cheerful','Fragile','Naughty','Clean','Frail','Nervous','Ugliest','Clear','Frantic','Nice','Ugly','Clever','Friendly','Nutty','Uninterested','Cloudy','Frightened','Unsightly','Clumsy','Funny','Obedient','Unusual','Colorful','Obnoxious','Upset','Combative','Gentle','Odd','Uptight','Comfortable','Gifted','Old-fashioned','Concerned','Glamorous','Open','Vast','Condemned','Gleaming','Outrageous','Victorious','Confused','Glorious','Outstanding','Vivacious','Cooperative','Good','Courageous','Gorgeous','Panicky','Wandering','Crazy','Graceful','Perfect','Weary','Creepy','Grieving','Plain','Wicked','Crowded','Grotesque','Pleasant','Cruel','Grumpy','Poised','Wild','Curious','Poor','Witty','Cute','Handsome','Powerful','Worrisome','Happy','Precious','Worried','Dangerous','Healthy','Prickly','Wrong','Dark','Helpful','Proud','Dead','Helpless','Putrid','Zany','Defeated','Hilarious','Puzzled','Zealous']]

for desc in data.Description:
  new_phrase = []
  words_text = token_space.tokenize(desc)
  for words in words_text:
    if words not in foo_words:
      new_phrase.append(words)     
  list_new_phrase.append(' '.join(new_phrase))
  
  new_phrase = []
  words_text = ''
  words_text = token_space.tokenize(desc)
  for words in words_text:
    if words not in other_words:
      new_phrase.append(words)     
  list_other_words.append(' '.join(new_phrase))

  new_phrase = []
  words_text = ''
  words_text = token_space.tokenize(desc)
  for words in words_text:
    if words not in adjetives:
      new_phrase.append(words)     
  list_adjective_phrase.append(' '.join(new_phrase))

  new_phrase = []
  words_text = ''
  words_text = token_punctuation.tokenize(list_new_phrase[-1].lower())
  for words in words_text:
    if(words not in list_punct) and (words not in list_places):
      new_phrase.append(words) 
  list_punc_phrase.append(' '.join(new_phrase))
  
  new_phrase = []
  words_text = ''
  words_text = token_space.tokenize(list_punc_phrase[-1])
  for words in words_text:
    if words not in list_punct:
      new_phrase.append(stemmer.stem(words)) 
  list_strem_phrase.append(' '.join(new_phrase))
  
data["elimination"] = list_strem_phrase

vector = CountVectorizer(lowercase=False,max_features=70)
bag_of_words = vector.fit_transform(data["elimination"])
cols = vector.get_feature_names()
data_sparse = pd.DataFrame.sparse.from_spmatrix(bag_of_words,columns=cols)

inertia = []
i=1
while(i<50):
  kmeans = KMeans(n_clusters=i, random_state=0).fit(data_sparse)
  inertia.append(kmeans.inertia_)
  i+=1

#graph = pd.DataFrame(inertia,columns=['grupos','inertia'])
mininum = math.sqrt(((inertia[0]-inertia[-1])*(inertia[0]-inertia[-1]))+((inertia[0]-inertia[-1])*(inertia[0]-inertia[-1])))
get = 0
index = 0
for ine in inertia:
  b = (inertia[0]-ine)*(inertia[0]-ine)
  c = (ine-inertia[-1])*(ine-inertia[-1])
  a = math.sqrt(b+c)
  if a<mininum:
    get = index
    mininum = a
  index+=1
kmeans = KMeans(n_clusters=get, random_state=0).fit(data_sparse)

model = AgglomerativeClustering(n_clusters=get)
gp = model.fit_predict(data_sparse)

tsne = TSNE()
visualisation = tsne.fit_transform(data_sparse) 

sns.set(rc={'figure.figsize':(13,13)})
sns.scatterplot(x=visualisation[:,0],y=visualisation[:,1],hue=kmeans.labels_,palette=sns.color_palette('Set1', get))
plt.show()

def count(data):
  all_words = ' '.join([text for text in data])
  token_phrase = token_space.tokenize(all_words)
  frequency = nltk.FreqDist(token_phrase)
  df_frequency = pd.DataFrame({"Palavra":list(frequency.keys()),"Frequencia":list(frequency.values())})
  de_frequency = df_frequency.nlargest(columns="Frequencia",n=10)
  return(de_frequency)

list_city = []
list_classification = []
for l in range(get):
  new_list = []
  city = []
  for i in range(len(gp)):
    if l==gp[i]:
      data["classification"] = l
      city.append(data['City'][i])
      new_list.append(data['elimination'][i])
  list_classification.append(new_list)
  list_city.append(city)
  
for l in range(get):
  print(len(list_city[l]))
