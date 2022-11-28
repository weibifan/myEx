# -*- coding: utf-8 -*-
# weibifan 2022-10-5
# 中文问题生成


from transformers import  pipeline

model_name = "algolet/mt5-base-chinese-qg"

# a) Get predictions
pipe = pipeline('text2text-generation', model=model_name, tokenizer=model_name)
text = ["在一个寒冷的冬天，赶集完回家的农夫在路边发现了一条冻僵了的蛇。他很可怜蛇，就把它放在怀里。当他身上的热气把蛇温暖以后，蛇很快苏醒了，露出了残忍的本性，给了农夫致命的伤害——咬了农夫一口。农夫临死之前说：“我竟然救了一条可怜的毒蛇，就应该受到这种报应啊！”"]

question1= pipe(text)   #这行代码执行需要一段时间，且没有提示
print(question1)

text = ["Beyonce further expanded her acting career, starring as blues singer Etta James in the 2008 musical biopic, Cadillac Records."]

question1= pipe(text)   #这行代码执行需要一段时间，且没有提示
print(question1)