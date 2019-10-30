import json
import unittest
import HTMLTestRunner
from distutils.command.config import config
 
class update_json_info(unittest.TestCase):
    def setUp(self):
        self.json_path='C:\\Users\\qiuc2\\Desktop\\workplan\\environment.json'
        self.new_json_path='C:\\Users\\qiuc2\\Desktop\\workplan\\environment88.json'
        config={
            "slot":" ",
            "cluster_num_for_vvxrail":"",
            "current_executed_slot":"",
            "current_executed_cluster":""           
            }
    
    def  test_check_json_value(self,dic_json,k,v):
        print(self.json_path)       
        if isinstance(dic_json,dict):         
            for key in dic_json:
                if key == k:
                    dic_json[key] = v
                elif isinstance(dic_json[key],dict):
                    self.test_check_json_value(dic_json[key],k,v)
 
    def  test_change_json_info(self):
        with open(self.json_path) as f:
            json_info=json.load(f)
        f.close()
        self.test_check_json_value(json_info,'slot','1')
        print(json_info)
        self.test_check_json_value(json_info,'cluster_num_for_vvxrail','')
        self.test_check_json_value(json_info, 'current_executed_slot', '')
        self.test_check_json_value(json_info, 'current_executed_cluster', '')
        with open(self.new_json_path,'w') as f:
            f.write(json.dumps(json_info))
        f.close()
 
if __name__=='__main__':
    suit=unittest.TestSuite()
    suit.addTest(update_json_info('test_change_json_info'))
    filename="C:\\Users\\qiuc2\\Desktop\\test\\test1.html"
    fb=open(filename,'wb')
    runer=HTMLTestRunner.HTMLTestRunner(stream=fb,title='VxRail Automation Test Report',description='Report_description')
    runer.run(suit)
    
    
    
    
    
    
    