# Transformer-Network-on-CN-EN-Translation
Apply state of art machine translation techniques to Chinese and English translation

### Dataset

1. Download [MultiUN dataset](wget http://opus.nlpl.eu/download.php?f=MultiUN/en-zh.txt.zip)
2. Unzip file and put 'MultiUN.en-zh.zh' and 'MultiUN.en-zh.en' in 'corpra' directory.

### Pre-Processing

2. Install Chinese tokenization library jieba by running command 'pip install jieba'.
3. Run token_zh.py to tokenize Chinese corpus in MultiUN Dataset (MultiUN.en-zh.zh).
4. Rename the tokenized result as 'MultiUN.en-zh.zh'.
5. Run split_data.py to split dataset into training set and test set. Hyperparameters are in hyperparams.py


TODO List:

1. Understand the padding logic of transformer net.

### Training

### Evaluating
