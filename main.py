import telebot
import random
import os
import logging
import psycopg2
from flask import Flask,request
from telebot import types
from aiogram import types
import re

app_url='https://myfirstbotnik.herokuapp.com/'+'5553206056:AAE7ElBXf-Qavo8JoXWnkzt4zj_qZ-2k1uc'
bot=telebot.TeleBot('5553206056:AAE7ElBXf-Qavo8JoXWnkzt4zj_qZ-2k1uc')
server=Flask(__name__)
logger=telebot.logger
logger.setLevel(logging.DEBUG)

db_connection = psycopg2.connect('postgres://gdsumpjrfacirz:f0652f5a5486e15f811e495dcee6c081500f1581a1dff155dd318544f46458a9@ec2-99-80-170-190.eu-west-1.compute.amazonaws.com:5432/d3p6fgvaocq6mb',sslmode="require")
db_object =db_connection.cursor()

@bot.message_handler(commands=['start'])
def start(massage):
    bot.send_message(massage.chat.id,'Привет')
    bot.send_message(massage.chat.id, 'Что же из себя представляет данный бот?')
    bot.send_message(massage.chat.id,'Это карточная игра 21 в которую на данный момент ты можешь поиграть только с диллером, но в скором времени будут допилен функционал для игры с друзьями, монеты за победы и турнирные сетки с призами для победителей!')
    bot.send_message(massage.chat.id, 'Если хочешь узнать что я могу, напиши /help')
    id=massage.from_user.id
    db_object.execute(f"SELECT id FROM users WHERE id = {id}")
    result = db_object.fetchone()
    if not result:
        db_object.execute(f"INSERT INTO  users(id,username,mssages) VALUES(%s,%s,%s)", (id,username,0))
        db_connection.commit()


@bot.message_handler(commands=['help'])
def help(message):
    markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    markup.row('/start_game')
    markup.row('/all_commands')
    bot.send_message(message.chat.id,'Выберите кнопку', reply_markup=markup)
@bot.message_handler(commands =['all_commands'])
def all_commands(message):
    bot.send_message(message.chat.id, 'Пока у меня только /start, /help, /start_game, /Get_another_card, /Stop, /all_commands, /register')
    bot.send_message(message.chat.id,'Но использовать /Get_another_card, /Stop, можно только после /start_game')
global k
k=4
@bot.message_handler(commands =['spent','s','earend','e'], commands_prefix = '!/')
def take_money(message):
    cmd_variants=(('/spent','/s','!spent','!s'),('/earend','/e','!earend','!e'))
    operation = '-' if message.text.startwith(cmd_variants[0]) else '+'
    value = message.text
    for i in cmd_variants:
        for j in i:
            value=value.replase(j,'').strip()
    if len(value):
        x=re.findall(r'\d+(?:.\d+)?',value)
        if len(x):
            value=float(x[0].replace(',','.'))
            bot.send_message(message.chat.id,value)
        else:
            bot.send_message(message.chat.id, 'Не удалось определить сумму')
    else:
        bot.send_message(message.chat.id,'Не введено значение')

@bot.message_handler(commands =['start_game'])
def start_game(message):
    global mas, sum_dil, sum_pol, flag_dil, flag_pol
    mas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]
    random.shuffle(mas)
    sum_dil, sum_pol = 0, 0
    flag_dil, flag_pol = 0, 0
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.row('/Get_another_card')
    markup.row('/Stop')
    markup.row('/all_commands')
    bot.send_message(message.chat.id,'Выберите кнопку', reply_markup=markup)
    prov = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
    for i in range(len(prov)):
        if mas[2]== prov[i]:
            if i==0:
                second_card_dil= open('два пики.jpg','rb')
                sum_dil+=2
            elif i==1:
                second_card_dil= open('два черви.jpg','rb')
                sum_dil += 2
            elif i==2:
                second_card_dil= open('два крести.jpg','rb')
                sum_dil += 2
            elif i==3:
                second_card_dil= open('два буби.jpg','rb')
                sum_dil += 2
            elif i==4:
                second_card_dil= open('три пики.jpg','rb')
                sum_dil += 3
            elif i==5:
                second_card_dil= open('три черви.jpg','rb')
                sum_dil += 3
            elif i==6:
                second_card_dil= open('три крести.jpg','rb')
                sum_dil += 3
            elif i==7:
                second_card_dil= open('три буби.jpg','rb')
                sum_dil += 3
            elif i==8:
                second_card_dil= open('четыре пики.jpg','rb')
                sum_dil += 4
            elif i==9:
                second_card_dil= open('четыре черви.jpg','rb')
                sum_dil += 4
            elif i==10:
                second_card_dil= open('четыре крести.jpg','rb')
                sum_dil += 4
            elif i==11:
                second_card_dil= open('четыре буби.jpg','rb')
                sum_dil += 4
            elif i==12:
                second_card_dil= open('пять пики.jpg','rb')
                sum_dil += 5
            elif i==13:
                second_card_dil= open('пять черви.jpg','rb')
                sum_dil += 5
            elif i==14:
                second_card_dil= open('пять крести.jpg','rb')
                sum_dil += 5
            elif i==15:
                second_card_dil= open('пять буби.jpg','rb')
                sum_dil += 5
            elif i==16:
                second_card_dil= open('шесть пики.jpg','rb')
                sum_dil += 6
            elif i==17:
                second_card_dil= open('шесть черви.jpg','rb')
                sum_dil += 6
            elif i==18:
                second_card_dil= open('шесть крести.jpg','rb')
                sum_dil += 6
            elif i==19:
                second_card_dil= open('шесть буби.jpg','rb')
                sum_dil += 6
            elif i==20:
                second_card_dil= open('семь пики.jpg','rb')
                sum_dil += 7
            elif i==21:
                second_card_dil= open('семь черви.jpg','rb')
                sum_dil += 7
            elif i==22:
                second_card_dil= open('семь крести.jpg','rb')
                sum_dil += 7
            elif i==23:
                second_card_dil= open('семь буби.jpg','rb')
                sum_dil += 7
            elif i==24:
                second_card_dil= open('восемь пики.jpg','rb')
                sum_dil += 8
            elif i==25:
                second_card_dil= open('восем черви.jpg','rb')
                sum_dil += 8
            elif i==26:
                second_card_dil= open('восемь крести.jpg','rb')
                sum_dil += 8
            elif i==27:
                second_card_dil= open('восемь буби.jpg','rb')
                sum_dil += 8
            elif i==28:
                second_card_dil= open('девять пики.jpg','rb')
                sum_dil += 9
            elif i==29:
                second_card_dil= open('девять черви.jpg','rb')
                sum_dil += 9
            elif i==30:
                second_card_dil= open('девять крести.jpg','rb')
                sum_dil += 9
            elif i==31:
                second_card_dil= open('девять буби.jpg','rb')
                sum_dil += 9
            elif i==32:
                second_card_dil= open('десять пики.jpg','rb')
                sum_dil += 10
            elif i==33:
                second_card_dil= open('десять черви.jpg','rb')
                sum_dil += 10
            elif i==34:
                second_card_dil= open('десять крести.jpg','rb')
                sum_dil += 10
            elif i==35:
                second_card_dil= open('десять буби.jpg','rb')
                sum_dil += 10
            elif i==36:
                second_card_dil= open('валет пики.jpg','rb')
                sum_dil += 10
            elif i==37:
                second_card_dil= open('валет черви.jpg','rb')
                sum_dil += 10
            elif i==38:
                second_card_dil= open('валет крести.jpg','rb')
                sum_dil += 10
            elif i==39:
                second_card_dil= open('валет буби.jpg','rb')
                sum_dil += 10
            elif i==40:
                second_card_dil= open('дама пики.jpg','rb')
                sum_dil += 10
            elif i==41:
                second_card_dil= open('дама черви.jpg','rb')
                sum_dil += 10
            elif i==42:
                second_card_dil= open('дама крести.jpg','rb')
                sum_dil += 10
            elif i==43:
                second_card_dil= open('дама буби.jpg','rb')
                sum_dil += 10
            elif i==44:
                second_card_dil= open('король пики.jpg','rb')
                sum_dil += 10
            elif i==45:
                second_card_dil= open('король черви.jpg','rb')
                sum_dil += 10
            elif i==46:
                second_card_dil= open('король крести.jpg','rb')
                sum_dil += 10
            elif i==47:
                second_card_dil= open('король буби.jpg','rb')
                sum_dil += 10
            elif i==48:
                second_card_dil= open('туз пики.jpg','rb')
                sum_dil += 11
                flag_dil+=1
            elif i==49:
                second_card_dil= open('туз черви.jpg','rb')
                sum_dil += 11
                flag_dil += 1
            elif i==50:
                second_card_dil= open('туз крести.jpg','rb')
                sum_dil += 11
                flag_dil += 1
            elif i==51:
                second_card_dil= open('туз буби.jpg','rb')
                sum_dil += 11
                flag_dil += 1
        if mas[3] == prov[i]:
            if i == 0:
                second_card_pol = open('два пики.jpg', 'rb')
                sum_pol+=2
            elif i == 1:
                second_card_pol = open('два черви.jpg', 'rb')
                sum_pol += 2
            elif i == 2:
                second_card_pol = open('два крести.jpg', 'rb')
                sum_pol += 2
            elif i == 3:
                second_card_pol = open('два буби.jpg', 'rb')
                sum_pol += 2
            elif i == 4:
                second_card_pol = open('три пики.jpg', 'rb')
                sum_pol += 3
            elif i == 5:
                second_card_pol = open('три черви.jpg', 'rb')
                sum_pol += 3
            elif i == 6:
                second_card_pol = open('три крести.jpg', 'rb')
                sum_pol += 3
            elif i == 7:
                second_card_pol = open('три буби.jpg', 'rb')
                sum_pol += 3
            elif i == 8:
                second_card_pol = open('четыре пики.jpg', 'rb')
                sum_pol += 4
            elif i == 9:
                second_card_pol = open('четыре черви.jpg', 'rb')
                sum_pol += 4
            elif i == 10:
                second_card_pol = open('четыре крести.jpg', 'rb')
                sum_pol += 4
            elif i == 11:
                second_card_pol = open('четыре буби.jpg', 'rb')
                sum_pol += 4
            elif i == 12:
                second_card_pol = open('пять пики.jpg', 'rb')
                sum_pol += 5
            elif i == 13:
                second_card_pol = open('пять черви.jpg', 'rb')
                sum_pol += 5
            elif i == 14:
                second_card_pol = open('пять крести.jpg', 'rb')
                sum_pol += 5
            elif i == 15:
                second_card_pol = open('пять буби.jpg', 'rb')
                sum_pol += 5
            elif i == 16:
                second_card_pol = open('шесть пики.jpg', 'rb')
                sum_pol += 6
            elif i == 17:
                second_card_pol = open('шесть черви.jpg', 'rb')
                sum_pol += 6
            elif i == 18:
                second_card_pol = open('шесть крести.jpg', 'rb')
                sum_pol += 6
            elif i == 19:
                second_card_pol = open('шесть буби.jpg', 'rb')
                sum_pol += 6
            elif i == 20:
                second_card_pol = open('семь пики.jpg', 'rb')
                sum_pol += 7
            elif i == 21:
                second_card_pol = open('семь черви.jpg', 'rb')
                sum_pol += 7
            elif i == 22:
                second_card_pol = open('семь крести.jpg', 'rb')
                sum_pol += 7
            elif i == 23:
                second_card_pol = open('семь буби.jpg', 'rb')
                sum_pol += 7
            elif i == 24:
                second_card_pol = open('восемь пики.jpg', 'rb')
                sum_pol += 8
            elif i == 25:
                second_card_pol = open('восем черви.jpg', 'rb')
                sum_pol += 8
            elif i == 26:
                second_card_pol = open('восемь крести.jpg', 'rb')
                sum_pol += 8
            elif i == 27:
                second_card_pol = open('восемь буби.jpg', 'rb')
                sum_pol += 8
            elif i == 28:
                second_card_pol = open('девять пики.jpg', 'rb')
                sum_pol += 9
            elif i == 29:
                second_card_pol = open('девять черви.jpg', 'rb')
                sum_pol += 9
            elif i == 30:
                second_card_pol = open('девять крести.jpg', 'rb')
                sum_pol += 9
            elif i == 31:
                second_card_pol = open('девять буби.jpg', 'rb')
                sum_pol += 9
            elif i == 32:
                second_card_pol = open('десять пики.jpg', 'rb')
                sum_pol += 10
            elif i == 33:
                second_card_pol = open('десять черви.jpg', 'rb')
                sum_pol += 10
            elif i == 34:
                second_card_pol = open('десять крести.jpg', 'rb')
                sum_pol += 10
            elif i == 35:
                second_card_pol = open('десять буби.jpg', 'rb')
                sum_pol += 10
            elif i == 36:
                second_card_pol = open('валет пики.jpg', 'rb')
                sum_pol += 10
            elif i == 37:
                second_card_pol = open('валет черви.jpg', 'rb')
                sum_pol += 10
            elif i == 38:
                second_card_pol = open('валет крести.jpg', 'rb')
                sum_pol += 10
            elif i == 39:
                second_card_pol = open('валет буби.jpg', 'rb')
                sum_pol += 10
            elif i == 40:
                second_card_pol = open('дама пики.jpg', 'rb')
                sum_pol += 10
            elif i == 41:
                second_card_pol = open('дама черви.jpg', 'rb')
                sum_pol += 10
            elif i == 42:
                second_card_pol = open('дама крести.jpg', 'rb')
                sum_pol += 10
            elif i == 43:
                second_card_pol = open('дама буби.jpg', 'rb')
                sum_pol += 10
            elif i == 44:
                second_card_pol = open('король пики.jpg', 'rb')
                sum_pol += 10
            elif i == 45:
                second_card_pol = open('король черви.jpg', 'rb')
                sum_pol += 10
            elif i == 46:
                second_card_pol = open('король крести.jpg', 'rb')
                sum_pol += 10
            elif i == 47:
                second_card_pol = open('король буби.jpg', 'rb')
                sum_pol += 10
            elif i == 48:
                second_card_pol = open('туз пики.jpg', 'rb')
                sum_pol += 11
                flag_pol += 1
            elif i == 49:
                second_card_pol = open('туз черви.jpg', 'rb')
                sum_pol += 11
                flag_pol += 1
            elif i == 50:
                second_card_pol = open('туз крести.jpg', 'rb')
                sum_pol += 11
                flag_pol += 1
            elif i == 51:
                second_card_pol = open('туз буби.jpg', 'rb')
                sum_pol += 11
                flag_pol += 1
        if mas[1] == prov[i]:
            if i == 0:
                first_card_pol = open('два пики.jpg', 'rb')
                sum_pol += 2
            elif i == 1:
                first_card_pol = open('два черви.jpg', 'rb')
                sum_pol += 2
            elif i == 2:
                first_card_pol = open('два крести.jpg', 'rb')
                sum_pol += 2
            elif i == 3:
                first_card_pol = open('два буби.jpg', 'rb')
                sum_pol += 2
            elif i == 4:
                first_card_pol = open('три пики.jpg', 'rb')
                sum_pol += 3
            elif i == 5:
                first_card_pol = open('три черви.jpg', 'rb')
                sum_pol += 3
            elif i == 6:
                first_card_pol = open('три крести.jpg', 'rb')
                sum_pol += 3
            elif i == 7:
                first_card_pol = open('три буби.jpg', 'rb')
                sum_pol += 3
            elif i == 8:
                first_card_pol = open('четыре пики.jpg', 'rb')
                sum_pol += 4
            elif i == 9:
                first_card_pol = open('четыре черви.jpg', 'rb')
                sum_pol += 4
            elif i == 10:
                first_card_pol = open('четыре крести.jpg', 'rb')
                sum_pol += 4
            elif i == 11:
                first_card_pol = open('четыре буби.jpg', 'rb')
                sum_pol += 4
            elif i == 12:
                first_card_pol = open('пять пики.jpg', 'rb')
                sum_pol += 5
            elif i == 13:
                first_card_pol = open('пять черви.jpg', 'rb')
                sum_pol += 5
            elif i == 14:
                first_card_pol = open('пять крести.jpg', 'rb')
                sum_pol += 5
            elif i == 15:
                first_card_pol = open('пять буби.jpg', 'rb')
                sum_pol += 5
            elif i == 16:
                first_card_pol = open('шесть пики.jpg', 'rb')
                sum_pol += 6
            elif i == 17:
                first_card_pol = open('шесть черви.jpg', 'rb')
                sum_pol += 6
            elif i == 18:
                first_card_pol = open('шесть крести.jpg', 'rb')
                sum_pol += 6
            elif i == 19:
                first_card_pol = open('шесть буби.jpg', 'rb')
                sum_pol += 6
            elif i == 20:
                first_card_pol = open('семь пики.jpg', 'rb')
                sum_pol += 7
            elif i == 21:
                first_card_pol = open('семь черви.jpg', 'rb')
                sum_pol += 7
            elif i == 22:
                first_card_pol = open('семь крести.jpg', 'rb')
                sum_pol += 7
            elif i == 23:
                first_card_pol = open('семь буби.jpg', 'rb')
                sum_pol += 7
            elif i == 24:
                first_card_pol = open('восемь пики.jpg', 'rb')
                sum_pol += 8
            elif i == 25:
                first_card_pol = open('восем черви.jpg', 'rb')
                sum_pol += 8
            elif i == 26:
                first_card_pol = open('восемь крести.jpg', 'rb')
                sum_pol += 8
            elif i == 27:
                first_card_pol = open('восемь буби.jpg', 'rb')
                sum_pol += 8
            elif i == 28:
                first_card_pol = open('девять пики.jpg', 'rb')
                sum_pol += 9
            elif i == 29:
                first_card_pol = open('девять черви.jpg', 'rb')
                sum_pol += 9
            elif i == 30:
                first_card_pol = open('девять крести.jpg', 'rb')
                sum_pol += 9
            elif i == 31:
                first_card_pol = open('девять буби.jpg', 'rb')
                sum_pol += 9
            elif i == 32:
                first_card_pol = open('десять пики.jpg', 'rb')
                sum_pol += 10
            elif i == 33:
                first_card_pol = open('десять черви.jpg', 'rb')
                sum_pol += 10
            elif i == 34:
                first_card_pol = open('десять крести.jpg', 'rb')
                sum_pol += 10
            elif i == 35:
                first_card_pol = open('десять буби.jpg', 'rb')
                sum_pol += 10
            elif i == 36:
                first_card_pol = open('валет пики.jpg', 'rb')
                sum_pol += 10
            elif i == 37:
                first_card_pol = open('валет черви.jpg', 'rb')
                sum_pol += 10
            elif i == 38:
                first_card_pol = open('валет крести.jpg', 'rb')
                sum_pol += 10
            elif i == 39:
                first_card_pol = open('валет буби.jpg', 'rb')
                sum_pol += 10
            elif i == 40:
                first_card_pol = open('дама пики.jpg', 'rb')
                sum_pol += 10
            elif i == 41:
                first_card_pol = open('дама черви.jpg', 'rb')
                sum_pol += 10
            elif i == 42:
                first_card_pol = open('дама крести.jpg', 'rb')
                sum_pol += 10
            elif i == 43:
                first_card_pol = open('дама буби.jpg', 'rb')
                sum_pol += 10
            elif i == 44:
                first_card_pol = open('король пики.jpg', 'rb')
                sum_pol += 10
            elif i == 45:
                first_card_pol = open('король черви.jpg', 'rb')
                sum_pol += 10
            elif i == 46:
                first_card_pol = open('король крести.jpg', 'rb')
                sum_pol += 10
            elif i == 47:
                first_card_pol = open('король буби.jpg', 'rb')
                sum_pol += 10
            elif i == 48:
                first_card_pol = open('туз пики.jpg', 'rb')
                sum_pol += 11
                flag_dil += 1
            elif i == 49:
                first_card_pol = open('туз черви.jpg', 'rb')
                sum_pol += 11
                flag_dil += 1
            elif i == 50:
                first_card_pol = open('туз крести.jpg', 'rb')
                sum_pol += 11
                flag_dil += 1
            elif i == 51:
                first_card_pol = open('туз буби.jpg', 'rb')
                sum_pol += 11
                flag_dil += 1
        if mas[0] == prov[i]:
            if i == 0:
                first_card_dil = open('два пики.jpg', 'rb')
                sum_dil += 2
            elif i == 1:
                first_card_dil = open('два черви.jpg', 'rb')
                sum_dil += 2
            elif i == 2:
                first_card_dil = open('два крести.jpg', 'rb')
                sum_dil += 2
            elif i == 3:
                first_card_dil = open('два буби.jpg', 'rb')
                sum_dil += 2
            elif i == 4:
                first_card_dil = open('три пики.jpg', 'rb')
                sum_dil += 3
            elif i == 5:
                first_card_dil = open('три черви.jpg', 'rb')
                sum_dil += 3
            elif i == 6:
                first_card_dil = open('три крести.jpg', 'rb')
                sum_dil += 3
            elif i == 7:
                first_card_dil = open('три буби.jpg', 'rb')
                sum_dil += 3
            elif i == 8:
                first_card_dil = open('четыре пики.jpg', 'rb')
                sum_dil += 4
            elif i == 9:
                first_card_dil = open('четыре черви.jpg', 'rb')
                sum_dil += 4
            elif i == 10:
                first_card_dil = open('четыре крести.jpg', 'rb')
                sum_dil += 4
            elif i == 11:
                first_card_dil = open('четыре буби.jpg', 'rb')
                sum_dil += 4
            elif i == 12:
                first_card_dil = open('пять пики.jpg', 'rb')
                sum_dil += 5
            elif i == 13:
                first_card_dil = open('пять черви.jpg', 'rb')
                sum_dil += 5
            elif i == 14:
                first_card_dil = open('пять крести.jpg', 'rb')
                sum_dil += 5
            elif i == 15:
                first_card_dil = open('пять буби.jpg', 'rb')
                sum_dil += 5
            elif i == 16:
                first_card_dil = open('шесть пики.jpg', 'rb')
                sum_dil += 6
            elif i == 17:
                first_card_dil = open('шесть черви.jpg', 'rb')
                sum_dil += 6
            elif i == 18:
                first_card_dil = open('шесть крести.jpg', 'rb')
                sum_dil += 6
            elif i == 19:
                first_card_dil = open('шесть буби.jpg', 'rb')
                sum_dil += 6
            elif i == 20:
                first_card_dil = open('семь пики.jpg', 'rb')
                sum_dil += 7
            elif i == 21:
                first_card_dil = open('семь черви.jpg', 'rb')
                sum_dil += 7
            elif i == 22:
                first_card_dil = open('семь крести.jpg', 'rb')
                sum_dil += 7
            elif i == 23:
                first_card_dil = open('семь буби.jpg', 'rb')
                sum_dil += 7
            elif i == 24:
                first_card_dil = open('восемь пики.jpg', 'rb')
                sum_dil += 8
            elif i == 25:
                first_card_dil = open('восем черви.jpg', 'rb')
                sum_dil += 8
            elif i == 26:
                first_card_dil = open('восемь крести.jpg', 'rb')
                sum_dil += 8
            elif i == 27:
                first_card_dil = open('восемь буби.jpg', 'rb')
                sum_dil += 8
            elif i == 28:
                first_card_dil = open('девять пики.jpg', 'rb')
                sum_dil += 9
            elif i == 29:
                first_card_dil = open('девять черви.jpg', 'rb')
                sum_dil += 9
            elif i == 30:
                first_card_dil = open('девять крести.jpg', 'rb')
                sum_dil += 9
            elif i == 31:
                first_card_dil = open('девять буби.jpg', 'rb')
                sum_dil += 9
            elif i == 32:
                first_card_dil = open('десять пики.jpg', 'rb')
                sum_dil += 10
            elif i == 33:
                first_card_dil = open('десять черви.jpg', 'rb')
                sum_dil += 10
            elif i == 34:
                first_card_dil = open('десять крести.jpg', 'rb')
                sum_dil += 10
            elif i == 35:
                first_card_dil = open('десять буби.jpg', 'rb')
                sum_dil += 10
            elif i == 36:
                first_card_dil = open('валет пики.jpg', 'rb')
                sum_dil += 10
            elif i == 37:
                first_card_dil = open('валет черви.jpg', 'rb')
                sum_dil += 10
            elif i == 38:
                first_card_dil = open('валет крести.jpg', 'rb')
                sum_dil += 10
            elif i == 39:
                first_card_dil = open('валет буби.jpg', 'rb')
                sum_dil += 10
            elif i == 40:
                first_card_dil = open('дама пики.jpg', 'rb')
                sum_dil += 10
            elif i == 41:
                first_card_dil = open('дама черви.jpg', 'rb')
                sum_dil += 10
            elif i == 42:
                first_card_dil = open('дама крести.jpg', 'rb')
                sum_dil += 10
            elif i == 43:
                first_card_dil = open('дама буби.jpg', 'rb')
                sum_dil += 10
            elif i == 44:
                first_card_dil = open('король пики.jpg', 'rb')
                sum_dil += 10
            elif i == 45:
                first_card_dil = open('король черви.jpg', 'rb')
                sum_dil += 10
            elif i == 46:
                first_card_dil = open('король крести.jpg', 'rb')
                sum_dil += 10
            elif i == 47:
                first_card_dil = open('король буби.jpg', 'rb')
                sum_dil += 10
            elif i == 48:
                first_card_dil = open('туз пики.jpg', 'rb')
                sum_dil += 11
                flag_pol += 1
            elif i == 49:
                first_card_dil = open('туз черви.jpg', 'rb')
                sum_dil += 11
                flag_pol += 1
            elif i == 50:
                first_card_dil = open('туз крести.jpg', 'rb')
                sum_dil += 11
                flag_pol += 1
            elif i == 51:
                first_card_dil = open('туз буби.jpg', 'rb')
                sum_dil += 11
                flag_pol += 1
    bot.send_message(message.chat.id, 'Карты диллера')
    bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(first_card_dil), telebot.types.InputMediaPhoto(second_card_dil)])
    bot.send_message(message.chat.id, f'У диллера{sum_dil}')
    bot.send_message(message.chat.id, 'Ваши карты')
    bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(first_card_pol), telebot.types.InputMediaPhoto(second_card_pol)])
    bot.send_message(message.chat.id, f'У вас{sum_pol}')


@bot.message_handler(commands=['Get_another_card'])
def Get_another_card(message):
    global sum_dil, sum_pol, flag_dil, flag_pol,k
    prov = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]
    for i in range(len(prov)):
        if mas[k]== prov[i]:
            if i == 0:
                next_card = open('два пики.jpg', 'rb')
                sum_pol += 2
            elif i == 1:
                next_card = open('два черви.jpg', 'rb')
                sum_pol += 2
            elif i == 2:
                next_card = open('два крести.jpg', 'rb')
                sum_pol += 2
            elif i == 3:
                next_card = open('два буби.jpg', 'rb')
                sum_pol += 2
            elif i == 4:
                next_card = open('три пики.jpg', 'rb')
                sum_pol += 3
            elif i == 5:
                next_card = open('три черви.jpg', 'rb')
                sum_pol += 3
            elif i == 6:
                next_card = open('три крести.jpg', 'rb')
                sum_pol += 3
            elif i == 7:
                next_card = open('три буби.jpg', 'rb')
                sum_pol += 3
            elif i == 8:
                next_card = open('четыре пики.jpg', 'rb')
                sum_pol += 4
            elif i == 9:
                next_card = open('четыре черви.jpg', 'rb')
                sum_pol += 4
            elif i == 10:
                next_card = open('четыре крести.jpg', 'rb')
                sum_pol += 4
            elif i == 11:
                next_card = open('четыре буби.jpg', 'rb')
                sum_pol += 4
            elif i == 12:
                next_card = open('пять пики.jpg', 'rb')
                sum_pol += 5
            elif i == 13:
                next_card = open('пять черви.jpg', 'rb')
                sum_pol += 5
            elif i == 14:
                next_card = open('пять крести.jpg', 'rb')
                sum_pol += 5
            elif i == 15:
                next_card = open('пять буби.jpg', 'rb')
                sum_pol += 5
            elif i == 16:
                next_card = open('шесть пики.jpg', 'rb')
                sum_pol += 6
            elif i == 17:
                next_card = open('шесть черви.jpg', 'rb')
                sum_pol += 6
            elif i == 18:
                next_card = open('шесть крести.jpg', 'rb')
                sum_pol += 6
            elif i == 19:
                next_card = open('шесть буби.jpg', 'rb')
                sum_pol += 6
            elif i == 20:
                next_card = open('семь пики.jpg', 'rb')
                sum_pol += 7
            elif i == 21:
                next_card = open('семь черви.jpg', 'rb')
                sum_pol += 7
            elif i == 22:
                next_card = open('семь крести.jpg', 'rb')
                sum_pol += 7
            elif i == 23:
                next_card = open('семь буби.jpg', 'rb')
                sum_pol += 7
            elif i == 24:
                next_card = open('восемь пики.jpg', 'rb')
                sum_pol += 8
            elif i == 25:
                next_card = open('восем черви.jpg', 'rb')
                sum_pol += 8
            elif i == 26:
                next_card = open('восемь крести.jpg', 'rb')
                sum_pol += 8
            elif i == 27:
                next_card = open('восемь буби.jpg', 'rb')
                sum_pol += 8
            elif i == 28:
                next_card = open('девять пики.jpg', 'rb')
                sum_pol += 9
            elif i == 29:
                next_card = open('девять черви.jpg', 'rb')
                sum_pol += 9
            elif i == 30:
                next_card = open('девять крести.jpg', 'rb')
                sum_pol += 9
            elif i == 31:
                next_card = open('девять буби.jpg', 'rb')
                sum_pol += 9
            elif i == 32:
                next_card = open('десять пики.jpg', 'rb')
                sum_pol += 10
            elif i == 33:
                next_card = open('десять черви.jpg', 'rb')
                sum_pol += 10
            elif i == 34:
                next_card = open('десять крести.jpg', 'rb')
                sum_pol += 10
            elif i == 35:
                next_card = open('десять буби.jpg', 'rb')
                sum_pol += 10
            elif i == 36:
                next_card = open('валет пики.jpg', 'rb')
                sum_pol += 10
            elif i == 37:
                next_card = open('валет черви.jpg', 'rb')
                sum_pol += 10
            elif i == 38:
                next_card = open('валет крести.jpg', 'rb')
                sum_pol += 10
            elif i == 39:
                next_card = open('валет буби.jpg', 'rb')
                sum_pol += 10
            elif i == 40:
                next_card = open('дама пики.jpg', 'rb')
                sum_pol += 10
            elif i == 41:
                next_card = open('дама черви.jpg', 'rb')
                sum_pol += 10
            elif i == 42:
                next_card = open('дама крести.jpg', 'rb')
                sum_pol += 10
            elif i == 43:
                next_card = open('дама буби.jpg', 'rb')
                sum_pol += 10
            elif i == 44:
                next_card = open('король пики.jpg', 'rb')
                sum_pol += 10
            elif i == 45:
                next_card = open('король черви.jpg', 'rb')
                sum_pol += 10
            elif i == 46:
                next_card = open('король крести.jpg', 'rb')
                sum_pol += 10
            elif i == 47:
                next_card = open('король буби.jpg', 'rb')
                sum_pol += 10
            elif i == 48:
                next_card = open('туз пики.jpg', 'rb')
                sum_pol += 11
                flag_pol += 1
            elif i == 49:
                next_card = open('туз черви.jpg', 'rb')
                sum_pol += 11
                flag_pol += 1
            elif i == 50:
                next_card = open('туз крести.jpg', 'rb')
                sum_pol += 11
                flag_pol += 1
            elif i == 51:
                next_card = open('туз буби.jpg', 'rb')
                sum_pol += 11
                flag_pol += 1
    if sum_pol>21 and flag_pol==0:
        global g
        g=k
        bot.send_photo(message.chat.id,next_card)
        bot.send_message(message.chat.id, f'У вас {sum_pol}')
        bot.send_message(message.chat.id, 'Вы проиграли')
        help(message)
    elif sum_pol>21 and flag_pol>0:
        flag_pol-=1
        k += 1
        sum_pol-=10
        bot.send_photo(message.chat.id, next_card)
        bot.send_message(message.chat.id, f'У вас {sum_pol}')
    elif sum_pol <= 21:
        k += 1
        bot.send_photo(message.chat.id, next_card)
        bot.send_message(message.chat.id, f'У вас {sum_pol}')

@bot.message_handler(commands=['Stop'])
def Stop(message):
    global g
    g=k
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.row('/all_commands')
    bot.send_message(message.chat.id, 'Диллер берет карты')
    Get_another_card_dil(message)

@bot.message_handler(commands=['Get_another_card_dil'])
def Get_another_card_dil(message):
    global sum_dil, sum_pol, flag_dil, flag_pol,g,mas
    prov = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]
    if sum_dil<sum_pol:
        for i in range(len(prov)):
            if mas[g]== prov[i]:
                if i == 0:
                    next_card = open('два пики.jpg', 'rb')
                    sum_dil += 2
                elif i == 1:
                    next_card = open('два черви.jpg', 'rb')
                    sum_dil += 2
                elif i == 2:
                    next_card = open('два крести.jpg', 'rb')
                    sum_dil += 2
                elif i == 3:
                    next_card = open('два буби.jpg', 'rb')
                    sum_dil += 2
                elif i == 4:
                    next_card = open('три пики.jpg', 'rb')
                    sum_dil += 3
                elif i == 5:
                    next_card = open('три черви.jpg', 'rb')
                    sum_dil += 3
                elif i == 6:
                    next_card = open('три крести.jpg', 'rb')
                    sum_dil += 3
                elif i == 7:
                    next_card = open('три буби.jpg', 'rb')
                    sum_dil += 3
                elif i == 8:
                    next_card = open('четыре пики.jpg', 'rb')
                    sum_dil += 4
                elif i == 9:
                    next_card = open('четыре черви.jpg', 'rb')
                    sum_dil += 4
                elif i == 10:
                    next_card = open('четыре крести.jpg', 'rb')
                    sum_dil += 4
                elif i == 11:
                    next_card = open('четыре буби.jpg', 'rb')
                    sum_dil += 4
                elif i == 12:
                    next_card = open('пять пики.jpg', 'rb')
                    sum_dil += 5
                elif i == 13:
                    next_card = open('пять черви.jpg', 'rb')
                    sum_dil += 5
                elif i == 14:
                    next_card = open('пять крести.jpg', 'rb')
                    sum_dil += 5
                elif i == 15:
                    next_card = open('пять буби.jpg', 'rb')
                    sum_dil += 5
                elif i == 16:
                    next_card = open('шесть пики.jpg', 'rb')
                    sum_dil += 6
                elif i == 17:
                    next_card = open('шесть черви.jpg', 'rb')
                    sum_dil += 6
                elif i == 18:
                    next_card = open('шесть крести.jpg', 'rb')
                    sum_dil += 6
                elif i == 19:
                    next_card = open('шесть буби.jpg', 'rb')
                    sum_dil += 6
                elif i == 20:
                    next_card = open('семь пики.jpg', 'rb')
                    sum_dil += 7
                elif i == 21:
                    next_card = open('семь черви.jpg', 'rb')
                    sum_dil += 7
                elif i == 22:
                    next_card = open('семь крести.jpg', 'rb')
                    sum_dil += 7
                elif i == 23:
                    next_card = open('семь буби.jpg', 'rb')
                    sum_dil += 7
                elif i == 24:
                    next_card = open('восемь пики.jpg', 'rb')
                    sum_dil += 8
                elif i == 25:
                    next_card = open('восем черви.jpg', 'rb')
                    sum_dil += 8
                elif i == 26:
                    next_card = open('восемь крести.jpg', 'rb')
                    sum_dil += 8
                elif i == 27:
                    next_card = open('восемь буби.jpg', 'rb')
                    sum_dil += 8
                elif i == 28:
                    next_card = open('девять пики.jpg', 'rb')
                    sum_dil += 9
                elif i == 29:
                    next_card = open('девять черви.jpg', 'rb')
                    sum_dil += 9
                elif i == 30:
                    next_card = open('девять крести.jpg', 'rb')
                    sum_dil += 9
                elif i == 31:
                    next_card = open('девять буби.jpg', 'rb')
                    sum_dil += 9
                elif i == 32:
                    next_card = open('десять пики.jpg', 'rb')
                    sum_dil += 10
                elif i == 33:
                    next_card = open('десять черви.jpg', 'rb')
                    sum_dil += 10
                elif i == 34:
                    next_card = open('десять крести.jpg', 'rb')
                    sum_dil += 10
                elif i == 35:
                    next_card = open('десять буби.jpg', 'rb')
                    sum_dil += 10
                elif i == 36:
                    next_card = open('валет пики.jpg', 'rb')
                    sum_dil += 10
                elif i == 37:
                    next_card = open('валет черви.jpg', 'rb')
                    sum_dil += 10
                elif i == 38:
                    next_card = open('валет крести.jpg', 'rb')
                    sum_dil += 10
                elif i == 39:
                    next_card = open('валет буби.jpg', 'rb')
                    sum_dil += 10
                elif i == 40:
                    next_card = open('дама пики.jpg', 'rb')
                    sum_dil += 10
                elif i == 41:
                    next_card = open('дама черви.jpg', 'rb')
                    sum_dil += 10
                elif i == 42:
                    next_card = open('дама крести.jpg', 'rb')
                    sum_dil += 10
                elif i == 43:
                    next_card = open('дама буби.jpg', 'rb')
                    sum_dil += 10
                elif i == 44:
                    next_card = open('король пики.jpg', 'rb')
                    sum_dil += 10
                elif i == 45:
                    next_card = open('король черви.jpg', 'rb')
                    sum_dil += 10
                elif i == 46:
                    next_card = open('король крести.jpg', 'rb')
                    sum_dil += 10
                elif i == 47:
                    next_card = open('король буби.jpg', 'rb')
                    sum_dil += 10
                elif i == 48:
                    next_card = open('туз пики.jpg', 'rb')
                    sum_dil += 11
                    flag_dil += 1
                elif i == 49:
                    next_card = open('туз черви.jpg', 'rb')
                    sum_dil += 11
                    flag_dil += 1
                elif i == 50:
                    next_card = open('туз крести.jpg', 'rb')
                    sum_dil += 11
                    flag_dil += 1
                elif i == 51:
                    next_card = open('туз буби.jpg', 'rb')
                    sum_dil += 11
                    flag_dil += 1
        if sum_dil>21 and flag_dil==0:
            bot.send_photo(message.chat.id,next_card)
            bot.send_message(message.chat.id, f'У диллера {sum_dil}')
            bot.send_message(message.chat.id, 'Вы выйграли')
            help(message)
        elif sum_dil>21 and flag_dil>0:
            flag_pol-=1
            g += 1
            sum_dil-=10
            bot.send_photo(message.сhat.id, next_card)
            bot.send_message(message.chat.id, f'У диллера {sum_dil}')
            Get_another_card_dil(message)
        elif sum_dil <= 21:
            g += 1
            bot.send_photo(message.chat.id, next_card)
            bot.send_message(message.chat.id, f'У диллера {sum_dil}')
            Get_another_card_dil(message)
    elif sum_dil==sum_pol:
        bot.send_message(message.chat.id, 'Ничья')
        help(message)
    else:
        bot.send_message(message.chat.id, 'Вы проиграли')
        help(message)

bot.polling(none_stop=True)

@server.route("/5553206056:AAE7ElBXf-Qavo8JoXWnkzt4zj_qZ-2k1uc",methods=["POST"])
def redirect_massege():
    json_string=request.get_data().decode('utf-8')
    update =telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!',200
if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=app_url)
    server.run(host='0.0.0.0',port=int(os.environ.get('PORT',5000)))