import pgzrun

Title = "Math Speed Answering Quiz"
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
time_left = 10
question_file_name = "math questions.txt"
game_is_over = False

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

questions = []
question_count = 0
question_index = 0
question = []

heading_box.move_ip(0, 0)
question_box.move_ip(20, 100)
timer_box.move_ip(700, 100)
answer_box1.move_ip(20, 270)
answer_box2.move_ip(370, 270)
answer_box3.move_ip(20, 450)
answer_box4.move_ip(370, 450)
skip_box.move_ip(700, 270)

def draw():
    screen.clear()
    screen.fill("black")

    screen.draw.filled_rect(heading_box, "black")
    screen.draw.filled_rect(question_box, "red")
    screen.draw.filled_rect(timer_box, "dark blue")
    screen.draw.filled_rect(skip_box, "grey")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "orange")

    heading_message = "Math Speed Quiz"
    heading_message = heading_message + "    Q: " + str(question_index) + " of " + str(question_count)

    screen.draw.textbox(heading_message, heading_box, color="white")

    if game_is_over:
        screen.draw.text(
            "Game over!", center=(WIDTH / 2, 180), fontsize=60, color="white")

        screen.draw.text(
            "You got " + str(score) + " points.", center=(WIDTH / 2, 260), fontsize=40, color="white")

    else:
        screen.draw.textbox(str(time_left), timer_box, color="white")

        screen.draw.textbox("Skip", skip_box, color="black", angle=-90)

        screen.draw.textbox(question[0].strip(), question_box, color="white")

        index = 1

        for answer_box in answer_boxes:
            screen.draw.textbox(question[index].strip(), answer_box,color="black")
            index = index + 1

        screen.draw.text(
            "Score: " + str(score), topleft=(20, 20), fontsize=25, color="white")

def update():
    pass

def read_questions_file():
    global question_count, questions

    q_file = open(question_file_name, "r")

    for question_line in q_file:
        questions.append(question_line)
        question_count = question_count + 1

    q_file.close()

def read_next_question():
    global question_index

    question_index = question_index + 1

    return questions.pop(0).split(",")

def on_mouse_down(pos):
    index = 1

    if game_is_over:
        return

    for box in answer_boxes:
        if box.collidepoint(pos):

            if index == int(question[5]):
                correct_answer()
            else:
                end_game()

        index = index + 1

    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score, question, time_left

    score = score + 1

    if questions:
        question = read_next_question()
        time_left = 10
    else:
        end_game()

def end_game():
    global game_is_over, time_left

    time_left = 0
    game_is_over = True

def skip_question():
    global question, time_left

    if questions:
        question = read_next_question()
        time_left = 10
    else:
        end_game()

def update_time_left():
    global time_left

    if not game_is_over:
        if time_left > 0:
            time_left = time_left - 1
        else:
            end_game()

read_questions_file()
question = read_next_question()

clock.schedule_interval(update_time_left, 1)

pgzrun.go()