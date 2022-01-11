number = randint(0, 100)
next_number = randint(0, 100)
score = 0
basic.show_number(number)

def on_button_pressed_a():
    global score, number, next_number
    if next_number <= number:
        basic.show_string("Bravo! scor:")
        score += 1
        basic.show_number(score)
        basic.show_string("Noul numar:")
        basic.show_number(next_number)
    else:
        basic.show_string("Gresit! Noul numar e:")
        basic.show_number(next_number)
        score = 0
        basic.show_string("Scor:")
        basic.show_number(score)
    number = next_number;
    next_number = randint(0, 100)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global score, number, next_number
    if next_number >= number:
        basic.show_string("Bravo! Scor:")
        score += 1
        basic.show_number(score)
        basic.show_string("Noul numar?")
        basic.show_number(next_number)
    else:
        basic.show_string("Gresit! Noul numar e:")
        basic.show_number(next_number)
        score = 0
        basic.show_string("Scor:")
        basic.show_number(score)
    number = next_number;
    next_number = randint(0, 100)
input.on_button_pressed(Button.B, on_button_pressed_b)
