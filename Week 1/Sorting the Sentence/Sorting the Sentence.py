class Solution(object):
    def sortSentence(self, s):

        slist = s.split()
        
        for i in range(len(slist)-1, 0, -1):
            for j in range(i):
                if slist[j][-1] > slist[j+1][-1]:
                    temp = slist[j]
                    slist[j] = slist[j+1]
                    slist[j+1] = temp
            slist[i] = slist[i].rstrip(slist[i][-1])
        slist[0] = slist[0].rstrip(slist[0][-1])
        
        return str(' '.join(slist))
                
  