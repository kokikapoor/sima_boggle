from tkinter import*

class right_panel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        '''
            Create questions button
        '''
        self.questions = Button(frame, text="?", command=lambda: instructions())
        self.questions.place(relx=.94, rely=0.01, relwidth=.05, relheight=.05)

        '''
            Creates a pop-up window of the instructions
        '''
        def instructions():
            self.instructions = Frame(root, bg='#80c1ff', bd=5)
            self.instructions.place(relx=.1, rely=.1, relwidth=.8, relheight=.8)
            # base_folder = os.path.dirname(__file__)
            # image_path = os.path.join(base_folder, 'left_background.png')
            # info = PhotoImage(file=image_path)
            # info_image = Label(root, image=info)
            # info_image.place(relwidth=.5, relheight=1)
            self.x_questions = Button(self.instructions, text="X", command=self.instructions.destroy)
            self.x_questions.place(relx=.94, rely=0.01, relwidth=.05, relheight=.05)

        self.clicked = StringVar()
        self.clicked.set("Number of Players")

        # self.options = [2,3,4,5,6,7,8,9,10]
        # self.drop = OptionMenu(frame, self.clicked, *self.options)
        # self.drop['width'] = 53
        # self.drop.config(font=('Helvetica',20)) 
        # self.drop.place(relx=.3, rely=.1, relwidth=.4, relheight=.05)

        self.timer_frame = Frame(frame, bg='#fa9300', bd=5)
        self.timer_frame.place(relx=0.0833, rely=0.07, relwidth=0.83, relheight=0.11)

        def countdown(count):
            m, s = divmod(count, 60)
            if m < 10:
                minutes = "0" + str(m)
            else:
                minutes = str(m)

            if s < 10:
                seconds = "0" + str(s)
            else:
                seconds = str(s)

            time_formated = minutes + ":" + seconds
            self.timer['text'] = time_formated

            if count >= 0:
                # call countdown again after 1000ms (1s)
                self.root.after(1000, countdown, count-1)
            
            if count == -1:
                self.root.after(50)
                self.timer['fg']='#c63420'
                self.timer['text'] = "Time's up!"

        self.timer = Label(self.timer_frame, font=("Comic Sans MS", 35), fg = 'black', justify='center')
        self.timer.place(relwidth=1, relheight=1)

        # call countdown first time    
        countdown(5)
        # root.after(0, countdown, 5)