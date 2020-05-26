# vversioning 


**vversioning** is a (quick and dirty) versioning system.

![](https://i.imgur.com/hzu7ERc.png)

For some projects you need a real code versioning system (like `git` or similar tools).

But for some others, typically micro-size projects, you sometimes **don't want to use a complex tool**. You might want to move to git *later* when the project gets bigger, or when you want to publish it online, but using git for any small project you begin creates a lot of friction for some users like me. Examples:

User A: *"I rarely use git. If I use it for this project, will I remember which commands to use in 5 years when I'll want to reopen this project? Or will I get stuck with `git wtf` and unable to quickly see the different versions?"*.

User B: *"I want to be able to see the different versions of my code even if no software like git is installed (ex: using my parents' computer)."*

User C: *"My project is just a single file. I don't want to use a complex versioning system for this."*

Here are some **dirty but working** solutions.

## **vversioning** for single-file projects

* Use a new file with an incremental suffix `...1.py`, `...2.py`, etc., each time you do significant changes (see for example `test1\` of this actual repository):

        myscript1.py
        myscript2.py
        ...

    I am sure that you have done this hundreds of times for small projects already.
    
    You could also add a date suffix e.g. `myscript_20200526_1328.py` or any other file-naming system that you like so that it is sorted correctly.

* Write changes in your source files, inside comments in such blocks:

        ==CHANGELOG==
        * list your changes here
        * new feature xyz
        ==CHANGELOG==

* Run 

        python vversioning.py test1

     to display the changes along the consecutives versions:
     
     ![](https://i.imgur.com/N2Jb2nS.png)
     
     
Note: it uses Python3, so depending on your system, you might want to do `python3 vversioning.py test1` instead.


## vversioning for multiple-file projects (aka "just archive your code in a ZIP" method)

For projects containing multiple files, just continue to use `==CHANGELOG==` blocks in your code. Then ZIP the whole folder every time you decide it's a new version. For example see `test2/` of the current repo.

![](https://i.imgur.com/03pFG3C.png)

Run:

    python vversioning.py test2
    
and here is the result:

![](https://i.imgur.com/xSR7zKp.png)

Note: Of course this doesn't scale for *big projects* because it would waste disk space, but it's totally fine to have a ZIP of 100KB for *each* of the 20 consecutive versions of a small project.

## I don't want to use vversioning anymore. Is my data lost?

No! All your changelog data is inside *your* source code files, inside your comments in ==CHANGELOG== blocks.

So if you don't want to use **vversionning** anymore, there's nothing to do, nothing to export: your data is already there, in your source code.

## Windows users

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
