from flask import Flask, request
import telegram
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, Dispatcher
import pandas as pd
import numpy as np
import logging
import os
import random
import sys
import random
from random import randint

#load files
df_bot_pv = pd.read_csv('./csv_files/dfpv.csv')
df_bot_cart = pd.read_csv('./csv_files/dfcart.csv')
df_bot_fav = pd.read_csv('./csv_files/dffav.csv')
df_bot_buy = pd.read_csv('./csv_files/dfbuy.csv')

#defining values
FIRST, SECOND = range(2)
random.seed(42)
value = randint(4831,5000)

#function to display taobao welcome photo and message at /start
def start(bot, update):
    update.effective_message.reply_photo(photo='https://www.mp.com.sg/wp-content/uploads/shipping-from-taobao-1.png')
    update.effective_message.reply_text("Welcome to mytaobao! We provide you recommendations on taobao products for your consideration!"+"\n\n"+"To facilitate your user experience, feel free to explore our list of commands below anytime you wish to do so!"+ "\n\n" + "/start : to start mytaobao bot!"+"\n"+ "/help : our friendly bot will assist you in answering a list of common FAQs!"+"\n"+"/links : photos and URLs to our top 10 best selling products!"+"\n"+"/exit : there is always a time to say goodbye. Hope we have served you well!"+"\n\n"+" Firstly, how may I address you?")
    return FIRST
    
def name(bot, update):
    update.effective_message.reply_text("Hi "+ update.effective_message.text + "! " + "If you have not registered an account with us, kindly do so first via the command '/register'. Otherwise, please provide us your User ID.")
    return SECOND

def register(bot, update):
    update.effective_message.reply_text("You are now a registered user! Your User ID is: {}".format(value) +". Now, please login by entering your given user ID:")    

    

def response(bot, update):
    num = update.effective_message.text
    if num.isdigit()==False:
        update.effective_message.reply_text("Invalid input. Please key in valid User ID.") 
        return
    
    pv = str(list(df_bot_pv[df_bot_pv['User ID']==int(num)]['Item ID']))
    cart = str(list(df_bot_cart[df_bot_cart['User ID']==int(num)]['Item ID']))
    fav = str(list(df_bot_fav[df_bot_fav['User ID']==int(num)]['Item ID']))
    buy = str(list(df_bot_buy[df_bot_buy['User ID']==int(num)]['Item ID']))  

    
    n  =  int(num)
    pv_true = n in df_bot_pv['User ID'].unique()
    cart_true = n in df_bot_cart['User ID'].unique()
    fav_true = n in df_bot_fav['User ID'].unique()
    buy_true = n in df_bot_buy['User ID'].unique()
    
    try:
        if int(num) in range(0,4831):
            #case 1: pv + cart + fav + buy
            if pv_true and cart_true and fav_true and buy_true:
                update.effective_message.reply_text('Welcome back! Based on your past consumer history, we wish to recommend the following items to you:  \n\n'+ 'Top 10 most viewed items: {}'.format(pv) + '\n\n Top 10 most add to cart items: {}'.format(cart) + ' \n\n Top 10 most favorite items: {}'.format(fav) + ' \n\n Top 10 most bought items: {}'.format(buy))
            #case 2: pv + fav
            if pv_true and not cart_true and fav_true and not buy_true:
                update.effective_message.reply_text('Welcome back! Based on your past consumer history, we wish to recommend the following items to you:  \n\n' + 'Top 10 most viewed items: {}'.format(pv) + '\n\n Top 10 most favorite items: {}'.format(fav))
            #case 3: pv + cart
            if pv_true and cart_true and not fav_true and not buy_true:
                update.effective_message.reply_text('Welcome back! Based on your past consumer history, we wish to recommend the following items to you:  \n\n' + 'Top 10 most viewed items: {}'.format(pv) + '\n\n Top 10 most add to cart items: {}'.format(cart))   
            #case 4: pv + cart + buy
            if pv_true and cart_true and not fav_true and buy_true:
                update.effective_message.reply_text('Welcome back! Based on your past consumer history, we wish to recommend the following items to you:  \n\n' + 'Top 10 most viewed items: {}'.format(pv) + '\n\n Top 10 most add to cart items: {}'.format(cart) + '\n\n Top 10 most bought items: {}'.format(buy))
            #case 5: pv
            if pv_true and not cart_true and not fav_true and not buy_true:
                               update.effective_message.reply_text('Welcome back! Based on your past consumer history, we wish to recommend the following items to you:  \n\n' + 'Top 10 most viewed items: {}'.format(pv))
        elif int(num) == value:
            update.effective_message.reply_text('Thank you for your first visit! We wish to recommend the following items to you: [141515, 3423, 137441, 142407, 115747, 208890, 133969, 47310, 134392, 120665]')
        else:
            update.effective_message.reply_text("Invalid input. Please key in valid User ID.")                                      
    except ValueError:
        update.effective_message.reply_text("Invalid input. Please key in valid User ID.")    
    return   

    
def helpme(bot, update):
    update.effective_message.reply_text("Q: What should I do first when I start the bot?"+ "\n"+"A: Please key in your name if you have NOT done so." + "\n\n" + "Q: I have an existing account with taobao. How should I retrieve my recommendations?" + "\n"+ "A: If you are an existing user, please key in your user ID between 0 to 4830. We would then recommend you the top 10 items to view/add to cart/favorite/purchase based on your user preference history."+ "\n\n"+ "Q: I am a new user, how do I get recommendations?"+ "\n"+ "A: If you are a new user, we wish to introduce you the top 10 most popular products on our website. Kindly key in your new User ID.")       

    
def links(bot, update):
    update.effective_message.reply_text("Here are the photos and corresponding URLs to our top 10 hot sellers of all time! (In order of priority):" + "\n\n")
    #item 1 
    update.effective_message.reply_photo(photo="http://www.price.com.hk/space/product/234000/234995_axbw0j_0.jpg")
    update.effective_message.reply_text("https://detail.tmall.com/item.htm?spm=a212uc.12510681.1265890180.7.39485e74n6S3dK&acm=lb-zebra-445083-5913228.1003.4.7108901&id=586564770220&scm=1003.4.lb-zebra-445083-5913228.ITEM_586564770220_7108901")
    #item 2
    update.effective_message.reply_photo(photo="https://china.pr.imgs.coovee.net/2014/09-27/06_09_42_19_39111303326945171542.jpg")
    update.effective_message.reply_text("https://detail.tmall.com/item.htm?spm=a212uc.12510681.7655910553.1.71f25e74s0vo5A&acm=lb-zebra-445083-6165048.1003.4.6125542&id=585492222231&scm=1003.4.lb-zebra-445083-6165048.ITEM_585492222231_6125542")
    #item 3
    update.effective_message.reply_photo(photo="https://img-cms.pchome.net/article/1k2/pu/4u/pbp4ej-ho0.png?x-oss-process=image/format,jpg/resize,m_lfit,w_720/quality,q_100")
    update.effective_message.reply_text("https://detail.tmall.com/item.htm?spm=a212uc.12510681.2367201086.3.39485e74n6S3dK&acm=lb-zebra-445083-5716819.1003.4.6125562&id=586564418860&scm=1003.4.lb-zebra-445083-5716819.ITEM_586564418860_6125562")
    #item 4
    update.effective_message.reply_photo(photo                                         ="http://static.chachehao.com/bao/uploaded/i4/820521956/O1CN01T4dY8w1QJtGedy7Dw_!!820521956.jpg")
    update.effective_message.reply_text("https://detail.tmall.com/item.htm?spm=a212uc.12510681.6374292700.4.39485e74n6S3dK&acm=lb-zebra-445083-5716948.1003.4.5193416&id=595307672021&scm=1003.4.lb-zebra-445083-5716948.ITEM_595307672021_5193416")
    #item 5
    update.effective_message.reply_photo(photo=
                                         "http://img1.miaomiaoz.com/image/0a218c9db1119fa86484742a62079a19.jpeg")
    update.effective_message.reply_text("https://detail.tmall.com/item.htm?spm=a212uc.12510681.5727280828.7.39485e74n6S3dK&acm=lb-zebra-445083-5716793.1003.4.7108930&id=592122594102&scm=1003.4.lb-zebra-445083-5716793.ITEM_592122594102_7108930&sku_properties=5919063:6536025")
    #item 6
    update.effective_message.reply_photo(photo=                                         "http://img2019.manmanbuy.com/r_img/img/20190908/19/0c01aa6e2b9e4602b7e4829a70214d33.jpg")
    update.effective_message.reply_text("https://detail.tmall.com/item.htm?spm=a212uc.12510681.8876145820.2.39485e74n6S3dK&acm=lb-zebra-445083-6769395.1003.4.7108867&id=602405659594&scm=1003.4.lb-zebra-445083-6769395.ITEM_602405659594_7108867&skuId=4212029860055")
    #item 7
    update.effective_message.reply_photo(photo=                                         "https://img.alicdn.com/bao/uploaded/i4/3315288987/TB1Sf70pYZnBKNjSZFrXXaRLFXa_!!0-item_pic.jpg")
    update.effective_message.reply_text("https://detail.tmall.com/item.htm?spm=a212uc.12510681.2576255250.11.39485e74n6S3dK&acm=lb-zebra-445083-5716892.1003.4.6125538&id=585357737845&scm=1003.4.lb-zebra-445083-5716892.ITEM_585357737845_6125538&skuId=3965591493646")
    #item 8
    update.effective_message.reply_photo(photo="https://g-search1.alicdn.com/img/bao/uploaded/i4/3519227058/O1CN01MgscvD220bznOBN7r_!!0-item_pic.jpg_300x300.jpg")
    update.effective_message.reply_text("https://detail.tmall.com/item.htm?spm=a212uc.12510681.7655910553.7.39485e74n6S3dK&acm=lb-zebra-445083-6165048.1003.4.6125542&id=587890253558&scm=1003.4.lb-zebra-445083-6165048.ITEM_587890253558_6125542&skuId=4172459150483")
    #item 9
    update.effective_message.reply_photo(photo="https://china.pr.imgs.coovee.net/2029/06-19/02_00_00_06_604939843507033688410.jpg")
    update.effective_message.reply_text("https://detail.tmall.com/item.htm?spm=a212uc.12510681.8370422910.3.39485e74n6S3dK&pos=3&acm=lb-zebra-445083-5732421.1003.1.5206150&id=585638271367&scm=1007.13976.92121.0")
    #item 10
    update.effective_message.reply_photo(photo="https://g-search1.alicdn.com/img/bao/uploaded/i3/3329874572/O1CN01yyLKVh1je1OJf6y8a_!!3329874572.jpg_300x300.jpg")
    update.effective_message.reply_text("https://detail.tmall.com/item.htm?spm=a212uc.12510681.4533881272.9.39485e74n6S3dK&acm=lb-zebra-445083-5716928.1003.4.6125595&id=585492550504&scm=1003.4.lb-zebra-445083-5716928.ITEM_585492550504_6125595&sku_properties=1627207:11010012")
    
def exit(bot, update):
    update.effective_message.reply_photo(photo ='https://www.ft.com/__origami/service/image/v2/images/raw/http%3A%2F%2Fcom.ft.imagepublish.upp-prod-us.s3.amazonaws.com%2F6aad2a94-9693-11e9-98b9-e38c177b152f?fit=scale-down&source=next&width=700')
    update.effective_message.reply_text("You have now exited the bot! We wish you a pleasant day ahead!")
            
if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "1053969263:AAEQnP6TtgiCXLd-pRi9GKUDr_U7chIupx0"
    NAME = "irecommend-taobao"

    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Add handlers
    conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start), CommandHandler('help', helpme), CommandHandler('links', links)],
    states={
        FIRST: [MessageHandler(Filters.text, name), CommandHandler('help', helpme), CommandHandler('links', links), CommandHandler('register',register)],
        SECOND: [MessageHandler(Filters.text, response), CommandHandler('help', helpme), CommandHandler('links', links), CommandHandler('register',register)]
    },
    fallbacks=[CommandHandler('exit', exit),CommandHandler('start', start)]
)
    
    dp.add_handler(conv_handler)

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()