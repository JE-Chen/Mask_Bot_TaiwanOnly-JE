# Line 機器人基本功能
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, AudienceRecipient, Limit, AgeFilter, RichMenu, RichMenuSize,
    RichMenuArea, RichMenuBounds, URIAction,ImagemapSendMessage,
    QuickReplyButton, MessageAction, ImageSendMessage, TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn,
    PostbackAction, CarouselTemplate, CarouselColumn, ConfirmTemplate, ButtonsTemplate, StickerSendMessage,
    AudioSendMessage,QuickReply,ImageMessage, VideoMessage, AudioMessage,StickerMessage,LocationMessage,
    LocationSendMessage, VideoSendMessage,BaseSize,Video,ExternalLink,MessageImagemapAction,ImagemapArea,FlexSendMessage,
    URIImagemapAction,BubbleContainer,ImageComponent,FileMessage,MemberLeftEvent,MemberJoinedEvent,
    FollowEvent,BeaconEvent,PostbackEvent,LeaveEvent,JoinEvent,UnfollowEvent
)

# 讀confing用
import configparser

# Line訊息主系統
from Models.Line_MessageMain import Line_MessageMain

from Core.Mask_Map_Core import Mask_Map_Core

Mask=Mask_Map_Core()

# configparser套件
config = configparser.ConfigParser()
config.read('key.ini')

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

Line_Main = Line_MessageMain(line_bot_api,MessageEvent, TextMessage, TextSendMessage, AudienceRecipient, Limit,
                             AgeFilter, RichMenu, RichMenuSize,
                             RichMenuArea, RichMenuBounds, URIAction,
                             QuickReplyButton, MessageAction, ImageSendMessage, TemplateSendMessage,
                             ImageCarouselTemplate, ImageCarouselColumn,
                             PostbackAction, CarouselTemplate,
                             CarouselColumn, ConfirmTemplate, ButtonsTemplate, StickerSendMessage, AudioSendMessage,
                             LocationSendMessage,
                             VideoSendMessage,QuickReply,ImagemapSendMessage,BaseSize,Video,ExternalLink,URIImagemapAction,
                             MessageImagemapAction,ImagemapArea,FlexSendMessage,BubbleContainer,ImageComponent)

app = Flask(__name__)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):

    '''
    每個event物件包含以下幾個屬性：

    type： event(事件)的形式，包括Message(使用者傳送訊息給聊天機器人),Follow(使用者將聊天機器人家為好友), Unfollow(使用者封鎖聊天機器人), Join(使用者將聊天機器人加入群組), Leave(聊天機器人離開群組), Postback(當使用者表現postback的動作), Beacon(當使用者進入或離開Line beacon的範圍) event。 
    
    replyToken： 在回應此訊息使用, 當程式要回應此訊息時須使用此token
    
    source： 訊息的來源，可能是一個user(使用者)、group(群組)或room(聊天室)
    若訊息的來源為user，則source中包含兩個屬性type(訊息來源的形式)及userId(傳送此訊息的使用者id) 
    若訊息的來源為group，則source中包含兩個屬性type(訊息來源的形式)及groupId(傳送此訊息的群組id)，若使用者有同意Official Accounts Terms of Use會多一個屬性userId(傳送此訊息的使用者id) 
    若訊息的來源為room，則source中包含兩個屬性type(訊息來源的形式)及roomId(傳送此訊息的聊天室id)，若使用者有同意Official Accounts Terms of Use會多一個屬性userId(傳送此訊息的使用者id) 
    
    timestamp： 此事件觸發的時間
    
    message： 傳送的訊息
    若為text(文字)訊息，則message包含三個屬性：id(訊息的識別id)、type(訊息的形式，text訊息type=text)、text(文字訊息中的文字)
    若為image(圖片)訊息，則message包含兩個屬性：id(訊息的識別id，此id可使用來下載此圖片)、type(訊息的形式，image訊息type=image)
    若為video(影片)訊息，則message包含兩個屬性：id(訊息的識別id，此id可使用來下載此影片)、type(訊息的形式，image訊息type=video)
    若為audio(聲音)訊息，則message包含兩個屬性：id(訊息的識別id，此id可使用來下載此音檔)、type(訊息的形式，image訊息type=audio)
    若為file(檔案)訊息，則message包含四個屬性：id(訊息的識別id，此id可使用來下載此檔案)、type(訊息的形式，file訊息type=file)、filename(檔案名稱)、filesize(檔案大小)
    若為location(位置)訊息，則message包含六個屬性：id(訊息的識別id)、type(訊息的形式，location訊息type=location)、title(位置名稱)、address(地址)、latitude(緯度)、longitude(經度)
    若為sticker(貼圖)訊息，則message包含四個屬性：id(訊息的識別id)、type(訊息的形式，sticker訊息type=sticker)、packageId、stickerId(每張貼圖都有其相對應的packageId及stickerId)
    '''
    if(event.message.type=='text'):
        text=event.message.text
        #Line_Main.Reply_Message(event.reply_token, text)
        print('Text!:\t',text)

@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    if(event.message.type=='image'):
        print('image!')

@handler.add(MessageEvent, message=VideoMessage)
def handle_image_message(event):
    if(event.message.type=='video'):
        print('video!')

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    if (event.message.type == 'location'):
        print('location!')
        lat=event.message.latitude
        lng = event.message.longitude
        Total=''
        for i in Mask.Mask_Search.Return_Nearby(lng,lat):
            Total+=str(i)+'\n'
        Line_Main.Reply_Message(event.reply_token, Total)

@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    if (event.message.type == 'sticker'):
        print('sticker!')

@handler.add(MessageEvent, message=AudioMessage)
def handle_audio_message(event):
    if (event.message.type == 'audio'):
        print('audio!')

@handler.add(MessageEvent, message=FileMessage)
def handle_file_message(event):
    if (event.message.type == 'file'):
        print('file!')

@handler.add(FollowEvent)
def handle_follow(event):
    print('FollowEvent')


@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print('UnfollowEvent')


@handler.add(JoinEvent)
def handle_join(event):
    print('JoinEvent')


@handler.add(LeaveEvent)
def handle_leave():
    print('LeaveEvent')


@handler.add(PostbackEvent)
def handle_postback(event):
    print('PostbackEvent')


@handler.add(BeaconEvent)
def handle_beacon(event):
    print('BeaconEvent')


@handler.add(MemberJoinedEvent)
def handle_member_joined(event):
    print('MemberJoinedEvent')


@handler.add(MemberLeftEvent)
def handle_member_left(event):
    print('MemberLeftEvent')

if __name__ == "__main__":
    app.run()
