from tkinter import *	
import random
import pygame as py	

HUMAN_SCORE= 0
COMPUTER_SCORE=0
human_choice = ""
computer_choice = ""

def rungame(start):
	start.destroy()
	start.quit()
	global HUMAN_SCORE,COMPUTER_SCORE


	def choice_to_number(choice):
		rps_dict = {'rock':0,'paper':1,'scissors':2}
		return rps_dict[choice]


	def number_to_choice(number):
		rps_dict = {0:'rock',1:'paper',2:'scissors'}
		return rps_dict[number]

	def random_computer_choice():
		return random.choice(['rock','paper','scissors'])

	def choice_result(human_choice,computer_choice):
		global COMPUTER_SCORE
		global HUMAN_SCORE

		human_number=choice_to_number(human_choice)
		computer_number=choice_to_number(computer_choice)

		if (human_number-computer_number)%3 == 1 :
			COMPUTER_SCORE = COMPUTER_SCORE + 1	
			cscore.configure(text=("Comp Score :",COMPUTER_SCORE))
			draw.configure(text="Computer won")



		elif human_number== computer_number:
			draw.configure(text="Draw")
		else:
			HUMAN_SCORE = HUMAN_SCORE + 1
			yscore.configure(text=("Your Score :",HUMAN_SCORE))
			draw.configure(text="You won")


	def rock():

		global human_number,computer_number
		global HUMAN_SCORE,COMPUTER_SCORE

		human_choice='rock'

		computer_choice= random_computer_choice()
		choice_result(computer_choice,human_choice)

	def paper():

		global human_number,computer_number
		global HUMAN_SCORE,COMPUTER_SCORE

		human_choice='paper'

		computer_choice= random_computer_choice()
		choice_result(computer_choice,human_choice)

	def scissors():

		global human_number,computer_number
		global HUMAN_SCORE,COMPUTER_SCORE

		human_choice='scissors'

		computer_choice= random_computer_choice()
		choice_result(computer_choice,human_choice)



	#window
	window = Tk()
	window.title("Rock-Paper-Scissors")
	window.configure(background="PeachPuff2")
	window.geometry("400x400")

	#buttons
	Rock = Button(window,text="Rock",command=rock)
	rock_photo=PhotoImage(file="rock_button.gif")
	Rock.config(image=rock_photo,width="120",height="120")
	Paper = Button(window,text="Paper",command=paper)
	paper_photo=PhotoImage(file="paper_button.gif")
	Paper.config(image=paper_photo,width="120",height="120")
	Scissors = Button(window,text="Scissors",command=scissors)
	scissors_photo=PhotoImage(file="scissors_button.gif")
	Scissors.config(image=scissors_photo,width="120",height="120")
	Rock.pack(padx=5, pady=5, side=LEFT)
	Paper.pack(padx=5, pady=10, side=LEFT)
	Scissors.pack(padx=5, pady=10, side=LEFT)
	result = StringVar()
			


	#text
	yscore = Label(window,text=("Your Score :",HUMAN_SCORE),bg="PeachPuff2",fg="Black")
	draw  =  Label(window,text ="Have Fun!",bg = "PeachPuff2",fg="Black",font='Helvetica 22 bold')
	cscore = Label(window,text=("Comp Score :",COMPUTER_SCORE),bg="PeachPuff2",fg="Black")
	

	yscore.place(x=100,y=350)
	draw.place(x=125,y=50)
	cscore.place(x=250,y=350)

	


	window.mainloop()


start=Tk()
py.init()
py.mixer.music.load("start_music.mp3")
py.mixer.music.play(-1)
start.configure(bg="#efe8ce")
start.title("Lets Play !!")
start.geometry("500x310")

photo1 = PhotoImage(file="screen.gif")
lbl = Label (start, image=photo1, bg="#efe8ce")
bttn = Button(start,text="PLAY",command=lambda:rungame(start))
bttn.pack(side="bottom")
lbl.pack()
start.mainloop()