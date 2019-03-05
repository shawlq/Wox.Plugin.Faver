import os, json

class Data:
    DATA_PREFIX = r"./.db"

    def __db_path(cls, k):
        return os.path.join(cls.DATA_PATH, k + ".json")

    @classmethod
    # void
    def Set(cls, k, d):
        with open (cls.__db_path(k), "w") as f:
            f.write(json.dumps(d))

    @classmethod
    #return list of url [url, url]
    def Get(cls, k):
        if not os.path.exits(cls.__db_path(k)):
            return set()

        with open (cls.__db_path(k), "r") as f:
            infos = f.read()
            return json.loads(infos) if infos else set()

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
        os.remove(ls.__db_path(k))

class Faver:

    @classmethod
    def Alert(cls, title, content):
        from wox import WoxAPI
        WoxAPI.show_msg(title, content, r"./Images/pic.png")

    @classmethod
    def Tag(cls, para):
        args = para.split(" ")
        if len(args) < 2: # at least: label and url
            return False

        labels = args[:-1]
        url = arg[-1]
        for label in labels:
            urls = Data.Get(label)
            urls.add(url)
            Data.Set(label, urls):
            cls.Alert("Success Tag!", "%s => %s"%(label, url))
        return True

    @classmethod
    def Untag(cls, para):
        args = para.split(" ")
        if len(args) < 2:
            return False

        label = args[0]
        url = arg[-1]

        urls = Data.Get(label)
        if url in urls:
            urls.remove(url)

        if len(urls) != 0:
            Data.Set(label, urls)
        else:
            Data.Delete(label)
        cls.Alert("Success Untag!", "%s => %s"%(label, url))
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
        