# Python 学习心得

## Git
### 8/27

-	Github上，在pull request被接受之前，commit会持续更新，merge后以最后一次更新为准。
-	Version Control System (VCS)
-	问题，无法在git中创建库可能是命令不可用
-	Git 工作区用 checkout -- file 修改, stage区 用 git reset HEAD file 退回工作区，commit后用 git reset –hard HEAD^进行版本退回。
-	Git rm 删除文件
-	Checkout 的本质是有版本库里的文件替换工作区的文件因此可以用于误删。

### 8/28
-	添加远程库
git remote add origin git@github.com:michaelliao/learngit.git
git push –u（第一次使用的参数） origin master
-	克隆远程库
  git clone git@github.com:michaelliao/gitskills.git
-	创建分支
  git checkout –b <branch name>(创建并切换)
  等同于 git branch + git checkout
-	合并分支到当前分支 git merge
-	删除分支  git branch –d
-	当无法merge是需要手动解决冲突
-	保留分支历史的merge方法（关闭fastforword）
git merge --no-ff -m "merge with no-ff" dev
-	Bug分支
git stash—储藏工作区
git stash （list）/apply（保留stash内容）/pop（不保留stash内容）
可多次stash
-	在当前分支时无法删除此分支
-	git branch –D  强制删除
-	本地创建与远程对应的分支
git branch --set-upstream branch-name origin/branch-name
-	抓取远程心得提交
git pull
-	把本地分支push到远程
git push origin branchname
-	在远程创建与本地分支相关联的分支
git push --set-upstream origin branchname
-	总的来说，先建立联系-抓取-推送
-	创建标签
git tag <tag name>
git tag <tag name> <commit id>
git tag –a <tag name> -m “messege”
-	删除git tag –d <tag name>
-	推送
git push origin <tag name>
git push origin –tags
-	删除已推送标签
  本地删除
git push origin :refs/tags/v1.1

### Learn python the hard way

### 8/29
Power shell
-	Pwd-print working directory
-	Cd ~-get home
-	Hostname-my computer’s network name
-	Mkdir-make directory
-	Cd-change directory
-	Ls-list directory
-	Rmdir-remove directory
-	Pushd-push directory
-	Popd-pop directory
-	Cp-copy a file or directory(will overwrite exist files)
-	New-item –meke new files
-	Robocopy-robust copy
-	Mv-move a file or directory or rename it.
-	More-page through a file
-	Type-print the whole file
-	Forfiles-run a command on lots of files
-	Dir –r –find files
-	Select-string – find things inside files
-	Help- read a manual page
-	Helpctr-find what man page is appropriate
-	Echo print some arguments
-	Exit-exit the shell
-	Runas-become super user root
Ls&dir-R 的区别？
rm & rmdir？rmdir empty directory ; rm unempty directory
mkdir –p中参数-p 的作用？
Copy a file to your home directory or desktop.

## Python 2.7
-	在python目录下，键入 “.\python”运行python
-	Quit（）退出


### 8/30

Python 2.7
-	[Environment]::SetEnvironmentVariable("Path", "$env:Path;D:\Python27", "User")设置环境变量，红色部分为路径。
-	1/4=0；1.0/4.0=0.25=1.0/4=1/4.0
-	Variables‘ names begin with a character.
-	%s-字符串替换, %d-用整数替换, %r-represent 完全与输入的一样，%f-浮点数
-	变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
-	在Python中，通常用全部大写的变量名表示常量。
-	每一行代码最好不要超过80个字母，good coding style
-	在formatter忘记放入符号
-	“”“……”””
-	pydoc.py <name> ...
    Show text documentation on something. <name> may be the name of a
    Python keyword, topic, function, module, or package, or a dotted
    reference to a class or function within a module or module in a
    package. If <name> contains a '\', it is used as the path to a
    Python source file to document. If name is 'keywords', 'topics',
    or 'modules', a listing of these things is displayed.
-	Argv – argument variable
-	Modules—features—libraries

### 8/31

-	Function-method-command
-	close -- Closes the file. Like File->Save.. in your editor.
-	read -- Reads the contents of the file. You can assign the result to a variable.
-	readline -- Reads just one line of a text file.
-	truncate -- Empties the file. Watch out if you care about the file.
-	write('stuff') -- Writes "stuff" to the file.
-	There's too much repetition in this file. Use strings, formats, and escapes to print out line1, line2, and line3 with just one target.write() command instead of six.???
Use target.write(“%s\n%s\n%s\n” % (line1,line2,line3)) 这是把%应用于stirng，要是把%放在外面是要把%应用在target.write上，不对。
-	Def——，function：After the colon（冒号） all the lines that are indented four spaces will become attached to this name,
Function checklist
-	Did you start your function definition with def?
-	Does your function name have only characters and _ (underscore) characters?
-	Did you put an open parenthesis ( right after the function name?
-	Did you put your arguments after the parenthesis ( separated by commas?
-	Did you make each argument unique (meaning no duplicated names)?
-	Did you put a close parenthesis and a colon ): after the arguments?
-	Did you indent all lines of code you want in the function four spaces? No more, no less.
-	Did you "end" your function by going back to writing with no indent (dedenting we call it)?
-	Did you call/use/run this function by typing its name?
-	Did you put the ( character after the name to run it?
-	Did you put the values you want into the parenthesis separated by commas?
-	Did you end the function call with a ) character?
-	documentation comments
def ……….
	“””docementation comments”””
-	from ex25 import *  --- Import everything from ex25
-	pop(num) ----(0,1,2,3…..) or (….-2,-1)

### 9/1

-	and
-	or
-	not
-	!= (not equal)
-	== (equal)
-	`>=` (greater-than-equal)
-	<= (less-than-equal)
-	True
-	False
-	Is
-	Is not
-	An if-statement creates what is called a "branch" in the code.
-	A colon at the end of a line is how you tell Python you are going to create a new "block" of code, and then indenting four spaces tells Python what lines of code are in that block.
-	Lists------ weights = [1, 2, 3, 4]
-	For-loop
-	obj -- 添加到列表末尾的对象。
-	range() function only does numbers from the first to the last, not including the last.
-	While – loop
-	While true ---- infinite loop
-	STAT 604, STAT 608, STAT 630.

### 9/2
-	Every if-statement must have an else..
-	Never nest if-statements more than two deep and always try to do them one deep.
-	Assert-you're telling the program to test that condition, and trigger an error if the condition is false.
-	Class，except, exec, lamba, pass, with…as…, yield…
-	Continue---Don't process more of the loop, do it again. 跳出此次循环，继续循环。

### 9/3
-	机器学习中决策树方法是对一系列需要验证的属性采取树状结构的方案去测试，以此来预测结果。
具体方法：简单的来说是通过最高的信息收益（information gain）寻找到应该最先测试的属性去测试，然后一直重复。
-	如果所有的结果一致，则所有分支回到同一节点，得到“预测为唯一结果“。
-	如果所有输入一致，则只有一个节点，得到“预测大多数结果。“
-	一般情况，找到具有最高信息收益的属性，假设其有n个元数，创建n个子代。
-	重复上一步骤直到不可分割。不可分割的情况有，所有 1）在这个子集里结果一致，2）在这个子集里，各个属性集合里数据的数目一致。
-	在所有节点都无法分割后，需要去修建分支，修建的依据是有多种，可以是卡方检验。

### 9/4
-	dict.get(key, default=None)
key -- 字典中要查找的键。
default -- 如果指定键的值不存在时，返回该默认值值。
-	the following values are interpreted as false: False, None, numeric zero of all types, and empty strings and containers (including strings, tuples, lists, dictionaries, sets and frozensets). All other values are interpreted as true. (See the `__nonzero__()` special method for a way to change this.)
### 9/5
Data 103学会了markdown，贝叶斯公式，google ngram
### 9/6
-	Class: tell python to make a new type of thing.
-	Object: two meanings: the most basic type of thing; and any instance of some thing.
-	Instance: What you get when you tell Python to create class
-	Def: How you define a function inside a class.
-	Self: inside the functions in a class, self is a variable for the instance/object being accessed.
-	Inheritance: The concept that one class can inherit traits from another class, much like you and your parents.
-	Composition: The concept that a class can be composed of other classes as parts, much like how a car has wheels.
-	Attribute: A property class have that are from composition and are usually variables.
-	Is-a: A phrase to say that something inherits from another, as in a ”salmon” is-a “fish”.
-	Has-a: A phrase to say that something is composed of other things or has a trait, as in “a salmon has-a mouth.”
-	Class X(Y): make a class named X that is-a Y.
-	Class X(object):def `__init__`(self, J): class X has-a` __init__ `that takes self and J parameters.
-	Class X(object): def M(self, J): class X has-a function named M that takes self and J parameters.
-	foo = X(): Set foo to an instance of class X
-	foo.M(J): from foo get the M function, and call it with parameters self, J.
-	foo.K = Q :from foo get the K attribute and set it to Q
-	range(a, b): a<=…<b
-	result = sentence[:] ? result = sentence

### 9/7

- [x] `__init__ & self` ?

### 9/8
data103
### 9/9
break
### 9/10
- data103
- pocedure of ex43
- inheritance
  - actions on the child imply an action on the parent.

    if you put functions in a base class then all subclasses will automatically get those features.

  - actions on the child override the action on the parent.
  - actions on the child alter the action on the parent.
- multiple inheritance
- `super()` with `__init__`
- Composition
- Avoid multiple inheritance at all costs, as it's too complex to be reliable. If you're stuck with it, then be prepared to know the class hierarchy and spend time finding where everything is coming from.
- Use composition to package code into modules that are used in many different unrelated places and situations.
- Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept or if you have to because of something you're using.
