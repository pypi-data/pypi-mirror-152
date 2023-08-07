# pyEmbedsSSSA Package

Package for Introduction to Programming and Machine Learning in Python

## Installing pyEmbedsSSSA
`pip install pyembeds-sssa`

## USAGE
-  AUTOTESTING ASSIGNMENT
```python
from pyembeds.testing.auto_testing import run_and_test
# Simple Test
def asgn01_01Hello_world():
    print('Ciao, mondo!')
run_and_test([], ["Ciao, mondo!"], asgn01_01Hello_world)
```
- TESTING DOWNLOAD FILE FUNCTION
```python
from pyembeds.data.load_data import donwload_file
url = 'https://raw.githubusercontent.com/EMbeDS-education/SNS-IProML2022/main/jupyter/jupyterNotebooks/data/WBCD.csv'
donwload_file(url)
```
-  LOAD CAPYTHONE ASSIGNMENT DATA
```python
from pyembeds.data.load_data import load_capythone_data
data = load_capythone_data()
reviews = data['reviews']
positive_word = data['positive_word']
negative_word = data['negative_word']
```
- LOAD WORDCLOUD ASSIGNMENT DATA
```python
from pyembeds.data.load_data import load_wordcloud_ita_data
data = load_wordcloud_ita_data()
text = data['manzoni']
stop_words = data['stopwords_italian']
```
- VISUALIZATION FUNCTION
```python
from pyembeds.vis.utils import draw_euclidean_distance
draw_euclidean_distance((20, 10), (5, 0), (5, 20))
```

## Course responsible:
- [Andrea Vandin](https://www.santannapisa.it/en/andrea-vandin), andrea.vandin@santannapisa.it 
- [Daniele Licari](https://www.linkedin.com/in/daniele-licari/), daniele.licari@santannapisa.it 

## Description:
The course introduces students to programming and data analysis, using python as a reference
language.
 - **Module 1** 
Introduces students to the fundamental principles of structured programming with basic applications to data processing

 - **Module 2**
Introduces the students to the components of typical data analysis processes and machine learning pipelines.
