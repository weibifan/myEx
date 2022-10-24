# -*- coding: utf-8 -*-
# weibifan 2022-10-7
# 系统展示界面，问答系统
# 可以直接和Hugging Face融合，详见官方文档 https://www.gradio.app/
# https://www.gradio.app/docs/
import gradio as gr

# 下面是非融合方式
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
model_name = "deepset/roberta-base-squad2"

# 加载时间很长
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

def question_answer(context, question):
    QA_input = {
        'question': question,
        'context': context
    }
    res = nlp(QA_input)
    print(res)
    return res['answer'], res['score']


# 简单版
'''
gr.Interface(fn=question_answer, inputs=["text", "text"], outputs=["textbox", "text"]).launch()

'''

#复杂版
qa_in1 = gr.Textbox(lines=10, value="Tom is a good man.")
qa_in2 = gr.Textbox(lines=2, value='What\'s about Tom?')
qa_out1 =  gr.Textbox(lines=10, label="Answer")
qa_out2 =  gr.Textbox(lines=2, label="Score")

demo = gr.Interface(
    fn=question_answer,
    inputs=[qa_in1, qa_in2],
    outputs=[qa_out1,qa_out2],
)
demo.launch()