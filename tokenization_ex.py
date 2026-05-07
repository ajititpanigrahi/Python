#ChatGPT --> Query, what is LLM --->["what","is","LLM"]
# Autotokenizer is the predefined class, used to implement the tokenization in LLM'S
#low lower lowest ["low","er","est"]
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
text = "Tokenization is Amazing!"
tokens = tokenizer.tokenize(text)
print(tokens)  # ['token', '##ization', 'is', 'amazing', '!']
token_ids = tokenizer.convert_tokens_to_ids(tokens)
print(token_ids)  # [19204, 3989, 2003, 6429, 999]

#[19204] ---->[0.000001,0.000767,0.909090,0.987656,.....8] #Embedding
#Embedding - converting tokenid to vector by using tokenizer
#LLM interal code is transformers (LLM architecture is transformers)
