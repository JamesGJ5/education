# 14.1 PERSISTENCE:

# Persistent programmes run for a long time/always and keep at least some data in
#   permanent storage, e.g. by reading/writing text files. Such programmes include operating systems and web servers.


# 14.2 READING AND WRITING:

# The return value of the write method is the number of characters that were written
#   to the file said method operated on.

# As below, you can use the write method to append to a file that has already been
#   written.
# fout = open("practice", "w")
# fout.write("aloha")
# fout.write("jum")
# fout.close()

# The file gets closed when the entire programme ends, if it isn't manually closed
#   with the close() method earlier in the programme.


# 14.3 FORMAT OPERATOR:

# "%d" formats a nuber into an integer in a string, "%g" a number into a
# floating-point number in a string and "%s" a string into a string.

# A more powerful alternative is the string format method:
#   https://docs.python.org/3/library/stdtypes.html#str.format


# 14.4 FILENAMES AND PATHS:

# # A relative path is one that relates to the current directory, e.g. Questions.txt
# #   in this current working directory.
#
# import os
# print("\n" + os.getcwd())
#
# # A path that begins with / doesn't depend on the current directory, and is called
# #   an absolute path; Questions.txt also has its own absolute path.
# print(os.path.abspath("Questions.txt"))
# # N.B: modern Windows can generally use / and \ interchangeably, according to a
# #   comment on https://stackoverflow.com/questions/38428561/difference-between-forward-slash-and-backslash-in-file-path/38428899
#
# print(os.path.exists("Questions.txt"))
# print(os.path.isdir("C:/Users/james/PycharmProjects/thinkpython2"))
#
# # os.path.isfile
# # os.listdir
# # os.path.join


# 14.5 CATCHING EXCEPTIONS:
#
# import os
# fin = open("C:/Users/james/PycharmProjects/thinkpython2/14.4_exercise")
#

# 14.6 DATABASES:

# The biggest difference between a database and a dictionary is that the database
#   is on disk (or other permanent storage), so it persists after the program ends.

# import dbm
# db = dbm.open("captions", "c")
#
# # Databases can be used (for most operations) like a dictionary.
# db["cleese.png"] = "Photo of John Cleese."
#
# # The result of the below is a bytes object, which is why it begins with b
# print(db["cleese.png"])
#
# # The keys() and items() dictionary methods, for example, don't work with databases.
# # Close a database when you are done with it.


# 14.7 PICKLING:

# Limitation of dbm: keys and values in dbm must be strings or bytes; pickle module
#   translates most types of objects into a string for database storage, then
#   translates strings back into objects when necessary.

# When you use the dumps() method followed by the loads() method, or perhaps vice
#   versa, the initial and final objects should have the same value but generally
#   are not the exact same object, so t1 == t2 will return True, but t1 is t2 won't -
#   t1 and t2 are copies of one another.

# The shelve module utilises pickle to store non-strings in a database.


# 14.8 PIPES:

# Any programme that can be launched from a shell (jargon for a command-line
#   interface, like Unix, provided by an operating system) can also be launched
#   from Python using a pipe object.

import os

# # In the book, "ls -l" is used rather than "dir"; that is for the UNIX shell, which
# #   I do not have. dir is the equivalent command for the cmd commands under Windows,
# #   listed at https://www.thomas-krenn.com/en/wiki/Cmd_commands_under_Windows
# cmd = 'dir'
# fp = os.popen(cmd)
# res = fp.read()
# # print(res)
# stat = fp.close()
#
# # The return of fp.close() is None if the pipe ends normally without any errors.
# print(stat)


# 14.9 WRITING MODULES:

# 14.9 clarifies why programmes that'll be imported as modules often use the
#   __name__ == '__main__' idiom.
# Warning: If you import a module that has already been imported, Python does
#   nothing. It does not re-read the file, even if it has changed. The built-in
#   function reload can reload a module but it is safer to restart the interpreter
#   and re-import the module instead.

# # The . below allows me to import a file from the subdirectory
# #   of a directory in the current working directory.
# from exercise14_4.directory1 import dasd
#
# print(dasd.linecount("words.txt"))


# 14.10 DEBUGGING:

# built-in function repr takes any object and returns a string representation of
#   it, e.g. a newline will appear as \n - this is helpful for debugging if you
#   want to get rid of whitespace, which is oft invisible.

# I put a tab after the 1 below, but it will show up as appears in the string, not
#   with a \t
print(repr("1   2"))
# This will show up without the \t, but with whitespace instead
print("1\t2")
# This will show up with the \t
print(repr("1\t2"))

# Moving files between different systems, e.g. from one where \n marks the end of a
#   line to one where \r marks the end of the line, inconsistencies can be problematic
#   so applications are oft used for conversion for most systems, e.g can be found
#   at http://en.wikipedia.org/wiki/Newline (the application, that is).