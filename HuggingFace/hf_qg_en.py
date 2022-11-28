# -*- coding: utf-8 -*-
# weibifan 2022-11-26
# 英文问题生成


from transformers import pipeline
# initialize model
pipe = pipeline("text2text-generation", 'lmqg/bart-base-squad')
# question generation
question = pipe('<hl> Beyonce <hl> further expanded her acting career, starring as blues singer Etta James in the 2008 musical biopic, Cadillac Records.')

print(question)
