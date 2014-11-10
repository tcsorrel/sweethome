# SweetHome
Dotfiles for Python coding with Vim, Xterm and Qtile

## Installation

* Clone the repository into your home directory
```
git clone --recursive https://github.com/tcsorrel/sweethome.git ~
```

* Include the gitconfig file in your `~/.gitconfig`:
```
[user]
    name = Your Name
    email = your.name@email.example
...
[include]
    path = ~/.gitconfig.sweethome
```
The .gitconfig `[include]` syntax requires Git 1.7.10+.
