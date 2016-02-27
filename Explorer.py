from sys import exit

def gold_room():
	print "This room is full of gold.  How many pieces of gold do you take? \
Choose your number carefully!"
	while True:
		choice = raw_input("> ")
		if "0" in choice or "1" in choice:
			how_much = int(choice)
		else:
			dead("Man, learn to type a number.")

		if how_much < 50:
			print "Nice, you're not greedy, you win!"
			exit(0)
		else:
			dead("You greedy bastard!")


def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in the front of another door."
	print "How are you going to move the bear?"
	print "Will you taunt bear or take the honey?"
	bear_moved = False

	while True:
		choice = raw_input("> ")

		if "honey" in choice:
			dead("The bear looks at you then slaps your face off.")
		elif "taunt" in choice and not bear_moved:
			print "The bear has moved from the door.  You can go through it now."
			print "Will you taunt bear again or open door?"
			bear_moved = True
		elif "taunt" in choice and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif "open door" or "open" in choice and bear_moved:
			snake_room()
		else:
			print "I got no idea what that means."


def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for you life or eat your head?"

	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def snake_room():
	print "You stumble into a chamber of snakes. There are 20 of them."
	print "They are Phillipine Cobras.  One of the deadliest snakes in the world"
	print "Fortunately for you, they are sleeping."
	print "A wrong move, however, may change your fortune."
	print "Do you grab the closest snake and play jump rope or "
	print "Do you run through the room as fast as you can?"
	snakes_wowed = False

	while True:
		choice = raw_input("> ")

		if "run" or "jump" in choice:
			dead("The snakes wakeup and jump you. You slowly lose conscious as the snakes \
make you their lunch!")
		elif "grab" or "jump rope" or "jump" in choice:
			print "The other cobras wake up.  Their gaze pierces and they make \
their menace known"
			snakes_wowed = True
			print "Do you jump snake-rope to the exit or throw the snake and run for it"
		elif "jump" in choice and snakes_wowed:
			dead("The snakes catch you and push their poison into you.  You die in your own \
defecation")
		elif "run" in choice and snakes_wowed:
			print "You manage to make it through"
			gold_room()
		else:
			print "I have no idea what you mean! English! Do you speak it?"

def dead(why):
	print why, "Good Job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

	choice = raw_input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around in the room until you starve.")


start()
