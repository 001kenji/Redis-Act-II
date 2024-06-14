import redis

r= redis.StrictRedis(host='localhost',port=6379,db=0)
def HyperlogManipulation(count=False,key=None,val=None):
    if count:
        result = r.pfcount(key)
        print('\n Count data from hyperloglog: ',result)
    else:
        result = r.pfadd(key,*val)
        print('\n Added values to hyperloglogs: ',result)



logval = {'Joe','Mack','Leu','Hestile',"Meredith","Kiston","Gesto"}
HyperlogManipulation(count=False,key='MyLog',val=logval)
HyperlogManipulation(count=True,key='MyLog')


def PubSubManipulation(sub=False,unsub=False,publish= False,key=None,val=None):
    if sub:
        result = r.pubsub().subscribe(key)
        print('\n Subscribed to: ',key, " : status ",result)
        for message in r.pubsub().listen():
            channel  = message['channel'].decode('utf-8')
            data = message['data'].decode('utf-8')
            print(f"Received message on channel '{channel}': {data}")
    elif unsub:
        result = r.pubsub().unsubscribe(key)
        print('\n Unsubscribed to: ',key," : status ",result)
    elif publish:
        result = r.publish(key,val)
        print('\n messaged: ',val, " :to :",key," : recievers :",result)
    

PubSubManipulation(sub=True,key='MyChannel')
PubSubManipulation(publish=True,key='MyChannel',val='am the message 1')
PubSubManipulation(unsub=True,key='MyChannel')




















