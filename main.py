#!/usr/bin/env python
# -*- coding: utf-8 -*-

#imports
import sys, os, re
from string import Template
from libs.helpers import timesince
import webkit, tweepy, webbrowser
import gobject
import webbrowser
import ConfigParser

#gtk init
try:
   import pygtk
   pygtk.require("2.0")
except:
    pass
try:
  import gtk
  import gtk.glade
except:
  sys.exit(1)  

#twitter class
class Twitter:

  def __init__(self):
    #starting the twitter part
    config = ConfigParser.RawConfigParser()
    config.read('beezu.cfg')    
    
    client_token = config.get('Client', 'token')
    client_secret = config.get('Client', 'secret')
    auth = tweepy.OAuthHandler(client_token, client_secret)
    user_token = config.get('User', 'token')
    user_secret = config.get('User', 'secret')
    auth.set_access_token(user_token, user_secret)

    self.twitter = tweepy.API(auth)  


#beezu class
class Beezu:
  myself = None
  def __init__(self):
    #opening the glade file and connecting the signals
    self.main = gtk.glade.XML("beezu.glade")
    self.win = self.main.get_widget("main_window")
    self.swin = self.main.get_widget("scroll_window")
    signals = { 
      "quit" : self.quit,
    }
    self.main.signal_autoconnect(signals)
    
    self.browser = webkit.WebView()
    self.t = Twitter()
    self.myself = self.t.twitter.auth.get_username()
    self.browser.connect('navigation-requested', self.open_link, None, False)
    self.browser.connect('title-changed',self.alterou)
    
    gobject.idle_add(self.browser_content)
    

    #path = "file://"+os.getcwd()+"/templates/"
    #content = self.browser_content()
    #browser.load_string(content, "text/html", "utf-8", path)
    #print content


    self.swin.add(self.browser)
    self.win.show_all()

  def alterou (self, view, frame, title):
    if title != "null":
      print "clicou "+title


  def open_link(self, view, frame, req, data=None, x=None):
    uri = req.get_uri()
    if uri.startswith("http://") or uri.startswith("https://"):
      webbrowser.open_new_tab(uri)
      return True
    else:
      #user clicked on reply icon
      if (uri.startswith("reply://")):
        print "resposta"
        return True
      #user clicked on retweet
      if (uri.startswith("retweet://")):
        print "retweet"
        return True      
      #user clicked on old RT
      if (uri.startswith("rt://")):
        script = """
           retweet('%s') 
        """ % uri.split("rt://")[1]
        self.browser.execute_script(script )
        return True
      #user clicked on favorite icon
      if (uri.startswith("fav://")):
        print "favorite"
        return True
    return False
  
  def post_content(self,tweets):
    post_tpl = Template(open('./templates/post.html', 'r').read())
    posts = ""
    for t in tweets:
      opt_text  = ""
      rt_class  = ""
      mod_class = ""
      owner = ""
      if (t.author.screen_name == self.myself):
        owner = "own"
        direction = "right"
      else:
        direction = "left"

      #retweeted
      if (hasattr(t,"retweeted_status")):
        rt_class = "rt"
        opt_text = "Retweeted by "+self.do_links("@"+t.author.name)
        t.author = t.retweeted_status.author
        t.text   = t.retweeted_status.text

      if (t.in_reply_to_status_id):
        opt_text = "In reply to "+t.in_reply_to_screen_name
        #if contains a mention to the user, use a different color
      if t.text.find("@"+self.myself) >= 0:
        mod_class = "re-me"
  
      post = post_tpl.substitute(
            pid       = t.id,
            photo     = t.author.profile_image_url,
            username  = t.author.screen_name,
            timeago   = timesince.timesince(t.created_at),
            owner     = owner,
            direction = direction,
            opt_text  = opt_text,
            rt_class  = rt_class,
            mod_class = mod_class,
            post      = self.do_links(t.text)
      )
      posts += post
    return posts

  def browser_content(self):
    base_tpl = Template(open('./templates/main.html', 'r').read())
    home_timeline     = self.t.twitter.home_timeline(count=50)
    mentions_timeline = self.t.twitter.mentions(count=50)
    home_tweets       = self.post_content(home_timeline)
    mentions_tweets   = self.post_content(mentions_timeline)
    doc = base_tpl.substitute(home_tweets = home_tweets, mentions = mentions_tweets)
    path = "file://"+os.getcwd()+"/templates/"
    self.browser.load_string(doc, "text/html", "utf-8", path)
    print doc

  def do_links(self,tweet):
    tweet = re.sub(r"(([\w]+?://[\w\#$%&~.\-;:=,?@\[\]+]*)(/[\w\#$%&~/.\-;:=,?@\[\]+]*)?)", lambda al: "<a href=\""+al.group(0)+"\">"+al.group(0)+"</a>",tweet)
    tweet = re.sub(r"@([a-zA-Z0-9]*)", lambda al: "<a href=\"http://twitter.com/"+al.group(1)+"\" title=\""+al.group(0)+"\" >"+al.group(0)+"</a>",tweet)
    tweet = re.sub(r"#([a-üA-Ü0-9]*)", lambda al: "<a href=\"http://search.twitter.com/"+al.group(0)+"\" title=\""+al.group(0)+"\">"+al.group(0)+"</a>",tweet)
    return tweet
    
  def quit(self, sender):
    gtk.main_quit()

#main
if __name__ == "__main__":
  b = Beezu()
  #gtk.gdk.threads_init()
  gtk.main()
