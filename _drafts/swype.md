---
layout: post
title: Swype no Android Keyboard (AOSP) no LineageOS 14.1
---

Ano passado comecei a usar o LineageOS no meu antigo celular
(Motorola Moto X 2013 - ver [2]).
Mas instalei parte do google junto com sistema operacional,
usando o opengapps.

Para conseguir fazer o Android Keyboard (AOSP) reconhecer gestos

certeza e uma duvida,
Quando coloquei (via adb) na pasta lib,
estava com as permissoes corretas
(ou talvez pq eu jah tenha ajustado anteriormente pelo Amaze File Explorer).

Duvida:
Serah que precisaria colocar na pasta lib tb?
chmod 644
baixei do opengapps

melhor usar o [1] q te ajuda a baixar a versao correta da lib
o [2] eh para zenfone2 e meio antigo
o [3] eh pq frisou a necessidade da permissao correta no arquivo

estranho eh q parece q funcionou por um tempo,
reparem no parece, pois eu estava com bastante sono nos primeiros dias

Talvez essa swypelib nao seja tao livre quanto o LAOS.

meu eh arm64

Referencias:
1 - https://android.stackexchange.com/questions/150439/enable-gesture-swipe-input-on-fairphone-2-without-google-keyboard
2 - clhio
3 - https://forum.xda-developers.com/zenfone2/general/tweak-fix-gesture-typing-aosp-keyboard-t3316337
4 - https://www.reddit.com/r/fossdroid/comments/6i92he/nogapps_android_nougat_and_swipe_gesture_typing/dqf68xk/
