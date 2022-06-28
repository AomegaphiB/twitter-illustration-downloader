# twitter illustration downloader based on twMediaDownloader

 This is a simple automation script for twitter media downloader from [furyutei](https://github.com/furyutei/twMediaDownloader).

 I use this script to bulk download the illustrations from some illustrators on Twitter.

 This script read a given list of users and download since date from a csv file and download the images from the timeline of all the users listed in the csv flie. 

 This script use keyboard&mouse simulation to input user names and sincedate/untildate and click start button if you use keyboard and mouse during progress the program may be interupted.

 The mouse click positions should be set manually, use the mouse.py script to determine the corresponding positions.

 Be aware that the positions will change during initial run then it will become stable after severel downloads.

 The format of the csv file is given in the usr.csv example.

 I am not familiar with Javascript now, next time I may write a more covenient version that achieves the same functionality in Javascript.

# Use

 install [twitter meida downloader](https://github.com/furyutei/twMediaDownloader) in your browser

 (I use chrome as the browser)

 install pyautogui

 `pip install pyautogui`

 open twitter page in the browser and click extensions

 run mouse.py and set the click positions manually in download.py 

 prepare csv file and set the path in download.py

 set the broswer download path in download.py

 run download.py
 
