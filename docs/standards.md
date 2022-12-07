# Repository Standards (Coding style, file structure, etc.)

## Commit Descriptions

Whenever you create a commit to push to the repository, make sure you put the name of each file / folder you changed, added, or removed followed by a new line with a numbered list of each change that was made to that file / folder.

Example:

**Summary:** ```Optmized scanning modules```

**Description:**
```
distance.py
1. Removed print statements that were used for debugging in waitForResponse()
2. Removed some useless import statements that were used previously for debugging

output.py
1. Removed a for loop that recounted the number of output files every time a new file was created and replaced it with a counter that increments each time a new file is created
2. Added a print statement that says what directory the output files were created in
3. Changed some comments for some of the global values to be more specific about what they do

scan_lib.py
1. Removed this file since everything it did was spread out to other files

UnitTest.py
1. Changed the name of this file to "unit_test.py" to fit the coding style standards

scan_modules
1. Changed the name of this folder to just "scan"
```

If 2 different files that were changed have the same name, include the directory path (relative to the repository root) to those files in the name that goes above the numbered list of changes.
Also try to keep commits to just one "theme". Ex: If you change a bunch of files in 2 different directories that are unrelated, commit and push the changes for each directory one at a time.

Example:
```
/src/FolderOne/example.py
1. Changes...

/src/FolderTwo/example.py
1. Changes...
```

Make sure your titles give a good overview of all of your changes as well!

## File / Directory Structure

All "main" program files should be stored in [/src](/src).

"Main" program files are the files that you actually call to execute when you run a program and don't get called by any other files.

All "import" program files should be stored in categorically organized subdirectories in [/src](/src).

All documentation files should be stored in [/docs](/docs).

## File / Directory Names

TLDR: Lowercase snake casing

File names for source code files will be all lowercase and use snake casing (using underscores to represent spaces).

Examples of snake casing:

```
parse_utils.py
output_lib_cleaner.py
unit_test.py
```

## Documentation Files

TLDR: All doc files should be ".md" files, have markdown formatting to make it look nice, and be well written.

All documentation files should be ".md" text files so they can be easily read on GitHub. Be sure to include some decent formatting as well to make it look nice.

[Here's a tutorial on how to use markdown formatting.](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

Make sure that your documentation files are well organized and clearly written as well!

## Class / Custome Type Names

TLDR: Upper camel case

Class names and other custom type names will be defined in upper camel casing. This means that the first letter of each class and custom type should be uppercase as well as the first letter of other words in the name.

Examples of upper camel casing:

```
CustomType
CarInfo
SuperLongInt
```

## Function Names

TLDR: Lower camel case

Function names will be defined in upper camel casing. This means that the first letter of each function will be lowercase, and the first letter of each following word in the name will be uppercase.

Examples of lower camel casing:

```
isNumber()
detectRange()
parseWithTypes()
```

## Variable Names

TLDR: Lowercase snake casing

Variable names will follow the same naming convention as file names.

Examples of lower camel casing:

```
tree_node
long_file_query
public_key
```

## Indenting

Use actual tabs, not spaces. **Make sure your text editor doesn't just input 4 spaces when you press tab, set it to input an actual tab character otherwise your programs might not compile!**

## Comments

There should be a comment above every function that describes what it does, what to input into it, and what it outputs / returns. Try to also put a comment above every loop, if / if-else statement, and variable too.
Comments should go on the line(s) right above the thing you're commenting about.
At the start of every file that will be used in the long term, there should also be a comment of this form:

```
########################################################################################################################
#
#
# University of Idaho Robotics Club, Mobile Robot Team
#
# Description of what this file is for
#
# Authors / Contributors:
# Firstname Lastname (Time person was a part of team)
# Bob Smith (Fall 2022 - Spring 2023)
#
#
########################################################################################################################
```

You can just copy and paste this text and use it as a template to start each new file.
Code should also be organized into sections of functions / classes that do similar things or chronologically based on execution order. Each section should have a comment similar to the one above at the start that describes what that section is.

Examples / templates:

```
########################################################################################################################
#
#
# Title of Section
#
#
########################################################################################################################
```
```
########################################################################################################################
#
#
# Title of Section
#
# Description of the section or notes about the section can go here if necessary. Text in this part can go to the end of
# the hashes at the top and bottom and then wrap like this.
#
#
########################################################################################################################
```