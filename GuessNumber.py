{\rtf1\ansi\ansicpg1252\cocoartf1348\cocoasubrtf170
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl420

\f0\fs28 \cf0 \expnd0\expndtw0\kerning0
# number guess\
# 1.generate a random number\
import random\
num = random.randint(1,101)\
\
# 2. input the guess number & compare them\
guess = -1\
while guess != num:    \
    guess = int(input('Enter your guess number:'))\
    if guess == num:\
        print('Congratulations! You get the right number!')\
    elif guess < num:\
        print('Your guess number is too small')\
    else:\
        print('Your guess number is too large')}