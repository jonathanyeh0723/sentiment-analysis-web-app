## Note for extract.py
The idea is to have the following dictionary...

```
{'train': {'pos': [], 'neg': []}, 'test': {'pos': [], 'neg': []}}
```

```
$ ipython3

In [1]: from extract import read_imdb

In [2]: data, labels = read_imdb()

In [3]: data['train']['pos'][13]
Out[3]: 'I\'ve always knew Anne DeSalvo was a great character actor, now I know she is a great writer/director also. I have been a fan since I first saw her in the movies "Perfect", "My Favorite Year", "DC Cab" and "Stardust Memories".<br /><br />It\'s so rare to see Lee Grant these days in anything. She has been missing from the screen for far too long. It\'s also wonderful to see Cloris Leachman in something other than a sit-com. This is her best work since "the Last Picture Show". If you grew up in an Italian American family you will love this movie. I wasn\'t expecting a lot when I started watching this movie, so I was pleasantly surprised when I fell in love with this movie. If you get the chance, watch it.'

In [4]: labels['train']['pos'][13]
Out[4]: 1
```

**Expected output:**
```
IMDB reviews: train = 12500 pos / 12500 neg, test = 12500 pos / 12500 neg

IMDb reviews (combined): train = 25000, test = 25000

```

## Note for review_to_words

```
from extract import read_imdb
from shuffle_imdb import prepare_imdb_data
from bs4 import BeautifulSoup


data, labels = read_imdb()
train_X, test_X, train_y, test_y = prepare_imdb_data(data, labels)
```
```
$ print(train_X[100])
```
Cut tries to be like most post-Scream slashers tried to be, a spoof of the horror genre that tried to be clever by referencing other famous horror movies. Now, I am not bagging 'Scream,' as I think 'Scream' is a very good horror movie that does a great job of blending horror and comedy. Cut fails on most levels. It has its moments but overall it just does not work out, not even as a "so bad it's good" movie, just a below average one.<br /><br />The first five minutes or so are OK and set the story fairly well, apart from the fact that Kylie Minogue can't really act, and ironically she gets her tongue out, go figure. Go forward some time and a group of film students want to finish her film off, which is apparently cursed. And, as you have probably predicted, one by one the cast and crew are slowly picked off by a masked madman.<br /><br />Unoriginal plot, poor acting and a predictable ending are a few of the elements that follow. There is plenty of referencing in the film, everything from 'Scream' to 'The Texas Chain Saw Massacre.' This isn't smart either, it feels as though the director wanted to feel smart and cool by mentioning other famous horror flicks ala Scream. For a slasher there is minimal gore and no nudity, which is a huge negative when it comes to a slasher that has not got a whole lot going for it. Really, I should be supporting this movie because I'm Australian and we're not as good when it comes to horror (we do have our gems, though) but Cut is definitely not one of them.<br /><br />However, it did keep me watching for the 90 minutes or so, so that is something good at least. I would not recommend this to anyone apart from hardcore slasher fans, who may be able to appreciate what this film is trying to aim for, but if you are looking for a good movie, stay away.<br /><br />2/5
