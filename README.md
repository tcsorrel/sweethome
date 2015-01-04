# SweetHome
Configuration files for Python coding with Vim, Xterm, Git and Qtile
## Installation
* Clone the repository into your home directory
```
git clone --recursive https://github.com/tcsorrel/sweethome.git ~/sweethome
```
## Integration
Each part of sweethome may be integrated seperatly, depending on what is needed
### VIM
* Use sweethome's vimrc
```
ln -s ~/sweethome/vim/vimrc ~/.vimrc
```
### Git
* Include the gitconfig file in your `~/.gitconfig`:
```
[user]
    name = Your Name
    email = your.name@email.example
...
[include]
    path = ~/sweethome/git/config
```
The .gitconfig `[include]` syntax requires Git 1.7.10+.
### X resources
* Use sweethome's Xresources file to configure Xterm font and colors
```
ln -s ~/sweethome/x/resources ~/.Xresources
xrdb -merge ~/.Xresources
```
### Qtile configuration
* Use sweethome's configuration for Qtile window manager
```
ln -s ~/sweethome/qtile/config.py ~/.config/qtile/config.py
```
