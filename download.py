#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyautogui as pa
import time
import os
import csv

#set these positions manually using mouse.py
click_search_id = (1440,120)
click_id_listed_below = (1328,271)
click_extensions = (1771,63)
click_media_downloader = (1504,270)
click_bulk_download =(1241,632)
#the positions below may change during initial run so you can set two sets of positions in case they changes
#_1
#click_since_date =(657,324)
#click_until_date = (967,324)
#click_image = (602,385)
#click_start = (1226,416)
#_2
click_since_date =(655,288)
click_until_date = (967,288)
click_image = (602,349)
click_start = (1228,380)
click_refresh_page = (106,65)

#simulate mouse click
def click(position) :
	x = position[0]
	y = position[1]
	pa.click(x,y)

#simulate keyboard input
def keyboard(string) :
	pa.typewrite(string)

def start_download(usr_id,since_date,until_date) :
	click(click_refresh_page)
	time.sleep(10)
	click(click_search_id)
	time.sleep(0.1)
	keyboard(usr_id)#type usr id
	time.sleep(4)
	click(click_id_listed_below)
	time.sleep(5)
	click(click_extensions)
	time.sleep(1)
	click(click_media_downloader)
	time.sleep(2)
	click(click_bulk_download)
	time.sleep(1)
	click(click_image)
	time.sleep(0.5)
	click(click_since_date)
	time.sleep(0.1)
	keyboard(since_date)#type since date
	time.sleep(0.1)
	keyboard(["enter"])
	time.sleep(0.1)
	click(click_until_date)
	time.sleep(0.1)
	keyboard(until_date)#type until date
	time.sleep(0.1)
	keyboard(["enter"])
	time.sleep(0.1)
	click(click_start)

def detect_appearance_of_new_zip_file(usr_id) :
	x = 0
	for element in os.listdir(r"C:\Users\***\Downloads") :#set your broswer download path here
		if(usr_id in element):
			x = x + 1
	return x

def read_list(path) :
	with open(path,'r') as list:
		reader = csv.reader(list)
		account_infos = [row for row in reader]
	for account_info in account_infos :
		del account_info[0]
	del account_infos[0]
	return account_infos

def download(usr_infos,until):
	time.sleep(10)
	for usr_info in usr_infos :
		usr_id = usr_info[0]
		sincee = usr_info[1]
		since = sincee + "/01/01"
		ur_id = usr_id.replace("@","")
		if(usr_id == ""):
			print("user id not listed, progress stop...")
			break
		print("bulk downloading " + usr_id)
		start_download(usr_id,since,until)
		time.sleep(30)
		while detect_appearance_of_new_zip_file(ur_id) == 0 :
			time.sleep(10)
			continue

if __name__ == "__main__":
	path = r"C:\Users\***\Desktop\usrs.csv"#set your csv flie path here
	until = "2022/06/01"#set the until date here
	usr_info = read_list(path)
	download(usr_info,until)

		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
