#read 

class DataBase(object):
    # def __init__(self):
        
        
    def getIPs(self, file_path: str) -> list[str]:
        ip_list = []
        with open(file_path, "r") as file:
            for line in file:
                if ("#" in line): 
                    line = line.split('#', 1)[0]
                    if(len(line) == 0): continue
                ip_list.append(line.strip())
        
        print(str(ip_list))