class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        my_dict={}
        output=[]
        for i in range(len(cpdomains)):
            dom=cpdomains[i].split(" ")
            rep=int(dom[0])
            second=dom[1].split(".")
            for j in range(len(second)):
                cur=(".").join(second[j:])
                if cur in my_dict.keys():
                    my_dict[cur]+=rep
                else:
                    my_dict[cur]=rep
        for key in my_dict.keys():
            out=""
            out+=str(my_dict[key])+" "+key
            output.append(out)
        return output
