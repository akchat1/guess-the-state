import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

df = pandas.read_csv('50_states.csv')
all_states = df.state.to_list()
for i in range(len(all_states)):
    all_states[i] = all_states[i].lower()
guessed_state = []
while len(guessed_state) != 50:
    answer_state = screen.textinput(title=f"Guess the state {len(guessed_state)}/50", prompt="What's another state's name?")
    if answer_state == 'exit':
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        position = df[df["state"].str.lower() == answer_state]
        print(position)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(position["x"]), int(position["y"]))
        t.write(answer_state)
        # t.write(position.state.item())
missed_states = list(set(all_states) ^ set(guessed_state))
missed_states = {"state to remember next time": missed_states}
pd = pandas.DataFrame(missed_states)
pd.to_csv('missed_states.csv')