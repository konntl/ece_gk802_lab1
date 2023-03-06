import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

def webserversoftware(k,v):
    if k == 'Server':
        print("Web Server Software : ",v)
    else : pass

#this is a comment 

url = input("enter URL : ")

with requests.get(url) as response:
    for k,v in response.headers.items():
        print("{} : {}".format(k,v))
    print('\n')
    for k,v in response.headers.items():
        webserversoftware(k,v)
    print(response.cookies)
    for k,v in enumerate(response.cookies):
        print('Cookies : ')
        print('{} : {}'.format(v.name,v.expires))

    
    
    
