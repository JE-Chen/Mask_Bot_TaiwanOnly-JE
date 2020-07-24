import requests
import json
# ----------------------------------------------------------------------------------------------
class Line_MessageMain():

    def __init__(self,line_bot_api,MessageEvent, TextMessage, TextSendMessage, AudienceRecipient, Limit, AgeFilter, RichMenu, RichMenuSize,
    RichMenuArea, RichMenuBounds, URIAction,QuickReplyButton, MessageAction, ImageSendMessage, TemplateSendMessage, ImageCarouselTemplate,
    ImageCarouselColumn,PostbackAction, CarouselTemplate,CarouselColumn, ConfirmTemplate, ButtonsTemplate, StickerSendMessage, AudioSendMessage,
    LocationSendMessage,VideoSendMessage,QuickReply,ImagemapSendMessage,BaseSize,Video,ExternalLink,URIImagemapAction,MessageImagemapAction,
    ImagemapArea,FlexSendMessage,BubbleContainer,ImageComponent):

        self.line_bot_api=line_bot_api
        self.MessageEvent=MessageEvent
        self.TextMessage=TextMessage
        self.TextSendMessage=TextSendMessage
        self.AudienceRecipient=AudienceRecipient
        self.Limit=Limit
        self.AgeFilter=AgeFilter
        self.RichMenu=RichMenu
        self.RichMenuSize=RichMenuSize
        self.RichMenuArea=RichMenuArea
        self.RichMenuBounds=RichMenuBounds
        self.URIAction=URIAction
        self.QuickReplyButton=QuickReplyButton
        self.MessageAction=MessageAction
        self.ImageSendMessage=ImageSendMessage
        self.TemplateSendMessage=TemplateSendMessage
        self.ImageCarouselTemplate=ImageCarouselTemplate
        self.ImageCarouselColumn=ImageCarouselColumn
        self.PostbackAction=PostbackAction
        self.CarouselTemplate=CarouselTemplate
        self.CarouselColumn=CarouselColumn
        self.ConfirmTemplate=ConfirmTemplate
        self.ButtonsTemplate=ButtonsTemplate
        self.StickerSendMessage=StickerSendMessage
        self.AudioSendMessage=AudioSendMessage
        self.LocationSendMessage=LocationSendMessage
        self.VideoSendMessage=VideoSendMessage
        self.QuickReply=QuickReply
        self.ImagemapSendMessage=ImagemapSendMessage
        self.BaseSize=BaseSize
        self.Video=Video
        self.ExternalLink=ExternalLink
        self.URIImagemapAction=URIImagemapAction
        self.MessageImagemapAction=MessageImagemapAction
        self.ImagemapArea=ImagemapArea
        self.FlexSendMessage=FlexSendMessage
        self.BubbleContainer=BubbleContainer
        self.ImageComponent=ImageComponent

# ----------------------------------------------------------------------------------------------
    #單純寄送文字
    def Push_Message(self,user_id,Text):
        self.line_bot_api.push_message(user_id,self.TextSendMessage(text = Text))

    #寄送物件
    def Push_Message(self,user_id,object):
        self.line_bot_api.push_message(user_id,object)
# ----------------------------------------------------------------------------------------------
    #回復訊息
    def Reply_Message(self, reply_token, ReplyText):
        self.line_bot_api.reply_message(reply_token, self.TextSendMessage(text=str(ReplyText)))
# ----------------------------------------------------------------------------------------------
    def Send_Multicast_Message(self,text='Hello!',*args):
        for user in args:
            pass
        self.line_bot_api.multicast(user, self.TextSendMessage(text=text))
# ----------------------------------------------------------------------------------------------
    #消費配額
    def Send_Quota_Consumption(self,reply_token,Text='total usage: '):
        quota_consumption = self.line_bot_api.get_message_quota_consumption()
        self.line_bot_api.reply_message(
                reply_token, [
                self.TextSendMessage(text= Text+ str(quota_consumption.total_usage)),
            ]
        )
# ----------------------------------------------------------------------------------------------
    '''
    如何發送音訊呢？基本也是需要兩個參數值

    original_content_url：錄音url的檔案

    duration：這個主要是看你錄音時間有多久，不過建議設高一點，否則低於你的錄音秒數會導致發送音訊訊息時，顯示秒數會有問題
    '''
    def SendAudioMessage(self, user_id, Content_Url, duration):
        audio = self.AudioSendMessage(
            original_content_url=Content_Url,
            duration=duration
        )
        self.line_bot_api.push_message(user_id, audio)
        return 'AudioSendMessage Done!'
#----------------------------------------------------------------------------------------------
    #快速回復文字 出現在下方
    def QuickReply_Text(self, user_id, text, *args):
        """
        這裡很眼熟吧？就發送一個訊息
        quick_reply 底下的動作，就是幫你建立自動回覆的按鈕
        每一個 QuickReplyButton 都代表一個按鈕
        label 就是顯示的文字，text就是當你點下去，他會回復你的訊息
        最後一樣 push_message
        """
        for QuickReplyButtons in args:
            pass
        '''
            items = [
                        QuickReplyButton(
                            action = MessageAction(label = "泡麵", text = "自己煮！！"),
                            image_url = 'https://shareboxnow.com/wp-content/uploads/2020/01/S__7938233.jpg'
                        ),
                        QuickReplyButton(
                            action = MessageAction(label = "火鍋", text = "自己買！！"),
                        ),
                        QuickReplyButton(
                            action = MessageAction(label = "牛排", text = "自己煎！！"),
                        ),
                        QuickReplyButton(
                            action = MessageAction(label = "炒麵", text = "炒起來！！"),
                        ),
                        QuickReplyButton(
                            action = MessageAction(label = "鐵板燒", text = "我不會！！"),
                        ),
                        QuickReplyButton(
                            action = MessageAction(label = "生魚片", text = "該去漁港了！！"),
                        )
                    ]
        '''

        QuickReply_Text = self.TextSendMessage(
            text=text,
            quick_reply=self.QuickReply(
                items=QuickReplyButtons
            )
        )
        self.Push_Message(user_id, QuickReply_Text)
        return 'QuickReplyText: %s' % QuickReply_Text

    #含文字的快速回復
    def QuickReply_Image(self, user_id, original_content_url, preview_image_url, *args):
        """
        上面是文字，圖片也行

        """
        for QuickReplyButtons in args:
            pass
        '''
                items = [
                QuickReplyButton(
                    action = MessageAction(label = "好看請按我", text = "我知道！！"),
                    image_url = 'https://shareboxnow.com/wp-content/uploads/2020/01/S__7938233.jpg'
                ),
                QuickReplyButton(
                    action = MessageAction(label = "不好看請按我", text = "你是不是點錯了？"),
                )
            ]
        '''

        QuickReply_Image = self.ImageSendMessage(
            original_content_url=original_content_url,
            preview_image_url=preview_image_url,
            quick_reply=self.QuickReply(
                items=QuickReplyButtons
            )
        )
        self.Push_Message(user_id, QuickReply_Image)
        return 'QuickReplyImage: %s' % QuickReply_Image
#----------------------------------------------------------------------------------------------
    def Broadcast_Message(self, SendText):
        self.line_bot_api.broadcast(self.TextSendMessage(text=SendText))
        return 'OK'

    def Broadcast_Narrow_Message(self, SendText, Group, Start_Age, EndAge, Max):
        self.line_bot_api.narrowcast(
            messages=self.TextSendMessage(text=SendText),
            recipient=self.AudienceRecipient(Group),
            filter=filter(demographic=self.AgeFilter(gte=Start_Age, lt=EndAge)),
            limit=self.Limit(max=Max)
        )

    def Broadcast_Narrow_Message_State(self):
        narrowcast_progress = self.line_bot_api.get_progress_status_narrowcast(self.line_bot_api)
        assert narrowcast_progress.phase == 'succeeded'
        print(narrowcast_progress.success_count)
        print(narrowcast_progress.failure_count)
        print(narrowcast_progress.target_count)

#----------------------------------------------------------------------------------------------
    '''
    最多只能有4個 action
    '''
    #ImageUrl 需使用真實的 有.bmp png jpg jpeg etc..
    def ButtonsTemplate_send_message(self, user_id, Alt_Text, Image_Url, Title, Text, *args):

        for item in args:
            pass
        # 這是一個傳送按鈕的模板，架構解說
        buttons_template_message = self.TemplateSendMessage(
            alt_text=Alt_Text,  # 當你發送到你的Line bot 群組的時候，通知的名稱
            template=self.ButtonsTemplate(
            thumbnail_image_url=Image_Url,  # 你的按鈕模板的圖片是什麼
            title=Title,  # 你的標題名稱
            text=Text,  # 應該算是一個副標題
            # 下面主要就是你希望使用者點擊了按鈕會有哪些動作，最多只能有四個action！超過會報錯喔！
            # PostbackAction 說真的這個我不知道要幹嘛用，可能後台可以收數據？我點了就回應我 postback text，至於data我就不熟了
            # MessageAction 跟上面差不多
            # URIAction 跳轉到URL
            # label 在按鈕模板上顯示的名稱
            # display_text 點擊會顯示的文字
            # data 這個我真的就不知道了
            # text點擊後顯示
            # uri跳轉到的url，看你要改什麼都行，只要是url
            actions = item
        )
    )
        self.line_bot_api.push_message(user_id, buttons_template_message)
        return 'ButtonsTemplate_send_message Done!'
        '''
            [
            # 說真的這個我不知道要幹嘛用，可能後台可以收數據？我點了就回應我 postback text，至於data我就不熟了
            PostbackAction(
                label = 'postback',  # 在按鈕模板上顯示的名稱
                display_text = 'postback text',  # 點擊會顯示的文字
                data = 'action=buy&itemid=1'  # 這個...我真的就不知道了～
            ),
            # 跟上面差不多
            MessageAction(
                label = '現在幾點了？',   # 在按鈕模板上顯示的名稱
                text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 點擊後，顯示現在的時間，這些都可以隨意修改喔！
            ),
            # 跳轉到URL
            URIAction(
                label = '我的部落格',  # 在按鈕模板上顯示的名稱
                uri = 'https://shareboxnow.com/'  # 跳轉到的url，看你要改什麼都行，只要是url
            ),
            # 這裡可以跟上面一樣，可以重複不限定只有一個 URIAction
            URIAction(
                label = 'Google',  # 在按鈕模板上顯示的名稱
                uri = 'https://www.google.com.tw/'  # 跳轉到的url，看你要改什麼都行，只要是url
            )
        ]
        '''
#----------------------------------------------------------------------------------------------
    '''
    圖片必須是url，不能是本地端的以及中間不能有中文，否則你執行會失敗(親身經驗)。
    
    original_content_url ：當你點擊圖片訊息時，點開圖片的畫面
    
    preview_image_url ：當收到圖片訊息時，所看到的畫面
    '''
    def SendImageMessage(self,user_id,original_content_url,preview_image_url):
        image_message = self.ImageSendMessage(
            original_content_url=original_content_url,
            preview_image_url=preview_image_url
        )
        self.line_bot_api.push_message(user_id, image_message)
        return 'ImageSendMessage Done!'
#----------------------------------------------------------------------------------------------
    '''
    發送位置需要有四個參數
    
    title：接收者所看到的第一個標題
    
    address：這裡是哪裡？
    
    latitude, longitude：地圖的經緯度
    
    哪要如何取得經緯度呢？請到Google map 指定你要的位置，點擊地圖右鍵 “這是哪裡?“
    '''
    def SendLocationMessage(self,user_id,title,address,latitude,longitude):
        location = self.LocationSendMessage(
            title=title,
            address=address,
            latitude=latitude,
            longitude=longitude
        )
        self.line_bot_api.push_message(user_id, location)
        return 'LocationSendMessage Done!'
#----------------------------------------------------------------------------------------------
    '''
    要如何發送貼紙訊息呢？需要兩個參數值
    
    package_id：每一組貼紙的id
    
    sticker_id：這個貼紙在package裡面的id是什麼？
    '''
    def SendStickerMessage(self,user_id,Package_Id='1',Sticker_Id='1'):
        sticker_message = self.StickerSendMessage(
            package_id=Package_Id,
            sticker_id=Sticker_Id
        )
        self.line_bot_api.push_message(user_id, sticker_message)
        return 'StickerSendMessage Done!'
#----------------------------------------------------------------------------------------------
    '''
    每一個輪播的資料都透過CarouselColumn包起來，所以看要建立幾個資料，最後他會放在一個 columns裡面，
    簡單說父親是 columns，他的兒子是CarouselColumn，看要給他幾個兒子
    '''
    def SendTemplate_CarouselTemplate(self,user_id,alt_text,thumbnail_image_url,title,text,*args):
        # 這是一個傳送 輪播的模板
        #alt_text 標題名
        #thumbnail_image_url 顯示的圖片
        # label顯示的文字
        # display_text回覆的文字
        #data 取得資料？
        for item in args:
            pass
            '''
              columns = [
                    # 這是我第一個兒子 
                    CarouselColumn(
                        thumbnail_image_url = 'https://shareboxnow.com/wp-content/uploads/2020/02/IMG_5601.jpg',  # 呈現圖片
                        title = '這是一隻貓頭鷹',  # 你要顯示的標題
                        text = '想養嗎？',  # 你想問的問題或是敘述
                        actions = [
                            PostbackAction(
                                label = '養',  # 顯示的文字
                                display_text = '對不起，這不是我的',  # 回覆的文字
                                data = 'action=buy&itemid=1'  # 取得資料？
                            ),
                            MessageAction(
                                label = '不養',  # 顯示的文字 
                                text = '好喔！沒問題'  # 回覆的文字
                            ),
                            URIAction(
                                label = '這是我的網址',  # 顯示的文字 
                                uri = 'https://shareboxnow.com/'   # 跳轉的url
                            )
                        ]
                    ),
                    # 這是我第二個兒子，下面的都跟上面一樣，只是內容稍為不同，如果想嘗試可以多複製一個看看唷！ 
                    # 記得要在父親裡面，不然你就沒有父親了，就會報錯還有 , 要特別注意
                    CarouselColumn(
                        thumbnail_image_url = 'https://shareboxnow.com/wp-content/uploads/2020/02/IMG_5599.jpg',
                        title = '我還是貓頭鷹',
                        text = '想喂我吃東西嗎？',
                        actions = [
                            PostbackAction(
                                label = '想',
                                display_text = '但我不想吃',
                                data = 'action=buy&itemid=2'
                            ),
                            MessageAction(
                                label = '不想',
                                text = '我剛好也不餓，謝謝你'
                            ),
                            URIAction(
                                label = '這還是我的網址 哈',
                                uri = 'https://shareboxnow.com/'
                            )
                        ]
                    )
                ]
            '''
        carousel_template_message = self.TemplateSendMessage(
            alt_text=alt_text,  # 通知訊息的名稱
            template=self.CarouselTemplate(
                # culumns 是一個父親
                columns=item
            )
        )
        self.line_bot_api.push_message(user_id, carousel_template_message)
        return 'CarouselTemplate Done!'
#----------------------------------------------------------------------------------------------
    '''
    最多只能有兩個 action
    '''
    def SendTemplate_ComfirmTemplate(self,user_id,alt_text,text,*args):
        # 這是一個傳送確認的模板
        for item in args:
            pass
            '''
             actions = [
                    PostbackAction(
                        label = '確認',  # 顯示名稱
                        display_text = '那還不快去買！？',  # 點擊後，回傳的文字
                        data = 'action=buy&itemid=1'  # 取得資料！？
                    ),
                    MessageAction(
                        label = '不買',  # 顯示名稱
                        text = '那就不買吧！'  # 點擊後，回傳的文字
                    )
                ]
            '''
        confirm_template_message = self.TemplateSendMessage(
            alt_text=alt_text,  # 當你發送到你的Line bot 群組的時候，通知的名稱
            template=self.ConfirmTemplate(
                text=text,  # 你要問的問題，或是文字敘述
                # action 最多只能兩個
                actions=item
            )
        )
        self.line_bot_api.push_message(user_id, confirm_template_message)
        return 'ConfirmTemplate Done!'
#----------------------------------------------------------------------------------------------
    '''
    每一個 action，只有三種類型 URIAction、PostbackAction、MessageAction，都可以隨意跟改，主要看你的需求會是什麼
    '''
    def SendTemplateMessage_ImageCarouselTemplate(self,user_id,*args):
        # 這是一個傳送 圖片輪播的模板，架構解說
        # image_url 分享網址給你看
        #label 顯示的文字
        #uri 跳轉的url
        for item in (args):
            pass
            '''
                   columns = [
                        # 這是我第一個女兒
                        ImageCarouselColumn(
                            # 她的圖片在這裡
                            image_url = 'https://shareboxnow.com/wp-content/uploads/2020/02/IMG_5599.jpg',
                            # 她的動作：分享網址給你看
                            action = URIAction(
                                    label = '這是我的網址',  # 顯示的文字
                                    uri = 'https://shareboxnow.com/'   # 跳轉的url
                                    )
                        ),
                        # 這是我第二個女兒
                        ImageCarouselColumn(
                            # 這是我二女兒的圖片在這裡
                            image_url = 'https://shareboxnow.com/wp-content/uploads/2020/02/IMG_5601.jpg',
                            # 她的動作是說 叫你不要點他，如果你點了 她會回復你訊息
                            action = PostbackAction(
                                label = '拜託不要選我',
                                display_text = '就說叫你不要選我了！為什麼要選我？',
                                data = 'action=buy&itemid=2'  # 取得資料？
                            )
                        )
                    ]
            '''
        image_carousel_template_message = self.TemplateSendMessage(
            alt_text='我是一個圖片輪播 模板',  # 發送通知訊息名稱
            template=self.ImageCarouselTemplate(
                # 改一下角色 我是媽媽
                columns=item
            )
        )
        self.line_bot_api.push_message(user_id, image_carousel_template_message)
        return 'ImageCarouselTemplate Done!'
#----------------------------------------------------------------------------------------------
    '''
    發送影片訊息需要兩個參數，其實就跟圖片一樣
    original_content_url, preview_image_url
    '''
    def Video_send_message(self,user_id,original_content_url,preview_image_url):
        video_message = self.VideoSendMessage(
            original_content_url=original_content_url,
            preview_image_url=preview_image_url
        )
        self.line_bot_api.push_message(user_id, video_message)
        return 'VideoSendMessage Done!'

# ----------------------------------------------------------------------------------------------
    '''
    [
                    self.URIImagemapAction(
                        link_uri='https://example.com/',
                        area=self.ImagemapArea(
                            x=0, y=0, width=520, height=1040
                        )
                    ),
                    self.MessageImagemapAction(
                        text='hello',
                        area=self.ImagemapArea(
                            x=520, y=0, width=520, height=1040
                        )
                    )
                ]
    '''

    def ImagemapSendMessage(self,original_content_url,preview_image_url,link_uri,label,*args):
        for item in args:
            pass

            imagemap_message = self.ImagemapSendMessage(
                base_url='https://example.com/base',
                alt_text='this is an imagemap',
                base_size=self.BaseSize(height=1040, width=1040),
                video=self.Video(
                    original_content_url=original_content_url,
                    preview_image_url=preview_image_url,
                    area=self.ImagemapArea(
                        x=0, y=0, width=1040, height=585
                    ),
                    external_link=self.ExternalLink(
                        link_uri=link_uri,
                        label=label,
                    ),
                ),
                actions=item
            )

# ----------------------------------------------------------------------------------------------
    '''
    貌似要高級帳戶
    '''
    def SendFlex_Message(self,alt_text='hello',direction='ltr',url='https://example.com/cafe.jpg',size='full'
        ,aspect_ratio='20:13',aspect_mode='cover',uri='http://example.com',label='label'):
        flex_message = self.FlexSendMessage(
            alt_text=alt_text,
            contents=self.BubbleContainer(
                direction=direction,
                hero=self.ImageComponent(
                    url=url,
                    size=size,
                    aspect_ratio=aspect_ratio,
                    aspect_mode=aspect_mode,
                    action=self.URIAction(uri=uri, label=label)
                )
            )
        )
# ----------------------------------------------------------------------------------------------
    '''
    Maybe Need Premium Account
    '''
    def Create_RichMenu(self, Selected=True, Name="Test RichMenu", Chat_Bar_Text="Tap here", ):
        Show_RichMenu = self.RichMenu(
            size=self.RichMenuSize(width=2500, height=843),
            selected=Selected,
            name=Name,
            chat_bar_text=Chat_Bar_Text,
            areas=[self.RichMenuArea(
                # 這邊是陣列的格式，可以動態設定自己要的區域想要有什麼功能
                bounds=self.RichMenuBounds(x=0, y=0, width=2500, height=843),
                action=self.URIAction(label='Go to line.me', uri='https://line.me'))]
        )
        self.rich_menu_id = self.line_bot_api.create_rich_menu(rich_menu=Show_RichMenu)
        print(self.rich_menu_id, "\t RichMenu ID")

    def Create_RichMenu_Json(self,token):
        headers = {"Authorization": ("Bearer "+token), "Content-Type": "application/json"}

        body = {
            "size": {"width": 2500, "height": 1686},
            "selected": "true",
            "name": "Controller",
            "chatBarText": "Controller",
            "areas": [
                {
                        "bounds": {"x": 551, "y": 325, "width": 321, "height": 321},
                        "action": {"type": "message", "text": "up"}
                },
                {
                        "bounds": {"x": 876, "y": 651, "width": 321, "height": 321},
                        "action": {"type": "message", "text": "right"}
                },
                {
                        "bounds": {"x": 551, "y": 972, "width": 321, "height": 321},
                        "action": {"type": "message", "text": "down"}
                },
                {
                        "bounds": {"x": 225, "y": 651, "width": 321, "height": 321},
                        "action": {"type": "message", "text": "left"}
                },
                {
                        "bounds": {"x": 1433, "y": 657, "width": 367, "height": 367},
                        "action": {"type": "message", "text": "btn b"}
                },
                {
                        "bounds": {"x": 1907, "y": 657, "width": 367, "height": 367},
                        "action": {"type": "message", "text": "btn a"}
                }
            ]
        }

        req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                                   headers=headers, data=json.dumps(body).encode('utf-8'))
        print(req.text)

    def Upload_RichMenu(self):
        file = self.request.files['the_file'].read()
        rich_menu_id = self.request.form['richmenu_id']
        content_type = "image/png"
        try:
            self.line_bot_api.set_rich_menu_image(
                rich_menu_id, content_type, file)
        except Exception as e:
            print("===Upload Exception===")
        return {'result': 'upload ok'}, 200

    def Set_RichMenu(self):
        rich_menu_id = self.request.form['richmenu_id']
        try:
            self.line_bot_api.set_default_rich_menu(rich_menu_id)
        except:
            print("Maybe your richmenu id error.")
        return {'result': 'set default ok!'}, 200

    def Get_RichMMenu(self):
        rich_menu_list = self.line_bot_api.get_rich_menu_list()
        total = []
        for rich_menu in rich_menu_list:
            total.append(rich_menu.rich_menu_id)
        return {'result': total}, 200

    def Delete_RichMenu(self):
        rich_menu_id = self.request.form['richmenu_id']
        try:
            self.line_bot_api.delete_rich_menu(rich_menu_id)
        except:
            print("Maybe your richmenu id error.")
        return {'result': f'{rich_menu_id} is delete!'}, 200
#----------------------------------------------------------------------------------------------
    def Leave_Group(self,group_id):
        self.line_bot_api.leave_group(group_id)


    def Leave_Room(self,room_id):
        self.line_bot_api.leave_room(room_id)
#----------------------------------------------------------------------------------------------
    '''
    Maybe Need Premium Account
    '''
    def Get_Group_Profile(self, group_id, user_id):
        profile = self.line_bot_api.get_group_member_profile(group_id, user_id)
        print(profile.display_name)
        print(profile.user_id)
        print(profile.picture_url)

    def Get_Room_Profile(self, room_id, user_id):
        profile = self.line_bot_api.get_room_member_profile(room_id, user_id)
        print(profile.display_name)
        print(profile.user_id)
        print(profile.picture_url)

    def Get_Group_ID(self, group_id):
        member_ids_res = self.line_bot_api.get_group_member_ids(group_id)
        print(member_ids_res.member_ids)
        print(member_ids_res.next)

    def Get_Room_ID(self, room_id):
        member_ids_res = self.line_bot_api.get_room_member_ids(room_id)
        print(member_ids_res.member_ids)
        print(member_ids_res.next)

#----------------------------------------------------------------------------------------------
    def Get_message_content(self,message_id,file_path):
        message_content = self.line_bot_api.get_message_content(message_id)
        with open(file_path, 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)
#----------------------------------------------------------------------------------------------