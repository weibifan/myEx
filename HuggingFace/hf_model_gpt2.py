# -*- coding: utf-8 -*-
# weibifan 2022-10-5
# 英文文本生成任务，
# 1) text generation，默认模型  gpt2
# 2) text2text-generation 默认模型  t5-base
# https://huggingface.co/gpt2

'''
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
'''

from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
result = generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5)
print(result)


