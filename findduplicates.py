class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentfreq=defaultdict(list)
        duplicated=[]
        for path in paths:
            mainpath=path.split(" ")
            root=mainpath[0]
            files=mainpath[1:]
            newfile=""
            for index in range(len(files)):
                file=files[index]
                braceidx=file.index("(")
                newfile=root+"/"+file[:braceidx]
                contentfreq[file[braceidx:]].append(newfile)
        for content in contentfreq:
            if len(contentfreq[content]) > 1:
                duplicated.append(contentfreq[content])
        return duplicated
