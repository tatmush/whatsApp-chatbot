from selenium import webdriver
import time

#selenium test
def seleniumTest(i):
    print(i)

    browser = webdriver.Firefox()
    browser.get('https://web.whatsapp.com/')
    time.sleep(45)
    unopenedChats=browser.find_elements_by_xpath('.//span[@class = "OUeyt _3zmhL"]')
    for unopenedChat in unopenedChats[3:5]:
    	  	
    	#click the first chat
    	unopenedChat.click()

    	#selecting all incoming messages
    	incomingMessages=browser.find_elements_by_class_name('message-in')

    	#getting the last message. Returns line with time in it as well
    	lastMessage=incomingMessages[len(incomingMessages)-1].text

    	#remove the time portion of string
    	foulString=lastMessage.splitlines()

    	messageFromUser=foulString[0]
    	print(messageFromUser)

    	
    	unopenedChats.remove(unopenedChat)

    print("DONE")

    #time is in seconds, change it to suit your internet connection and video size.
   #time.sleep(180)
    #browser.quit()
    
seleniumTest(1)
'''for i in range(100):
    
    seleniumTest(i)
    
print("DONE")

/html/body/div/div/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div[2]/div[2]/div[2]/span[1]/div/span

/html/body/div/div/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div[2]/div[2]/div[2]/span[1]/div/span








div.vW7d1:nth-child(22) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)

innerHTML: iri sei independence
outerHTML: <span dir="ltr" class="selectable-text invisible-space copyable-text">iri sei independence</span>
css_selector: div.vW7d1:nth-child(19) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)
css_path: html.js.adownload.cssanimations.csstransitions.no-webp.wf-roboto-n4-active.wf-roboto-n5-active.wf-roboto-n3-active.wf-opensans-n4-active.wf-opensans-n6-active.wf-active body.web div#app div._1FKgS.app-wrapper-web.bFqKf div.app._3dqpi.two div._3q4NP._1Iexl div#main._1GX8_ div._3zJZ2 div.copyable-area div._2nmDZ div._9tCEa div.vW7d1 div._3_7SH._3DFk6.message-out.tail div.Tkt2p div.copyable-text div._3zb-j.ZhF0n span.selectable-text.invisible-space.copyable-text
xpath: /html/body/div/div/div/div[3]/div/div[2]/div/div/div[3]/div[19]/div/div/div[1]/div/span


innerHTML: Ngatitsvage vanhu
outerHTML: <span dir="ltr" class="selectable-text invisible-space copyable-text">Ngatitsvage vanhu</span>
css_selector: div.vW7d1:nth-child(34) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)
css_path: html.js.adownload.cssanimations.csstransitions.no-webp.wf-roboto-n4-active.wf-roboto-n5-active.wf-roboto-n3-active.wf-opensans-n4-active.wf-opensans-n6-active.wf-active body.web div#app div._1FKgS.app-wrapper-web.bFqKf div.app._3dqpi.two div._3q4NP._1Iexl div#main._1GX8_ div._3zJZ2 div.copyable-area div._2nmDZ div._9tCEa div.vW7d1 div._3_7SH._3DFk6.message-in div.Tkt2p div.copyable-text div._3zb-j.ZhF0n span.selectable-text.invisible-space.copyable-text
xpath: /html/body/div/div/div/div[3]/div/div[2]/div/div/div[3]/div[34]/div/div/div[1]/div/span



div._2wP_Y:nth-child(15) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)
div._2wP_Y:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)
div._2wP_Y:nth-child(14) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)
div._2wP_Y:nth-child(14) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)
div._2wP_Y:nth-child(13) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)
div._2wP_Y:nth-child(12) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)



div.vW7d1:nth-child(22) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)
div.vW7d1:nth-child(24) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)

div.vW7d1:nth-child(24) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)



Python 3.7.0a4 (v3.7.0a4:07c9d85, Jan  9 2018, 07:07:02) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from selenium import webdriver
>>> browser=webdriver.Firefox()
>>> browser.get('https://web.whatsapp.com/')
>>> a=browser.find_element_by_css_selector('div._2wP_Y:nth-child(12) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
>>> a.text
'Isa Tsitsi Munikwa'
>>> a.click()
>>> b=browser.find_element_by_css_selector('div._2wP_Y:nth-child(13) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
>>> b.click()
>>> c=find_element_css_selector('div.vW7d1:nth-child(22) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'find_element_css_selector' is not defined
>>> c=browser.find_element_css_selector('div.vW7d1:nth-child(22) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'WebDriver' object has no attribute 'find_element_css_selector'
>>> c=browser.find_element_by_css_selector('div.vW7d1:nth-child(22) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
>>> c.text()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> c.text
'did you watch the video'
>>> c=browser.find_element_by_css_selector('div.vW7d1:nth-child(24) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
>>> c.text
'Rakareba'
>>> d=browser.find_element_by_css_selector('._2S1VP')
>>> d.send_keys("this was sent automatically")
>>> e.browser.find_element_by_css_selector('._2lkdt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'e' is not defined
>>> e=browser.find_element_by_css_selector('._2lkdt')
>>> e.click()
>>>
'''