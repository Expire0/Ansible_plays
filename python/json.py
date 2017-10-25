#json example 

credd = "<placeholder>"

cred = str(sec.b64decode('<base64code>'),"utf-8")
 r = requests.get('https://<url>/%s' % (mas1), auth=('<username>', cred))

data =json.loads(r.text)
            
for k,v in data[0].items():
    if '<key value>' in k:
        print(v)
