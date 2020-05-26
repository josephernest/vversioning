# vversioning 


**vversioning** is a (quick and dirty) versioning system.

For some projects you need a real code versioning system (like `git` or similar tools).

But for some others, typically micro-size projects, you sometimes don't want to use a complex tool. You might want to move to git *later* when the project gets bigger, or when you want to publish it online, but using git for any small project you begin creates a lot of friction for some users like me. Examples:

User A: *"I rarely use git. If I use it for this project, will I remember which commands to use in 5 years when I'll want to reopen this project? Or will I get stuck with `git wtf` and unable to quickly see the different versions?"*.

User B: *"I want to be able to see the different versions of my code even if no software like git is installed (ex: using my parents' computer)."*

User C: *"My project is just a single file. I don't want to use a complex versioning system for this."*

Here are some **dirty but working** solutions.

## **vversioning** for single-file projects

* Write code (see for example `test1\` of this actual repository):

        myscript1.py
        myscript2.py
        ...

    (the latest is the more recent). 

* Write changes in your source files, inside comments in such blocks:

        ==CHANGELOG==
        * list your changes here
        * new feature xyz
        ==CHANGELOG==

* Run 

        python versioning.py test1

     to display the changes along the consecutives versions:
     
     ![](https://i.imgur.com/N2Jb2nS.png)


## vversioning for bigger projects



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
