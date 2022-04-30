from guizero import App, Box, PushButton, Drawing

def keyboard():
    global opperation
    opperation = ""
    count=0


    for number in range(10):
        if number >=1 and number < 4:
            button = PushButton(box_numbers, text=str(number), grid=[count, 1], command=writting, args=[number])
            count+=1
        if number >= 4 and number < 7:
            if number == 4 :
                count = 0
            button = PushButton(box_numbers, text=str(number), grid=[count, 2], command=writting, args=[number])
            count+=1
        if number >= 7:
            if number == 7:
                count=0
            button = PushButton(box_numbers, text=str(number), grid=[count, 3], command=writting, args=[number])
            count+=1
        if number == 0:
            button = PushButton(box_numbers, text=str(number), grid=[2, 4], command=writting, args=[number])
    button = PushButton(box_numbers, text=">", grid=[3, 4], command=enter)
    button = PushButton(box_numbers, text="<", grid=[0, 4])
    button = PushButton(box_numbers, text=".", grid=[1, 4], command=writting, args=["."])
    button = PushButton(box_numbers, text="-", grid=[2, 0,3, 1 ], command=writting, args=["-"], height = 1, width = 6)
    button = PushButton(box_numbers, text="+", grid=[3, 1, 4, 2], command=writting, args=["+"], height = 4, width = 1)
    button = PushButton(box_numbers, text="*", grid=[1, 0], command=writting, args=["*"])
    button = PushButton(box_numbers, text="/", grid=[0, 0], command=writting, args=["/"])


def enter():
    global line, x, y, opperation
    left_part=0
    calcul=""
    result=0.0
    for index, character in enumerate(opperation):
        if character == "*" or character == "/" or character == "+" or character == "-":
            calcul = character
            left_part=opperation[:index]

    right_part = opperation[len(str(left_part))+1:]  
    if calcul == "*":
        result=int(left_part)*int(right_part)
    if calcul == "/":
        result=round(int(left_part)/int(right_part), 3)
    if calcul == "+":
        result=int(left_part)+int(right_part)
    if calcul == "-":
        result=int(left_part)-int(right_part)
    print(round(result,3))
    drawing.text(0, y[line+1]+3, str(result), size = 20)
    line+=2
    opperation=""
    

def writting(player_input):
    global opperation
    inputed=[0,20,40,60,80,100,120]
    opperation += str(player_input)
    drawing.text(inputed[len(opperation)-1], y[line]+2, str(player_input), size = 20)
    print(opperation)



app = App(title="Calculator", width=300, height=500)
app.bg=(32,32,32)
line=0
y=[0,20,40,60,80,100,120,140,160,180,200,220,240]

box_numbers=Box(app,layout="grid", align="right")
box_numbers.bg=(85,85,85)
box_drawing =Box(app, align="left")
box_drawing.bg=(120,120,120)


drawing=Drawing(box_drawing, width=150, height=200)


keyboard()
    
app.display()