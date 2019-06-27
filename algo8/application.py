from flask import Flask, request, render_template,redirect

app = application = Flask(__name__)

#from twitter_API_scrapper_election import twitter_api

#from Twitter_streaming_on_time_election import streaming_api_time
#from twitter_handles_api_election import Twitter_handles
#from premium_api import twitter_api
import pandas as pd
from twitter_class import *
'''
consumer_key='hbwjipkBG7tP0ohtia7hCAQDB'
consumer_secret='0biMHiFkJNz5nFNVE13kcpoHjBW3qJ7F4pAxgh7wVKmHTqYAoh'
access_key='112166849-VsUzdcK2aQXPAd5VVg77q608ESOCx4R1QABitR6J'
access_secret='LaHCSMiMNsoP6BMjrNxUFXKH2Fn6KWmMTXCeYb21QQKh1'


consumer_key='V2qwIFQFkq29mlZdqfXqcwfdP'
consumer_secret='RggvK6C70YbveYdlpgogoVc7Okx6AkrdWtdguvWPvZ9CyY52ZF'
access_key='2252707229-f1mtDeug3TjvkAKA9PHqa7LW6lqdRqV12kGeid0'
access_secret='BALeMDezc3llku7YiAcHUOEudlWcJo4Kc8fJW4zYDjPM3'


consumer_key='oqyhKtrSrCyYfAjYdhLdNrEOh'
consumer_secret='8qHWSiLfV6vNot0gkltG2uGkJwJhExedmBVRKwAfXnSZOZSS4I'
access_key='796928120741761024-vG8nQrFyhzs28SchXZKD3Fh4XO1yQru'
access_secret='72siJ2y6SZWkUnA2OeRRWohxO3lbxTlEWFBZo7g3heSv7'



#akash

consumer_key='HK92sfktQdQONb2lh822rsL3g'
consumer_secret='l9ZIihb9ATXOm8B1RxoYCUgy4Su7ODXKVuSmOFOJrKLYC3aBb3'
access_key='626504527-7vQwkB06EF4EsZ9UnKAVTKULWYj6r0jDvvKBb0VS'
access_secret='R6HUQmqlKuX9yvi4HdZtzFC7eOn7VZUavgca6Re9y8hAb'

'''
#bramhesh
consumer_key='FEIq9oOX5gY2Uk80cLjCuaLTu'
consumer_secret='l5CVTE0fqsqIrN9e0yZXvNjUHKY5WGK8rbbqp4Iuy5HrjwF9RW'
access_key='370162760-57o86rED5Xh2u2TGRMGlD127fXHRrVQBFTRNmzPR'
access_secret='FFKt4z4dVpFJ50kiRMCZXOGCPakMuxGm4ks91VAQBF3wg'

'''
#shivam
consumer_key='A5g4VgiHFN5UfKM3ia0j44o7t'
consumer_secret='bdp8I7OiZhpMhvogDH70VbQC1RDILmjcHorE5VEYfVK93XxsgG'
access_key='1130070993953730561-ZgUX00Eb8TXsFetw9BzIcHnnrp0mCl'
access_secret='rtoJulbeRq5hZDU6iLXiPH30fR3smBfLVNnHJ3BURJbVw'
'''


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/ml_ai')
def ml_ai():
    return render_template('ml_ai.html')

@app.route('/manufacturing')
def manufacturing():
    return render_template('manufacturing.html')

@app.route('/banking')
def banking():
    return render_template('banking.html')

@app.route('/banking_case')
def banking_case():
    return render_template('bank_case.html')

@app.route('/healthcare')
def healthcare():
    return render_template('healthcare.html')

@app.route('/insurance')
def insurance():
    return render_template('insurance.html')

@app.route('/retail')
def retail():
    return render_template('retail.html')

@app.route('/retail_case')
def retail_case():
    return render_template('retail_case.html')

@app.route('/telecom')
def telecom():
    return render_template('telecom.html')

@app.route('/telecom_case')
def telecom_case():
    return render_template('telecom_case.html')

@app.route('/government')
def government():
    return render_template('government.html')

@app.route('/custom_ai')
def custom_ai():
    return render_template('custom_ai.html')

@app.route('/oil_natural_gas')
def oil_natural_gas():
    return render_template('oil_natural_gas.html')

@app.route('/loc8')
def loc8():
    return render_template('loc8.html')

@app.route('/loc8_case')
def loc8_case():
    return render_template('loc8_case.html')

@app.route('/vision8')
def vision8():
    return render_template('vision8.html')

@app.route('/opini8')
def opini8():
    return render_template('opini8.html')

@app.route('/opini8_case')
def opini8_case():
    return render_template('opini8_case.html')

@app.route('/career')
def career():
    return render_template('careers.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/api_twitter/<key>')
def api_twitter(key):
    #print("fetching from twitter")
    keyword = str(key)
    Object4 = twitter_api(keyword, consumer_key, consumer_secret, access_key, access_secret)
    Object4.run()
    return redirect("/")


if __name__ == '__main__':
    app.run()
