# vversioning 


**vversioning** is a (quick and dirty) versioning system, done in 22 lines of Python code.

![](https://i.imgur.com/hzu7ERc.png)

For some projects you need a real code versioning system (like `git` or similar tools).

But for some others, typically micro-size projects, you sometimes **don't want to use a complex tool**. You might want to move to git *later* when the project gets bigger, or when you want to publish it online, but using git for any small project you begin creates a lot of friction for some users like me. Examples:

User A: *"I rarely use git. If I use it for this project, will I remember which commands to use in 5 years when I'll want to reopen this project? Or will I get stuck with `git wtf` and unable to quickly see the different versions?"*.

User B: *"I want to be able to see the different versions of my code even if no software like git is installed (ex: using my parents' computer)."*

User C: *"My project is just a single file. I don't want to use a complex versioning system for this. How can I archive the versions?"*

Here is a **dirty but working** solution.

## How to use it for single-file projects?

* You're probably already doing this: **just use a new file with an incremental suffix** each time you do significant changes in your code. See for example `test1/` of this actual repository:

        myscript1.py
        myscript2.py
        myscript3.py
        ...
        
    You could also use a date suffix e.g. *myscript_20200526_1328.py* or any other file-naming system that you like so that it is sorted correctly.

* **Log your changes** in your source files, inside `==CHANGELOG==` blocks (typically in top comments of your code):

        ==CHANGELOG==
        * list your changes here
        * new feature xyz
        ==CHANGELOG==

* Run 

        python vversioning.py test1

     to display the changes along the consecutive versions:
     
     ![](https://i.imgur.com/N2Jb2nS.png)
     
     
Note: it uses Python3, so depending on your system, you might need to do `python3 ...` instead of `python ...`.

## How to use it for multiple-file projects? (aka "just archive your code in a ZIP" method)

For projects containing multiple files, just continue to use `==CHANGELOG==` blocks in your code. Then ZIP the whole folder every time you decide it's a new version. For example see `test2/` of the current repo.

![](https://i.imgur.com/03pFG3C.png)

Run:

    python vversioning.py test2
    
and here is the result:

![](https://i.imgur.com/xSR7zKp.png)

How does it work? **vversioning** automatically also looks in the files inside the ZIP archives, searching for `==CHANGELOG==` blocks.

Note: Of course this doesn't scale for *big projects* because it would waste disk space, but it's totally fine to have a ZIP of 100KB for *each* of the 20 consecutive versions of a small project.

## I don't want to use vversioning anymore. Is my data lost?

No! All your changelog data is inside *your* source code files, inside `==CHANGELOG==` blocks, in your code comments.

So if you don't want to use **vversionning** anymore, there's nothing to do, nothing to export: your data is already there, in your source code.

## For Windows users

Create a file named `vversioning.bat` somewhere in your systtem PATH containing:

    @python "D:\path\to\vversioning.py"

and then you will be able to call it from anywhere, like this:

![](https://i.imgur.com/N2Jb2nS.png)
    

## Meta

Using this method is not incompatible with using `git`. For this actual project `vversioning`, I still use `==CHANGELOG==` blocks, but I will eventually use git to update this Github-hosted project.

## About

Author: Joseph Ernest ([@JosephErnest](http:/twitter.com/JosephErnest))

www.afewthingz.com

## License

MIT license

## My other projects

[SamplerBox](https://github.com/josephernest/SamplerBox), [Yopp](https://github.com/josephernest/Yopp), [Writing](https://github.com/josephernest/writing), [bigpicture.js](https://github.com/josephernest/bigpicture.js), [Void CMS](https://github.com/josephernest/void), etc.
