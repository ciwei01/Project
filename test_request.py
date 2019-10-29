import requests
import json
import types

#获取key的值，传入比对值       
def verify_value(data,key,test_value):    
    actual_value=get_value(data,key)
    if actual_value==test_value:
        print('keys value equal expected value')
#         return Ture
    else:
        print('keys value not equal expected value')
                       
def get_value(data,key):
    for k,v in data.items():
        if k == key:
            return v
        else:
            if type(v).__name__=='dict':
                ret=get_value(v,key)
                return ret
    
            
if __name__=="__main__":
    response=requests.get('http://10.62.91.153:88/first_run_json/4_7_xxx/1/1/4/download',verify=False)
    data=json.loads(response.text)
    print(type(data))
    verify_value(data, 'netmask', '255.255.0.0')
    
    
    
    
    
    
    