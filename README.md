# Python with TDD 

I use manjaro 

1. Requirements: 

1.1. Geckodriver for Firefox

~~~~
sudo pacman -S geckodriver   # in manjaro and arch like distro
~~~~

2. virtualenvwrapper 

~~~~
yaourt virtualenvwrapper
~~~~

3. git (and I use 'hub' it's cli tools complete git-cli) 

4. pyenv (help you use anything version python) 

2. Create enviroment 

Look like :
mkvirtualenv -p ~/path/to/pyenv/pythons name_enviroment 

Need python >= 3.6
~~~~~
mkvirtualenv -p ~/.pyenv/versions/3.6.5/bin/python superlists 
~~~~~

2.1 Djnago and Selenium

~~~~~
pip install django==1.11.3 "selenium==3.4.3
~~~~~

