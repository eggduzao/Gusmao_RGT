#!/bin/zsh

fList=( "./PWM/"* )
for fn in $fList
do
    python2.7 makeLogo.py 300 png $fn "./logo/"
done


