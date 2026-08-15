import pgzrun

Title = "Quiz master"
WIDTH = 870
HEIGHT = 650

heading_box = Rect(0, 0, 880, 80)
question_box = Rect(0, 0, 650, 150)
timer_box = Rect(0, 0, 150, 150)
answer_box1 = Rect(0, 0, 300, 150)
answer_box2 = Rect(0, 0, 300, 150)
answer_box3 = Rect(0, 0, 300, 150)
answer_box4 = Rect(0, 0, 300, 150)
skip_box = Rect(0, 0, 150, 330)

score = 0
time_left = 0
question_file_name = "questions.txt"
mark_message = ""
game_over = False
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
questions = []
question_count = 0
question_index = 0

heading_box.move_ip(0, 0)
question_box.move_ip(20, 100)
timer_box.move_ip(700, 100)
answer_box1.move_ip(370, 450)
answer_box2.move_ip(20, 450)
answer_box3.move_ip(20, 450)
answer_box4.move_ip(370, 450)
skip_box.move_ip(700, 270)

def draw():
    global heading_message
    screen.clear()
    screen.fill(color = "black")
    screen.draw.filled_rect(heading_box, "black")
    screen.draw.filled_rect(question_box, "cherry red")
    screen.draw.filled_rect(timer_box, "dark blue")
    screen.draw.filled_rect(skip_box, "grey")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "dark orange")

        heading_message = "Welcome to Quiz Master!"
        heading_message = heading_message + f"Q: {question_index} of {question_count}"

        screen.draw.textbox(heading_message, heading_box, color = "white")
        screen.draw.textbox(str(time_left), timer_box, color = "white", shadow = (0.5, 0.5), scolor = "dim grey")
        screen.draw.textbox("Skip", skip_box, color ="black", angle = -90)
        screen.draw.textbox(question[0].strip(), question_box, color = "white", shadow = (0.5, 0.5), scolor = "dim grey")

        index = 1
        for answer in answer_boxes:
            screen.draw.textbox(question[index].strip(), answer_box, color = "black")
            index = index + 1

def update():
    move_heading()

def move_heading():
    heading_box.x = heading_box.x - 2
    if heading_box.right < 0:
        heading_box.left = WIDTH

def read_questions_file():
    global question_count, questions 
    q_file = open(question_file_name, "r")
    for question in q_file:
        questions.append(question)
        question_count = question_count + 1
    q_file.close()

def read_next_question():
    global question_index
    question_index = question_index + 1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index == int(question[5]):
                correct_answer()
            else:
                game_over()

        if skip_box.collidepoint(pos):
            skip_question()

def correct_answer():
    global score, question, time_left, questions 
    if questions:
        question = read_questions_file()
        time_left = 10
    else:
        game_over()

def game_over():
    global is_game_over
    message = f"Game over!\n You got {score} points."
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0
    is_game_over = True

def skip_question():
    global question, time_left
    if question and not game_over:
        question = read_next_question()
        time_left = 10
    else:
        game_over()

def update_time_left():
    global time_left
    if time_left:
        time_left = time_left - 1
    else:
        game_over()

read_questions_file()
question = read_next_question()
clock.schedule_interval(update_time_left, 1)

pgzrun.go()