---
layout: post
title: 'Fazendo o unity voltar a funcinoar para conta da minha mae'
---



Can someone affected by this please run

  gsettings get org.compiz.core:/org/compiz/profiles/unity/plugins/core/ active-plugins

  in a terminal and paste the output to this bug?

  Also please attach your ~/.xsession-errors file.

  Then try running

    gsettings reset org.compiz.core:/org/compiz/profiles/unity/plugins/core/ active-plugins

    and restarting/logging out and in to see if you get your session back.


fonte: https://bugs.launchpad.net/ubuntu/+source/compiz/+bug/1166765/comments/9




***************



Switch to tty1 using Ctrl+Alt+F1

Login to your user account

And export your Display with

export DISPLAY=:0

Add opengl to Compiz active plugins list

```
dconf write /org/compiz/profiles/unity/plugins/core/active-plugins "[`dconf read /org/compiz/profiles/unity/plugins/core/active-plugins | sed -r 's/(\[|\])//g'`, 'opengl']"
```

Or reset the key to default

```
dconf reset /org/compiz/profiles/unity/plugins/core/active-plugins
```

If it didn't work, come back and reset all Compiz settings to defaults

```
dconf reset -f /org/compiz/
```

Restart graphical display manager after one of the dconf command above

```
sudo service lightdm restart
```

Switch back to tty7 (X graphic display) Ctrl+Alt+F7

Try login again.
