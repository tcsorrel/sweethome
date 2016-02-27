# SweetHome
Configuration files for Python coding with Vim, Emacs, Xterm, Git and Qtile

## Installation
* Clone the repository into your home directory:
```bash
$ git clone --recursive https://github.com/tcsorrel/sweethome.git ~/sweethome
```

## Integration
Each part of sweethome may be integrated seperately,
depending on what is needed.

### VIM
* Use sweethome's vimrc and install plugins with
[Vundle](https://github.com/gmarik/Vundle.vim):
```bash
$ ln -s ~/sweethome/vim/vimrc ~/.vimrc
$ vim +PluginInstall +qa
```

### Emacs
* Include sweethome's configuration from your `~/.emacs`:
```lisp
(setq user-full-name "Sarah Connor")
(setq user-mail-address "<sarah@connor.org>")
(setq mail-self-address "Sarah Connor <sarah@connor.org>")

;; Ubuntu PPA hacks
;;(load-file ""~/sweethome/emacs/snapshot-ppa.el"")

;; main configuration
(load-file "~/sweethome/emacs/emacs.el")
```
Mode packaging requires `emacs 24.4+` or `package.el`.

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
```bash
$ ln -s ~/sweethome/x/resources ~/.Xresources
$ xrdb -merge ~/.Xresources
```

### Qtile configuration
* Use sweethome's configuration for Qtile window manager:
```bash
$ ln -s ~/sweethome/qtile/config.py ~/.config/qtile/config.py
```
