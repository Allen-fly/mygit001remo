#coding=utf-8
class Test:
    @classmethod
    def open_schema(cls,path):
        with open(path,'r')as fp:
            lines = fp.readlines()
            out_string = ''
            for line in lines:
                out_string += line.rstrip()
        return out_string

    @classmethod
    def write_text(cls,schema):
        with open('test.txt','w') as fp:
            fp.write(schema)
    @classmethod
    def analyze_data(cls,data):
        if isinstance(data, dict):
            for k, v in data.items():
                cls.analyze_data(v)
        elif isinstance(data, (list, tuple)):
            for i in range(len(data)):
                cls.analyze_data(data[i])
        else:
            contents = data
            return contents

if __name__=='__main__':
    content = Test.open_schema(r'D:\pyproject\project001\test.schema')
    content = Test.analyze_data(content)
    print content