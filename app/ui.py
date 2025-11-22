import gradio as gr
from src.inference import generate_plan

levels = ['beginner','intermediate','advanced']
goals = ['weight_loss','muscle_gain','endurance','flexibility','general_fitness']

def run_ui():
    def fn(age, level, goal, time):
        return generate_plan(age, level, goal, time)
    demo = gr.Interface(fn=fn, inputs=[gr.Slider(13,80,value=25,label='Age'), gr.Dropdown(levels, value='beginner', label='Level'), gr.Dropdown(goals, value='general_fitness', label='Goal'), gr.Slider(10,120,value=30,label='Time (mins)')], outputs='text', title='Personal Fitness Assistant NLP')
    demo.launch()

if __name__ == '__main__':
    run_ui()
