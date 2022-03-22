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

並不是所有的資料都能這麼方便地以表格式資料（Tabular data），EXCEL 試算表或者 JSON 載入工作環境，有時候我們的資料散落在網路不同的角落裡，然而並不是每一個網站都會建置 API（Application Programming Interface）讓你很省力地把資料帶回家，這時候我們就會需要網頁解析（Web scraping）。

R 語言使用者對於 rvest 套件在網頁解析的便利性愛不釋手，而 Python 對應的代表套件就是 BeautifulSoup，事實上，rvest 開發的靈感就是啟發自 BeautifulSoup。

準備工作
除了 BeautifulSoup 套件以外，我們還需要搭配使用 lxml 套件與 requests 套件。由於我們的開發環境是安裝 Anaconda，所以這些套件都不需要再另外下載與安裝，只要進行一貫的 import 就好。如果對於開發環境的部分有興趣，我推薦你參考 [第 01 天] 建立開發環境與計算機應用。

lxml 套件
lxml 套件是用來作為 BeautifulSoup 的解析器（Parser），BeautifulSoup 可以支援的解析器其實不只一種，還有 html.parser（Python 內建）與 html5lib，根據官方文件的推薦，我們使用解析速度最快的 lxml。

```
from extract import read_imdb
from shuffle_imdb import prepare_imdb_data
from bs4 import BeautifulSoup


data, labels = read_imdb()
train_X, test_X, train_y, test_y = prepare_imdb_data(data, labels)
```
```
$ print(train_X[100])
$ print(train_y[100])
```
Cut tries to be like most post-Scream slashers tried to be, a spoof of the horror genre that tried to be clever by referencing other famous horror movies. Now, I am not bagging 'Scream,' as I think 'Scream' is a very good horror movie that does a great job of blending horror and comedy. Cut fails on most levels. It has its moments but overall it just does not work out, not even as a "so bad it's good" movie, just a below average one.<br /><br />The first five minutes or so are OK and set the story fairly well, apart from the fact that Kylie Minogue can't really act, and ironically she gets her tongue out, go figure. Go forward some time and a group of film students want to finish her film off, which is apparently cursed. And, as you have probably predicted, one by one the cast and crew are slowly picked off by a masked madman.<br /><br />Unoriginal plot, poor acting and a predictable ending are a few of the elements that follow. There is plenty of referencing in the film, everything from 'Scream' to 'The Texas Chain Saw Massacre.' This isn't smart either, it feels as though the director wanted to feel smart and cool by mentioning other famous horror flicks ala Scream. For a slasher there is minimal gore and no nudity, which is a huge negative when it comes to a slasher that has not got a whole lot going for it. Really, I should be supporting this movie because I'm Australian and we're not as good when it comes to horror (we do have our gems, though) but Cut is definitely not one of them.<br /><br />However, it did keep me watching for the 90 minutes or so, so that is something good at least. I would not recommend this to anyone apart from hardcore slasher fans, who may be able to appreciate what this film is trying to aim for, but if you are looking for a good movie, stay away.<br /><br />2/5
0

```
removed_before = train_X[100]
removed_after = BeautifulSoup(train_X[100], 'html.parser').get_text()
```

```
$ print(removed_after)
```
Cut tries to be like most post-Scream slashers tried to be, a spoof of the horror genre that tried to be clever by referencing other famous horror movies. Now, I am not bagging 'Scream,' as I think 'Scream' is a very good horror movie that does a great job of blending horror and comedy. Cut fails on most levels. It has its moments but overall it just does not work out, not even as a "so bad it's good" movie, just a below average one.The first five minutes or so are OK and set the story fairly well, apart from the fact that Kylie Minogue can't really act, and ironically she gets her tongue out, go figure. Go forward some time and a group of film students want to finish her film off, which is apparently cursed. And, as you have probably predicted, one by one the cast and crew are slowly picked off by a masked madman.Unoriginal plot, poor acting and a predictable ending are a few of the elements that follow. There is plenty of referencing in the film, everything from 'Scream' to 'The Texas Chain Saw Massacre.' This isn't smart either, it feels as though the director wanted to feel smart and cool by mentioning other famous horror flicks ala Scream. For a slasher there is minimal gore and no nudity, which is a huge negative when it comes to a slasher that has not got a whole lot going for it. Really, I should be supporting this movie because I'm Australian and we're not as good when it comes to horror (we do have our gems, though) but Cut is definitely not one of them.However, it did keep me watching for the 90 minutes or so, so that is something good at least. I would not recommend this to anyone apart from hardcore slasher fans, who may be able to appreciate what this film is trying to aim for, but if you are looking for a good movie, stay away.2/5

```
In [14]: len(removed_before)
Out[14]: 1823

In [15]: len(removed_after)
Out[15]: 1775

In [17]: "<br />" in removed_before
Out[17]: True

In [18]: "<br />" in removed_after
Out[18]: False
```
