# AVOIDING SYNTAX ERRORS:

# 1. Make sure you are not using a Python keyword for a variable name.
#
# 2. Check that you have a colon at the end of the header of every compound statement,
# including for, while, if, and def statements.
#
# 3. Make sure that any strings in the code have matching quotation marks. Make sure
# that all quotation marks are “straight quotes”, not “curly quotes”.
#
# 4. If you have multiline strings with triple quotes (single or double), make sure you
# have terminated the string properly. An unterminated string may cause an invalid
# token error at the end of your program, or it may treat the following part of the
# program as a string until it comes to the next string. In the second case, it might not
# produce an error message at all!
#
# 5. An unclosed opening operator—(, {, or [—makes Python continue with the next line
# as part of the current statement. Generally, an error occurs almost immediately in the
# next line.
#
# 6. Check for the classic = instead of == inside a conditional.
#
# 7. Check the indentation to make sure it lines up the way it is supposed to. Python
# can handle space and tabs, but if you mix them it can cause problems. The best way
# to avoid this problem is to use a text editor that knows about Python and generates
# consistent indentation.
#
# 8. If you have non-ASCII characters in the code (including strings and comments), that
# might cause a problem, although Python 3 usually handles non-ASCII characters. Be
# careful if you paste in text from a web page or other source.


# More possible solutions:

# 1. You edited the file and forgot to save the changes before running it again. Some
# programming environments do this for you, but some don’t.

# 2. You changed the name of the file, but you are still running the old name.

# 3. Something in your development environment is configured incorrectly.

# 4. If you are writing a module and using import, make sure you don’t give your module
# the same name as one of the standard Python modules.

# 5. If you are using import to read a module, remember that you have to restart the
# interpreter or use reload to read a modified file. If you import the module again, it
# doesn’t do anything.

# 6. If you get stuck and you can’t figure out what is going on, one approach is to start again
# with a new program like “Hello, World!”, and make sure you can get a known program to
# run. Then gradually add the pieces of the original program to the new one.


# OTHER THINGS IN APPENDIX A:

# Runtime errors:
# -> Programme does nothing
# -> Programme hangs
# -> Infinite loop
# -> Infinite recursion
# -> Flow of execution
# -> Exceptions (for which the Python debugger is useful, see https://docs.python.org/3/library/pdb.html)

# Semantic errors