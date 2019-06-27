"""This api call is done over a loop and will retrieve data for 7 days for input given on key word search"""
"""raw file is created with all the attributes, for all the retrieved tweets based on the key word, mentioned in the doc in the social media analyitcs folder """
"""this code also creates two seperate file for hashtags and usermentions with Retweet and Engagement flags"""

#import os
import pandas as pd
import datetime
from nltk.sentiment import vader
#import re
import nltk
nltk.download('vader_lexicon')
import tweepy #https://github.com/tweepy/tweepy
sia= vader.SentimentIntensityAnalyzer()  
import os
from application import *
#import numpy as np
#from googletrans import Translator
#import emoji
#from Topics_election import pronoun_topicmodelling_hindi

#from Topics_LDA import lda_topicmodelling

class twitter_api(object):
    
    def __init__(self,string,consumer_key,consumer_secret,access_key,access_secret):
        self.string = string
        self.consumer_key=consumer_key
        self.consumer_secret=consumer_secret
        self.access_key=access_key
        self.access_secret=access_secret
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_key, self.access_secret)
        self.api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
        #datee = datetime.date.today() - datetime.timedelta(days=1)
        x= datetime.date.today() 
        y= x.strftime('%Y-%m-%d')
        c= datetime.date.today() - datetime.timedelta(days=1)
        d= c.strftime('%Y-%m-%d')
        e= datetime.date.today() - datetime.timedelta(days=2)
        f= e.strftime('%Y-%m-%d')
        g= datetime.date.today() - datetime.timedelta(days=3)
        h= g.strftime('%Y-%m-%d')
        i= datetime.date.today() - datetime.timedelta(days=4)
        j= i.strftime('%Y-%m-%d')
        k= datetime.date.today() - datetime.timedelta(days=5)
        l= k.strftime('%Y-%m-%d')
        m= datetime.date.today() - datetime.timedelta(days=6)
        n= m.strftime('%Y-%m-%d')
        o= datetime.date.today() - datetime.timedelta(days=7)
        p= o.strftime('%Y-%m-%d')
        q= datetime.date.today() - datetime.timedelta(days=8)
        r= q.strftime('%Y-%m-%d')
        s= datetime.date.today() - datetime.timedelta(days=9)
        t= s.strftime('%Y-%m-%d')
        u= datetime.date.today() - datetime.timedelta(days=10)
        v= u.strftime('%Y-%m-%d')
        
        w= datetime.date.today() - datetime.timedelta(days=11)
        x= w.strftime('%Y-%m-%d')
        
        
        #self.a=[v,t,r,p,n,l,j,h,f,d]
        #self.b=[t,r,p,n,l,j,h,f,d,y]
        #self.a=[x,v,t,r,p,n,l,j,h,f,d]
        #self.b=[v,t,r,p,n,l,j,h,f,d,y]
        #self.a=[l,j,h,f,d]
        #self.b=[j,h,f,d,y]
        #self.a=[h,f,d]
        #self.b=[f,d,y]
        #self.a=[f,d]
        #self.b=[d,y]
        self.a=[v,t]
        self.b=[t,r]
        
       
        self.all_tweet_list=[] 

    def run(self):
    
        def dateformat(temp):
            return(str(temp.day)+ "-" +str(temp.month)+ "-" +str(temp.year) + " " +str(temp.hour)+ ":" +str( temp.minute)+ ":" +str(temp.second))
        
        def get_list(status):
            y0=[]
            y1=[]
            y2=[]
            for i in range(len(status.entities['hashtags'])):
                y0.append(status.entities['hashtags'][i]['text'])
            for i in range(len(status.entities['user_mentions'])):
                y1.append(status.entities['user_mentions'][i]['screen_name'])
            for i in range(len(status.entities['urls'])):
                y2.append(status.entities['urls'][i]['expanded_url'])
            return (y0, y1, y2)    

        def sent(new_tweets):        
            new = new_tweets
            return [status._json["text"].strip() for status in new]

        def createTestData(search_string,date,nextdate):
            try:
                alltweets=[]
                print('Start Fetching')
                print(date,nextdate)
                new_tweets=self.api.search(q=search_string+" -filter:retweets",count=100,since=date,until=nextdate,result_type="recent")

                twees = sent(new_tweets)
                compound=[]
                senti=[]  
                for twee in twees:               
                    compound.append(sia.polarity_scores(twee)["compound"])

                    if compound[len(compound)-1]>0:
                        senti.append('positive')
                    elif compound[len(compound)-1]==0:
                        senti.append('neutral')
                    else:
                        senti.append('negative')    
                alltweets.extend(new_tweets)
                print (str(len(new_tweets))+"  new tweets")
                print (str(len(alltweets))+"  all tweets")
                
                oldest= (alltweets[-1].id -1)
                #while ((len(new_tweets) > 0)):
                while ((len(new_tweets) > 0) and (len(alltweets) < 1000)):
                    
                    #for i in range(0,1):
                    new_tweets=self.api.search(q=search_string+" -filter:retweets",count=100,max_id=oldest,since=date,until=nextdate,result_type="recent")
                
                    twees = sent(new_tweets)
                    for twee in twees:               
                        compound.append(sia.polarity_scores(twee)["compound"])
    
                        if compound[len(compound)-1]>0:
                            senti.append('positive')
                        elif compound[len(compound)-1]==0:
                            senti.append('neutral')
                        else:
                            senti.append('negative')    
              
                    alltweets.extend(new_tweets)
                    oldest=(alltweets[-1].id - 1)   
                    print (str(len(new_tweets))+ "  more new tweets")
                    print (str(len(alltweets))+"  all tweets")
                    
                    print("Great! We fetched "+str(len(alltweets))+" tweets with the term "+search_string + " for Date: " + str(alltweets[-1].created_at)+ " !!")
                    #print(len(alltweets))
                    new_tweet_list =  [{"id":status._json["id"],
                             "Date":dateformat(status.created_at),
                             "shifted_date":None,
                             "tweet":status._json["text"].strip(),
                             "RT Flag":None,
                             "language":status._json["lang"],
                             "user_id":status.user._json["id_str"],
                             "friends":status.user._json["friends_count"],
                             "favorited_status":status._json["favorited"],
                             "retweet_status":status._json["retweeted"],
                             "description":status.user._json["description"],###
                             "time_zone":status.user._json["time_zone"],
                             "place":status._json["place"],
                             "in_reply_to_screenname":status._json["in_reply_to_screen_name"],
                             "in_reply_to_status_id":status._json["in_reply_to_status_id"],
                             "in_reply_to_userid":status._json["in_reply_to_user_id"],
                             'is_quote_status':status._json['is_quote_status'],
                             #"label":None,
                             "favorite_count":status._json["favorite_count"],
                             "retweet_count":status._json["retweet_count"],
                             "user_screen_name":status.user._json["screen_name"],
                             "user_name":status.user._json["name"],
                             "user_location":status.user._json["location"],
                             "Verified":status.user._json["verified"],
                             "followers":status.user._json["followers_count"],
                             "Sources" : status._json["source"],
                             "status_count":status.user._json["statuses_count"],
                             "geo_enabled":status.user._json["geo_enabled"],
                             "Sentiment":senti[i],
                             "Profile_URL":status.user._json['profile_image_url'],
                             "Compound_score":compound[i],
                             "entities":get_list(status)} for i,status in enumerate(alltweets)] 
                    
                    self.all_tweet_list.extend(new_tweet_list)
                    
                    df = pd.DataFrame.from_dict(self.all_tweet_list)
        
                    hashtags=[]
                    user_mentions=[]
                    #translator = Translator()
                    #converted = []
                    comment = []
                    #compound_vernacular=[]
                    #senti_vernacular=[] 
                    impression=[]
                    #translation_flag = []
                    df['shifted_date'] =  pd.to_datetime(df['Date'])
                   
                    for index,row in df.iterrows():
                        hashtags.append(str(self.all_tweet_list[index]["entities"][0]))
                        user_mentions.append(str(self.all_tweet_list[index]["entities"][1]))
                        
                        if df.at[index, "Date"] == []:
                            df = df.drop([index])
                        if df.at[index, "Date"].find("-") ==-1:
                            df = df.drop([index])
                        if df.at[index, "tweet"] == []:
                            df = df.drop([index])
                        if str(type(df.at[index, 'tweet'])).find('str') ==-1:
                            df = df.drop([index])
                        if str(df.at[index, 'Date']).find("-") ==-1:
                            df = df.drop([index])   
                        if str(df.at[index, 'Verified']) != "False" and str(df.at[index, 'Verified']) != "True":
                            df = df.drop([index])
                        if str(df.at[index, 'favorited_status']) != "False" and str(df.at[index, 'favorited_status']) != "True":
                            df = df.drop([index])
                        
                        if df.at[index,'is_quote_status'] == False:
                            comment.append("No")
                        else:
                            comment.append("Yes")
                        
                        df.at[index,'shifted_date'] = pd.to_datetime(df['Date'][index]).strftime('%d-%m-%y %H:%M:%S')
                        df.at[index,'shifted_date'] = pd.to_datetime(df['shifted_date'][index]- datetime.timedelta(hours=7))
                        
                        if "RT @" in row["tweet"]:
                            df.at[index, "RT Flag"]= "Retweet"
                            df.at[index, "Engagements"]= 0
                        elif "@" in row["tweet"]:
                            df.at[index, "RT Flag"]= "Reply"
                            df.at[index, "Engagements"]= (row["favorite_count"] + row["retweet_count"])
                        else:
                            df.at[index, "RT Flag"]= "Original"
                            df.at[index, "Engagements"]= (row["favorite_count"] + row["retweet_count"])                
                    
                        '''
                        if df.at[index,'language'] != 'en':
                            try:
                               
                                inpt = emoji.demojize(df.at[index,'tweet'])
                                converted.append(translator.translate(inpt).tweet)
                                translation_flag.append('Successful')
                                
                            except:
                                converted.append(df.at[index,'tweet'])
                                translation_flag.append('failed')
                        else:
                            converted.append(df.at[index,'tweet'])
                            translation_flag.append('NA')
                    
                     
                        #for tweet in df['Translated_tweet']:               
                        
                        compound_vernacular.append(sia.polarity_scores(df.at[index,'tweet'])["compound"])
                        if compound_vernacular[len(compound_vernacular)-1]>0:
                            senti_vernacular.append('positive')
                        elif compound_vernacular[len(compound_vernacular)-1]==0:
                            senti_vernacular.append('neutral')
                        else:
                            senti_vernacular.append('negative')
                        '''
                        impression.append(int(0.1*(int(df.at[index,'followers']))))
            #==============================================================================
            # 
            #             if "RT @" in row["tweet"]:
            #                 df.at[index, "Reach"]= 0
            #             else:
            #                 df.at[index, "Reach"]= (row["Engagements"]+ int(df["Impressions"][index]))
            #         
            #==============================================================================
                    
                    df["Hashtags"] = hashtags
                    df["User_Mentions"] = user_mentions    
                    df['Comment'] = comment        
                    
                    '''
                    df['Translated_tweet'] = converted
                    df['Sentiment_vernacular'] = senti_vernacular
                    df['Compound_vernacualar'] = compound_vernacular
                    '''
                    df['Issue'] = str(self.string)  
                    
                    df['Influencers'] = df['Influencers'] = df['tweet'].str.extract("RT\s+(\@[^\:]*)", expand=False).fillna('Original')
                    df['Impressions'] = impression
                    #df['translation_flag'] = translation_flag
                    
                    '''
                    topic_object = pronoun_topicmodelling_hindi(df['tweet'])
                    topics = topic_object.run()
                    df['Topics'] = topics
                    '''
                    columns = ['id','Date','shifted_date','tweet','RT Flag','language','user_id',
                                  'friends','favorited_status','retweet_status',
                                  'description','time_zone','place','in_reply_to_screenname',
                                  'in_reply_to_status_id','in_reply_to_userid',
                                  'is_quote_status','favorite_count','retweet_count',
                                  'user_screen_name','user_name','user_location','Verified','followers','Sources','status_count',
                                  'geo_enabled','Profile_URL','Hashtags','User_Mentions','Sentiment','Compound_score',
                                  'entities','Comment','Issue',
                                  'Influencers','Impressions']
                    df = df[columns]
                    
                    df = df.drop(columns="entities")  
                    df.reset_index(inplace=True)

                    filename = os.path.join(application.instance_path, 'test', "search-"+str(self.string)+"-twitter_raw.xlsx")
                    #path = "/static/test/"+"search-"+str(self.string)+"-twitter_raw.xlsx"
                    df.to_excel(filename,header= True,index=False)
                    #df.to_excel("search-"+str(self.string)+"-twitter_raw.xlsx", header= True,index=False)
                    print(" Raw Data Fetching Done into excel !!!")   
                    df["Hashtags"] = df["Hashtags"].str.replace("'","")
                    
                    df["User_Mentions"] = df["User_Mentions"].str.replace("'","")
                    df["User_Mentions"] = df["User_Mentions"].str.replace("[","")
            
                    df["User_Mentions"] = df["User_Mentions"].str.replace("]","")
                    
                    
                    df['Hashtags'] = df['Hashtags'].astype(str).str.strip("[u']")
                    df['Hashtags'] = df['Hashtags'].str.strip("'")
                    df1 = df.drop('Hashtags', axis=1).join(df.Hashtags.str.split(expand=True)
                                .stack().reset_index(drop=True, level=1).rename('Hashtags'))
                    
                    df1['Hashtags'] =df1['Hashtags'].astype(str).str.strip("u'  ',")
                    if str(df1['Hashtags'].astype(str)).find("nan") ==-1:    
                        df1['Hashtags'] ="#"+ df1['Hashtags'].astype(str)
                    
                    #df1.to_excel("search-"+str(self.string)+"-twitter_HT.xlsx", header= True,index=False)
                    
                    df['User_Mentions'] = df['User_Mentions'].astype(str).str.strip("[u']")
                    df2 = df.drop('User_Mentions', axis=1).join(df.User_Mentions.str.split(expand=True)
                                 .stack().reset_index(drop=True, level=1).rename('User_Mentions'))
                    df2['User_Mentions'] = df2['User_Mentions'].astype(str).str.strip("u'  ',")
                    
                    df2['User_Mentions'] = "@"+df2['User_Mentions']
                    
                    df2['User_Mentions'] = df2['User_Mentions'].str.replace('@nan','')
                    df2['User_Mentions'] = df2['User_Mentions'].str.replace('@htTweets','')
                    
                    
                    #df2.to_excel('search-term.excel', header= True,index=False)
                    #df2.to_excel("search-"+str(self.string)+"-twitter_UM.xlsx", header= True,index=False) 
                    '''
                    df3 = df
                    df3['Topics'] = df.Topics.apply(pd.Series) \
                                 .merge(df, right_index = True, left_index = True) \
                                 .drop(["Topics"], axis = 1)
                    
                    df3.to_excel(str(self.string)+"Topics.xlsx")
                    ''' 
                    '''
                    lda_topic_object = lda_topicmodelling(df[df['language']=='en'],10,5)
                    lda_topics = lda_topic_object.run()
                    lda_df = pd.DataFrame()
                    lda_df = lda_topics 
                    
                    lda_df.to_excel(str(self.screen_name)+"_LDA_Topics")
                    '''
                print ("Great! We fetched "+ str(len(self.all_tweet_list)) +" tweets for the term "+self.string + " !!")

                    
            
            except Exception as e:
                print(e)
                print ("Sorry there was a n error for Range: " + str(i+1))
                new_tweet_list =  [{"id":status._json["id"],
                         "Date":dateformat(status.created_at),
                         "shifted_date":None,
                         "tweet":status._json["text"].strip(),
                         "RT Flag":None,
                         "language":status._json["lang"],
                         "user_id":status.user._json["id_str"],
                         "friends":status.user._json["friends_count"],
                         "favorited_status":status._json["favorited"],
                         "retweet_status":status._json["retweeted"],
                         "description":status.user._json['description'],###
                         "time_zone":status.user._json["time_zone"],
                         "place":status._json["place"],
                         "in_reply_to_screenname":status._json["in_reply_to_screen_name"],
                         "in_reply_to_statusid":status._json["in_reply_to_status_id"],
                         "in_reply_to_userid":status._json["in_reply_to_user_id"],
                         "is_quote_status":status._json["is_quote_status"],
                         #"label":None,
                         "favorite_count":status._json["favorite_count"],
                         "retweet_count":status._json["retweet_count"],
                         "user_screen_name":status.user._json["screen_name"],
                         "user_name":status.user._json["name"],
                         "user_location":status.user._json["location"],
                         "Verified":status.user._json["verified"],
                         "followers":status.user._json["followers_count"],
                         "Sources" : status._json["source"],
                         "status_count":status.user._json["statuses_count"],
                         "geo_enabled":status.user._json["geo_enabled"],
                         "Profile_URL":status.user._json["profile_image_url"],
                         "Sentiment":senti[i],
                         "Compound_score":compound[i],
                         "entities":get_list(status)} for i,status in enumerate(alltweets)]
                self.all_tweet_list.extend(new_tweet_list)
    
                
                
                
        for i in range(len(self.a)):
            createTestData(search_string = self.string,date = self.a[i],nextdate = self.b[i])
            
            
            
        