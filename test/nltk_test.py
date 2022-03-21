"""
In [1]: import nltk
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-1-1d2184025e54> in <module>
----> 1 import nltk

ModuleNotFoundError: No module named 'nltk'
"""

"""
$ pip3 install nltk
Defaulting to user installation because normal site-packages is not writeable
Collecting nltk
  Downloading nltk-3.7-py3-none-any.whl (1.5 MB)
     |████████████████████████████████| 1.5 MB 1.8 MB/s            
Requirement already satisfied: joblib in ./.local/lib/python3.8/site-packages (from nltk) (1.1.0)
Collecting tqdm
  Downloading tqdm-4.63.0-py2.py3-none-any.whl (76 kB)
     |████████████████████████████████| 76 kB 9.2 MB/s             
Collecting regex>=2021.8.3
  Downloading regex-2022.3.15-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (764 kB)
     |████████████████████████████████| 764 kB 11.7 MB/s            
Requirement already satisfied: click in ./.local/lib/python3.8/site-packages (from nltk) (8.0.1)
Installing collected packages: tqdm, regex, nltk
Successfully installed nltk-3.7 regex-2022.3.15 tqdm-4.63.0

$ pip freeze | grep nltk
nltk==3.7
"""

import nltk


nltk.download("stopwords", quiet=True)
# True

nltk_stopwords = nltk.corpus.stopwords.words('english')
print(nltk_stopwords[:10])
len(nltk_stopwords)
"""
['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're"]
179
"""
