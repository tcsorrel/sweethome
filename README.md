# SweetHome
Configuration files for Python coding with Vim, Xterm, Git and Qtile

## Installation
* Clone the repository into your home directory:
```bash
$ git clone --recursive https://github.com/tcsorrel/sweethome.git ~/sweethome
```

## Integration
Each part of sweethome may be integrated seperately,
depending on what is needed.

### NeoVIM
```bash
$ curl https://raw.githubusercontent.com/Shougo/dein.vim/master/bin/installer.sh > installer.sh
$ sh ./installer.sh ~/.cache/dein
$ ln -s ~/sweethome/vim/init.vim ~/.config/nvim/init.vim
$ vi "+call dein#install()" +qa
```

### Shell
* Load sweethome's shell functions in your `~/.bashrc` or `~/.bash_aliases`.
```bash
source ~/sweethome/sh/func.sh
```

### Git
* Include the gitconfig file in your `~/.gitconfig`:
```ini
[user]
    name = Your Name
    email = your.name@email.example
...
[include]
    path = ~/sweethome/git/config
```
The .gitconfig `[include]` syntax requires `git 1.7.10+`.

### Mercurial
* Include configuration files in your `~/.hgrc`:
```ini
[ui]
username = Your Name <your.name@email.example>
ignore = ~/sweethome/hg/ignore

%include ~/sweethome/hg/main

```

### X resources
* Use sweethome's Xresources file to configure Xterm font and colors:
GCC Precompiler need to be installed here
```bash
$ ln -s ~/sweethome/x/resources ~/.Xresources
$ xrdb -merge ~/.Xresources
```

### Qtile configuration
* Use sweethome's configuration for Qtile window manager:
```bash
$ ln -s ~/sweethome/qtile/config.py ~/.config/qtile/config.py
```
