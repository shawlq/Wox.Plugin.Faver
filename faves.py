import os, json

class Data:
    DATA_PREFIX = r"./data"

    @classmethod
    def __db_path(cls, k):
        return os.path.join(cls.DATA_PREFIX, k + ".json")

    @classmethod
    def Exists(cls, k):
        return os.path.exists(cls.__db_path(k))

    @classmethod
    # void
    def Set(cls, k, d):
        with open (cls.__db_path(k), "w") as f:
            f.write(json.dumps(list(d)))

    @classmethod
    #return list of url [url, url]
    def Get(cls, k):
        with open (cls.__db_path(k), "r") as f:
            infos = f.read()
            return set(json.loads(infos)) if infos else set()

    @classmethod
    #return list of key [key1, key2]
    def GetChildren(cls, part_of_k):
        import glob
        likely = []
        precise = None
        files = glob.glob(r'%s/*%s*.json'%(cls.DATA_PREFIX, part_of_k))
        for f in files:
            filename, _ = os.path.splitext(os.path.split(f)[-1])
            if(part_of_k == filename):
                precise = filename
            elif (filename.startswith(part_of_k)):
                likely.insert(0, filename)
            else:
                likely.append(filename)

        return precise, likely

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
    def Tag(cls, args):
        labels = args[:-1]
        url = args[-1]
        for label in labels:

            urls = set() if not Data.Exists(label) else Data.Get(label)
            urls.add(url)
            Data.Set(label, urls)    
        cls.Alert("Success Tag!", "%s is taged"%url)

    @classmethod
    def Untag(cls, para):
        args = para.split(" ")
        if len(args) < 2:
            return False

        label = args[0]
        url = args[-1]

        if not Data.Exists(label):
            return True
        
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
        labels = para.split(" ")
        if len(labels) == 0:
            return False, "At least one label", list(), list()

        for label in labels[:-1]:
            if not Data.Exists(label):
                return False, "Not found %s"%label, list(), list()

        precise, likely = Data.GetChildren(labels[-1])
        if precise is None and len(likely) == 0:
            return False, "Not found %s"%(labels[-1],), list(), list()

        common_urls = None
        for label in labels[:-1]:
            urls = Data.Get(label)
            common_urls = common_urls & urls if common_urls is not None else urls
            if len(common_urls) == 0:
                return True, "", list(), list()

        precise_labels = labels[:-1]
        no_more = list()
        found = list()
        count = 0
        if precise is not None:
            urls = Data.Get(precise)
            precise_common = common_urls & urls if common_urls is not None else urls      
            found.append([para, precise_common])
            count = 100 # if found precisely, likely no need to show details

        for like in likely:
            if like in precise_labels:
                continue

            k = " ".join(precise_labels + [like])
            if count > 20:
                no_more.append([k, "type label '%s' to show more"%like])
                continue

            urls = Data.Get(like)
            like_common = common_urls & urls if common_urls is not None else urls
            size = len(like_common)
            if (size == 0):
                continue

            count += size
            found.append([k, like_common])
        return True, "", found, no_more


    @classmethod
    def FindLabels(cls, para):
        #args = para.split(" ")
        return []
        
    @classmethod
    def Click(cls, url):
        import webbrowser
        webbrowser.open(url)
        