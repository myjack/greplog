# -*- coding: utf-8 -*-

import time
import re
import os

class Greplog():

    def write_log(self,filename, content):
        file_dir = "errorlog/"+time.strftime('%Y%m%d',time.localtime(time.time()))
        if not os.path.isdir(file_dir):
            os.makedirs(file_dir)
        with open(file_dir + filename, 'a+') as f:
            f.write(content)

    def grep_log(self,file_path, start_log_reg, end_log_reg):
        file = open(file_path)
        while True:
            file.tell()
            line = file.readline()
            print line
            result = re.match(start_log_reg, line)
            if result == None : continue
            file_name =  "/errorlog-" + time.strftime('%H%M%S',time.localtime(time.time()))
            self.write_log(file_name, line)
            while True:
                file.tell()
                next_line = file.readline()
                if next_line == '' or next_line.strip() == '':continue
                match_end_result = re.match(end_log_reg, next_line)
                if match_end_result != None : break
                else:
                    print next_line
                    self.write_log(file_name, next_line)

if __name__ == '__main__' :
    start_log_reg = '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} ERROR'
    end_log_reg = '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} (DEBUG|INFO){1}'
    obj = Greplog()
    obj.grep_log('a.log', start_log_reg, end_log_reg)

