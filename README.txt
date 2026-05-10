For this Assignment, there are three main modules: a2.py, ui.py, and Profile.py.

a2.py is the front end of the program that contains the main() function. ui.py contains most of the methods and functionality. Profile holds information for the Profile and Post classes.

The program as a whole allows you to create, open read, delete, edit, and print any .dsu file in your given directory. Each created file is associated with a Profile object, which contains a dsuserver, username, password, bio, and posts. These attributes can be edited and printed, with the E and P commands in ui.py.

There are two different user-interfaces/modes. A user friendly mode that gives explanations and a clear structure to the program. It also explains any possible errors that might appear. The second mode is admin mode which can be entered at the start of the program by entering "admin". This mode has minimal prints, direction, and expects all commands to be entered in a single line. Any errors that may arise only print "ERROR".