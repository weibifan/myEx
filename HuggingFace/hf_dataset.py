# -*- coding: utf-8 -*-
# weibifan 2022-10-5
# 介绍Huggingface的数据集  https://huggingface.co/docs/datasets/load_hub
'''
数据集位置：https://huggingface.co/datasets
'''
from datasets import load_dataset

#第1种方法：不加载数据，只是浏览数据元数据。前提是下载数据到本地。
'''
from datasets import load_dataset_builder

ds_builder = load_dataset_builder("squad")  #下载数据到本地

print(ds_builder.info.description)

'''

# 第2种方法：将数据加载到内存，浏览数据。前提是下载数据到本地。
# C:/Users/Wei/.cache/huggingface/datasets/squad
dataset = load_dataset("squad")  #下载数据到本地。

print(dataset)  # 显示数据集元数据

train = load_dataset("squad", split="train")
print(train) #显示数据元数据

print(train[0]) #访问第1个数据

print(train[0]['context']) #访问第1个数据的context字段


#  命令行执行
import datasets
data = datasets.load_dataset('GEM/FairytaleQA')  # ACL22
print(data)  # 显示数据集元数据
print(data['train'][0])  # 显示数据集元数据
'''
C:/Users/Wei/.cache/huggingface/datasets/GEM___fairytale_qa/default/1.0.0/915cb13387fb0028e0fd29b7f156905e3afb99ba1d58c88d6c54a4e550c8678b.
'''