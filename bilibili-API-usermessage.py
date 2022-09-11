# 导入依赖模块
import requests
import easygui

#创建输入框 给它起个名字
inputbox = easygui.enterbox("请输入用户UID")
#你输入的内容给送给url
url = "https://api.bilibili.com/x/space/acc/info?mid="+inputbox
url2 = "https://api.bilibili.com/x/relation/stat?vmid="+inputbox
url3 = "https://api.bilibili.com/x/space/navnum?mid="+inputbox
url4 = "https://api.bilibili.com/x/space/upstat?mid="+inputbox
#伪装成浏览器
headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
#获取数据 并在数据中获取data内容
response = requests.get(url,headers=headers).json()['data']
response2 = requests.get(url2,headers=headers).json()['data']
response3 = requests.get(url3,headers=headers).json()['data']
response4 = requests.get(url4,headers=headers).json()['data']
#在data内容分别获取名字(name)、性别(sex)、简介(sign)、职业区(official)
name = response['name']
sex = response['sex']
sign = response['sign']
official = response['official']['title']
birthday = response['birthday']
#2区域
mid = response2['mid']
following = response2['following']
follower = response2['follower']
#3区域
video = response3['video']
album = response3['album']
#4区域
#view = response4['archive']['view'] 一直找不到原因
#把获取的信息返回到这里
easygui.msgbox("名字："+str(name)+'\n'
                ""+'\n'
               "性别："+str(sex)+'\n'
               ""+'\n'
               "介绍："+str(sign)+'\n'
                ""+'\n'
               "up主职业区："+str(official)+'\n'
               ""+'\n'
                "生日："+str(birthday)+'\n'
                ""+'\n'
               "用户的UID："+str(mid)+'\n'
               ""+'\n'
               "关注量："+str(following)+'\n'
               ""+'\n'
               "粉丝量："+str(follower)+'\n'
               ""+'\n'
               "视频总数："+str(video)+'\n'
               ""+'\n'
               "相薄总数："+str(album)+'\n'
               ""+'\n'
                )