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
