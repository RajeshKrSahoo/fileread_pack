import pytest
import filex
fileread = filex.filex()
class TestJsonLoad():
    def test_jsonread(self):
        ''' This method validate get file name functionality'''
        print ("Enter into test_jsonread fun.")
        assert fileread.jsonread("Data_utils.json")

 

    def test_yaml(self):
        ''' This method validate get file name functionality'''
        print ("Enter yamls")
        assert fileread.yaml("sample.yaml")
        
    def test_confRead(self):
        assert  fileread.confRead("config.cfg")