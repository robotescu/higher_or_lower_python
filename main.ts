let number = randint(0, 100)
let next_number = randint(0, 100)
let score = 0
basic.showNumber(number)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (next_number <= number) {
        basic.showString("Bravo! scor:")
        score += 1
        basic.showNumber(score)
        basic.showString("Noul numar:")
        basic.showNumber(next_number)
    } else {
        basic.showString("Gresit! Noul numar e:")
        basic.showNumber(next_number)
        score = 0
        basic.showString("Scor:")
        basic.showNumber(score)
    }
    
    number = next_number
    next_number = randint(0, 100)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (next_number >= number) {
        basic.showString("Bravo! Scor:")
        score += 1
        basic.showNumber(score)
        basic.showString("Noul numar?")
        basic.showNumber(next_number)
    } else {
        basic.showString("Gresit! Noul numar e:")
        basic.showNumber(next_number)
        score = 0
        basic.showString("Scor:")
        basic.showNumber(score)
    }
    
    number = next_number
    next_number = randint(0, 100)
})
