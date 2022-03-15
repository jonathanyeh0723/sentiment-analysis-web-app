# Install scikit-learn (This can be referred to https://scikit-learn.org/stable/install.html)
!pip install -U scikit-learn

"""
Defaulting to user installation because normal site-packages is not writeable
Collecting scikit-learn
  Downloading scikit_learn-1.0.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (26.7 MB)
     |████████████████████████████████| 26.7 MB 16.0 MB/s            
Collecting scipy>=1.1.0
  Downloading scipy-1.8.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (41.6 MB)
     |████████████████████████████████| 41.6 MB 123 kB/s             
Collecting joblib>=0.11
  Downloading joblib-1.1.0-py2.py3-none-any.whl (306 kB)
     |████████████████████████████████| 306 kB 15.3 MB/s            
Requirement already satisfied: numpy>=1.14.6 in ./.local/lib/python3.8/site-packages (from scikit-learn) (1.21.2)
Collecting threadpoolctl>=2.0.0
  Downloading threadpoolctl-3.1.0-py3-none-any.whl (14 kB)
Installing collected packages: threadpoolctl, scipy, joblib, scikit-learn
Successfully installed joblib-1.1.0 scikit-learn-1.0.2 scipy-1.8.0 threadpoolctl-3.1.0
"""

# Check download
!pip freeze | grep scikit

"""
scikit-learn==1.0.2
"""

# Start check
from sklearn import shuffle
import numpy as np

x = np.array([1, 2], [3, 4], [5, 6])
print(x)

# Output
"""
array([[1, 2],
       [3, 4],
       [5, 6]])
"""

shuffle(x)

# Output
"""
# Output
"""
array([[3, 4],
       [1, 2],
       [5, 6]])
"""
