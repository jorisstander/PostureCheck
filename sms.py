from twilio.rest import Client

SID = 'Your_SID_code' #Todo found on twilio after creating a trial account
Auth_Token = 'Your_auth_token' #Todo found on twilio after creating a trial account

def sentsms():
    cl = Client(SID, Auth_Token)
    print('sending sms')

    #Todo add your verified number to parameter to='number' - found on twilio after creating a trial account
    #Todo add Twilio it's verified number to parameter from='number' - found on twilio after creating a trial account
    cl.messages.create(body='You need to fix your posture, it has been bad for 5 minutes!', from_='twilio_number', to='Your_verified_number')
