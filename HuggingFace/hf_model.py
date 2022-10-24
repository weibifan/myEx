# -*- coding: utf-8 -*-
# weibifan 2022-10-3
# 基于Transformer的PLM模型的使用 --- PaddleHub模拟的对象
# 大模型理论
# 基本方法：①访问 https://github.com/huggingface/transformers
# ②  进入模型网站，看说明和代码：https://huggingface.co/gpt2

# 这里的pipeline和TorchData里面的pipeline是什么关系？？？？
"""
https://huggingface.co/models  模型检索
1） 所有模型放到https://huggingface.co/网站上。支持PyTorch，TF等，几乎没有Paddle平台。
2） 通过 AutoConfig类设置模型的信息
3） 通过字符串标识不同模型，比如luhua\\chinese_pretrain_mrc_macbert_large
4）通过from_pretrained()函数从网站下载模型到本地，并加载到cpu的mem
5）模型大小一般在2G左右
9）中文模型很少

2种基本使用方法：
1）基于Python的 pipeline API
2）微服务版The Inference API：huggingface上模型的在线版
在页面的右侧：Hosted inference API

这里的模型分为3类：
1）大厂发布的基础模型，比如Google的T5，mT5，OpenAI的CLIP，GPT2等。
2）基于大厂基础模型的微调，比如基于mT5的中文问题生成。
3）基于论文实现的模型，及这些模型的微调版，尤其是大厂的微调版。

https://huggingface.co/docs/transformers/quicktour

Auto Classes：一种使用PLM的规范
https://huggingface.co/docs/transformers/model_doc/auto

AutoTokenizer：基于词表的分词器，不同语言该模型有较大区别。
1） 词表一般来源于PLMs，所以使用from_pretrained()函数获得。

AutoFeatureExtractor：Word Embedding？？？

典型的pipeline：pipeline函数的第1个参数，huggingface页面左侧的任务标签
feature-extraction (get the vector representation of a text) ：词嵌入
fill-mask ：完形填空
ner (named entity recognition)
question-answering
sentiment-analysis：文本分类
summarization ：T5
text-generation ：GPT2
translation ：
zero-shot-classification

# 英文语法纠错：Huggingface  tuner007/pegasus_paraphrase


每个任务有很多模型：比如文本生成任务包括GPT2，distilgpt2，xlnet-base-cased等。
https://huggingface.co/models?pipeline_tag=text-generation

Transformer原理：
https://huggingface.co/course/chapter1/4?fw=pt

Checkpoints：指某个模型的参数

"""
# 典型案例：文本分类
from transformers import pipeline

# 查看源代码，或者访问上面网站，得到pipeline所有可能参数，
# 第1个参数：任务类型，决定那些函数。当没定义第2个参数时，选择一个默认模型。
# 第2个参数：具体的模型。也就是PLMs
classifier = pipeline("sentiment-analysis")

result = classifier("We are very happy to show you the 🤗 Transformers library.")
print(result)
# [{'label': 'POSITIVE', 'score': 0.9998}]

''' 
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
result = classifier("Nous sommes très heureux de vous présenter la bibliothèque 🤗 Transformers.")
# [{'label': '5 stars', 'score': 0.7273}]

'''