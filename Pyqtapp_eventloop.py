#  core of any PyQt application
# manages the application’s control flow as well as its main settings
# any instance of QApp =>  an application
# Every PyQt GUI application must have one QApplication object
# responsibilities :
# Handling initialization and finalization
# Providing the event loop and event handling
# Handling most of the system-wide and application-wide settings
# Providing access to global information, such as the application’s directory, screen size etc.
# Parsing common command-line arguments
# Defining the application’s look and feel
# Providing localization capabilities
# these  just some
# +++++++++++++++++++++++++++++
# methods are executed in response to user actions
# The event loop waits for an event to occur and then dispatches it to perform some task
# The event loop continues to work until the application is terminated.
#  infinite loop that waits for the occurrence of events
# Terminate event
# In PyQt, you can run the application’s event loop by calling .exec_() on the QApplication object. or  .exec()
# trigger a response action => you can establish that connection by using the signals and slots mechanism
#
#
#
#
#
#
#
