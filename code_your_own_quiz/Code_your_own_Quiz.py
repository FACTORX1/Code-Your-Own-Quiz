#!/usr/bin/python
from string import Template


#level 1 easy
level_1 = '''
	Python is a widely used $answ1-level programming language for general-purpose $answ2, created by Guido van Rossum and first released in 1991.
	An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code
	blocks rather than curly brackets or keywords), and a syntax which allows $answ3 to express concepts in fewer lines of code than
	might be used in languages such as C++ or Java.The language provides constructs
	intended to enable writing clear $answ4 on both a small and large scale.
'''

# level 2 medium
level_2 = '''
        C was originally developed by $answ1 Ritchie between 1969 and 1973 at Bell Labs, and used to re-implement the Unix operating system.
        It has since become one of the most widely used programming languages of all time, with
        C compilers from various vendors available for the majority of existing computer architectures and operating systems. C has been
        standardized by the American National Standards Institute (ANSI) since $answ2 (see ANSI C) and subsequently
        by the International Organization for Standardization (ISO).
	K&R introduced several language features:

        Standard $answ3 library
        long int data type
        unsigned int data type
        Compound assignment operators of the form =op (such as =-) were changed to the form op= (that is, -=) to remove the semantic ambiguity created
        by constructs such as i=-10, which had been interpreted as i =- 10 (decrement i by 10) instead of the possibly intended i = -10 (let i be -10).
        Even after the publication of the 1989 ANSI standard, for many years K&R C was still considered the "lowest common denominator" to which
        C programmers restricted themselves when maximum portability was desired,
        since many older compilers were still in use, and because carefully written $answ4 C code can be legal Standard C as well.
'''

# level 3 hard
level_3 = '''
	Facebook is an American for-profit corporation and an online social media and social networking service based in Menlo Park, California.
	The Facebook website was launched on February 4, 2004, by Mark Zuckerberg, along with fellow $answ1 College students and roommates,
	$answ2, Andrew McCollum, Dustin Moskovitz, and Chris Hughes.

        The founders had initially limited the website's membership to Harvard students; however,
        later they expanded it to higher education institutions in the Boston area, the Ivy League schools, and Stanford University.
        Facebook gradually added support for students at various other universities, and eventually to high school students as well.
        Since 2006, anyone age $answ3 and older has been allowed to become a registered user of Facebook, though variations exist in the minimum age requirement,
        depending on applicable local laws. The Facebook name comes from the face book directories often given to United States university students.

        Facebook may be accessed by a large range of $answ4, laptops, tablet computers, and smartphones over the
        Internet and mobile networks. After registering to use the site, users can create a user profile indicating their name,
        occupation, schools attended and so on. Users can add other users as "friends", exchange messages, post status updates and digital photos,
        share digital videos and links, use various software applications ("apps"), and receive notifications when others update their profiles or make posts.
        Additionally, users may join common-interest user groups organized by workplace, school, hobbies or other topics, and categorize their friends into lists
        such as "People From Work" or "Close Friends". In groups, editors can pin posts to top. Additionally, users can complain about or block unpleasant people.
        Because of the large volume of data that users submit to the service, Facebook has come under scrutiny for its privacy policies.
        Facebook makes most of its revenue from advertisements which appear onscreen.
'''
#level 4 very hard
level_4= '''
        Google is an American multinational technology company specializing in Internet-related services and products.
        These include online advertising technologies, $answ1, cloud computing, software, and hardware. Google was founded in 1998 by
        Larry Page and Sergey Brin while they were Ph.D. students at Stanford University, in California. Together, they own about 14 percent of its
        shares, and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a privately held company on
        September 4, 1998. An initial public offering (IPO) took place on August 19, 2004, and Google moved to its new headquarters in $answ2,
        California, nicknamed the Googleplex. In August 2015, Google announced plans to reorganize its various interests as a conglomerate
        called Alphabet Inc. Google, Alphabet's leading subsidiary, will continue to be the umbrella company for Alphabet's Internet interests.
        Upon completion of the restructure, Sundar Pichai became CEO of Google, replacing $answ3, who became CEO of Alphabet.

        Rapid growth since incorporation has triggered a chain of products, acquisitions, and partnerships beyond Google's core search engine
        (Google Search). It offers services designed for work and productivity (Google Docs, Sheets and Slides), email (Gmail/Inbox),
        scheduling and time management (Google Calendar), cloud storage (Google Drive), social networking (Google+), instant messaging and
        video chat (Google Allo/Duo), language translation (Google Translate), mapping and turn-by-turn navigation (Google Maps/Waze), video sharing (YouTube),
        notetaking (Google Keep), and photo organizing and editing (Google Photos). The company leads the development of the Android mobile operating system,
        the Google Chrome web browser, and Chrome OS, a lightweight operating system based on the Chrome browser. Google has moved increasingly into hardware;
        from 2010 to 2015, it partnered with major electronics manufacturers in the production of its Nexus devices, and in October 2016, it released
        multiple hardware products (including the Google Pixel smartphone, Home smart speaker, Wifi mesh wireless router, and Daydream View virtual reality headset).
        The new hardware chief, $answ4, stated: "a lot of the innovation that we want to do now ends up requiring controlling the end-to-end user experience".
        Google has also experimented with becoming an Internet carrier. In February 2010, it announced Google Fiber, a fiber-optic infrastructure that was
        installed in Kansas City; in April 2015, it launched Project Fi in the United States, combining Wi-Fi and cellular networks from different providers;
        and in 2016, it announced the Google Station initiative to make public Wi-Fi around the world,
        with initial deployment in India.
'''


substitution = {
	'answ1': '-1-',
	'answ2': '-2-',
	'answ3': '-3-',
	'answ4': '-4-'
}

# solution of level 1
solution1 = {
	'answ1': 'high',
	'answ2': 'programming',
	'answ3': 'programmers',
	'answ4': 'program'
}

# solution of level 2
solution2 = {
	'answ1': 'Dennis',
	'answ2': '1989',
	'answ3': 'I/O',
	'answ4': 'K&R'
}
# solution of level 3
solution3 = {
	'answ1': 'hardvard',
	'answ2': 'Eduardo Saverin',
	'answ3': '13',
	'answ4': 'Desktop'
}
# solution of level 4
solution4 = {
	'answ1': 'search',
	'answ2': 'Mountain View',
	'answ3': 'Larry Page',
	'answ4': 'Rick Osterloh'
}

def check(answer, question, solution):
	'''
	  answer: string --> answer that user typed
	question: string --> the current question key in solution
	solution: string --> the solution dictionary 
	return True if answer is the solution of the question
		  False if answer is not the solution
	'''
	
	if solution.get(question) != None and solution[question] == answer:
		return True
	else:
		return False


def get_level():
	'''
	ask the user which level to play,
	get the corresponding level template and solution,
	return a tuple (level, solution)
	   level: Template --> the corresponding string template of the user selected level
	solution: dict     --> the solution dictionary of the corresponding level
	'''
	print('Please choose a difficulty level from easy / medium / hard / very hard')
	levelTemplate = None		
	solution = None				
	while(solution == None):	
		level = str(input())
		if(level == 'easy'):
			#  easy --> level 1
			levelTemplate = Template(level_1)
			solution = solution1
		elif(level == 'medium'):
			#  medium --> level 2
			levelTemplate = Template(level_2)
			solution = solution2
		elif(level == 'hard'):
			#  hard --> level 3
			levelTemplate = Template(level_3)
			solution = solution3
		elif(level == 'very hard'):
			#  hard --> level 4
			levelTemplate = Template(level_4)
			solution = solution4
		else:
			#  user didn't type any valid level
			print('Please choose a real level that actually exists!')
	print('You choosed level ' + level)
	return (levelTemplate, solution)


def main():
	levelTemplate, solution = get_level()	
	current = 1				
	total = len(solution)	
    #string = levelTemplate.substitute(substitution)
    #print(levelTemplate.substitute(substitution))
    #print(get_level())
	while current <= total:
		string = levelTemplate.substitute(substitution);
		question = 'What should go in blank number ' + str(current) + '?'
		print(string)
		print(question)
		answe = input()
		fill = 'answ'+str(current)	
		if check(answe, fill, solution):
			
			substitution[fill] = answe
			print('Right Answer!')
			current += 1
		else:
		
			print('Wrong Answer!')
		print('\n--------------------------------------------------------------------------------\n')

	
	print('Congratulation!!!!!!!! you won!')
	

main()
print('Want to play again')
print('y or n')
option=input()
if(option=='y'):
    main()
else:
    print("Thank You for playing the game")
