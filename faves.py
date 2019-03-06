import os, json
from log import logger

class Data:
    DATA_PREFIX = r"./data"

    @classmethod
    def __db_path(cls, k):
        return os.path.join(cls.DATA_PREFIX, k + ".json")

    @classmethod
    # void
    def Set(cls, k, d):
        logger.debug("Data.Set, k:%s, d:%s", k, d)
        with open (cls.__db_path(k), "w") as f:
            f.write(json.dumps(list(d)))

    @classmethod
    #return list of url [url, url]
    def Get(cls, k):
        logger.debug("Data.Get, k:%s",k)
        if not os.path.exists(cls.__db_path(k)):
            return set()

        with open (cls.__db_path(k), "r") as f:
            infos = f.read()
            return set(json.loads(infos)) if infos else set()

    @classmethod
    #return list of key [key1, key2]
    def GetChildren(cls, part_of_k):
        found = []
        files = os.listdir(cls.DATA_PREFIX)  
        for f in files:
            if(os.path.isfile(f)):
                key_name = os.path.splitext(f)[0]
                if key_name.find(part_of_k) >= 0:
                    found.append(key_name)
        return found

    @classmethod
    #return list of key [key1, key2]
    def GetChildren(cls):
        found = []
        files = os.listdir(cls.DATA_PREFIX)  
        for f in files:
            if(os.path.isfile(f)):
                key_name = os.path.splitext(f)[0]
                found.append(key_name)
        return found

    @classmethod
    def Delete(cls, k):
        os.remove(cls.__db_path(k))

class Faver:

    @classmethod
    def Alert(cls, title, content):
        # can not call frequently, will crash
        from wox import WoxAPI
        WoxAPI.show_msg(title, content, r"./Images/pic.png")

    @classmethod
    def Tag(cls, para):
        args = para.split(" ")
        if len(args) < 2: # at least: label and url
            return False

        labels = args[:-1]
        url = args[-1]
        for label in labels:
            urls = Data.Get(label)
            logger.debug("Tag, get urls:%s", urls)
            urls.add(url)
            logger.debug("Tag, new urls:%s", urls)
            Data.Set(label, urls)    
        cls.Alert("Success Tag!", "%s is taged"%url)
        return True

    @classmethod
    def Untag(cls, para):
        args = para.split(" ")
        if len(args) < 2:
            return False

        label = args[0]
        url = args[-1]

        urls = Data.Get(label)
        if url in urls:
            urls.remove(url)

        if len(urls) != 0:
            Data.Set(label, urls)
        else:
            Data.Delete(label)
        cls.Alert("Success Untag!", "TAG %s is removed"%label)
        return True
        
    @classmethod
    def List(cls, para):
        args = para.split(" ")
        if len(args) == 0:
            return set()

        found = Data.Get(args[0])
        if len(args) == 1:
            return found

        for arg in args[1:]:
            if len(found) == 0:
                break
            urls = Data.Get(arg)
            found = found & urls

        return found


    @classmethod
    def FindLabels(cls, para):
        #args = para.split(" ")
        return []
        
    @classmethod
    def Click(cls, url):
        import webbrowser
        webbrowser.open(url)
        