from __future__ import print_function
from future.standard_library import install_aliases

install_aliases()

import json
import os
import smtplib

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r



def makeWebhookResult(req):
    if req.get("result").get("action") == "fallback.fallback-custom":
        result = req.get("result")
        parameters = result.get("parameters")

        Addr = parameters.get("email")
        AddrB =''.join(Addr)

        Countr = parameters.get("geo-country")
        CountrB =''.join(Countr)
        
        GvenNam = parameters.get("given-name")
        GvenNamB =''.join(GvenNam)
        
        LastName = parameters.get("last-name")
        LastNameB = ''.join(LastName)
        
        #LastNme = parameters.get("last-name")
        
        #ContentM = parameters.get("any")
        #hw="Country:"

        #Pr = ''.join(Progr)
        # Ti = ''.join(tme)
        #Le = ''.join(Levp)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        #server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
        server.starttls()
        server.login("testapiblcu@gmail.com", "Testapi2017")

        msg = "A user need further help at BLCU online Bot -> \nGiven Name: "+str(GvenNamB)+" "+str(LastNameB) +"\nE-mail: " +str(AddrB)+"\nCountry: "+str(CountrB)+"\nProgram Interest: BLCUOnline \nStarting Date: Anytime" 
        #+str(ContentM) 
        server.sendmail("testapiblcu@gmail.com", "testapiblcu2017@gmail.com", msg)
        server.quit()




    speech = "Thank you for your interest and providing required info; Soon We will get in contact with you Otherwise you can contact us Directly to :=>WechatID: richyingjie  Or By E-mail Address:  admissions@blcuchinese.com"


    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        #"contextOut": [[{"name":"requestedhuman ", "lifespan":5}],
        "source": "blcualertmade"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
