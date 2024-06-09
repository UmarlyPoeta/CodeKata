class User:
    def __init__(self):
        self.ranks = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
        self.rank = self.ranks[0]
        self.progress =0
        
    
    def inc_progress(self,rank):
        try:
            if rank not in self.ranks:
                raise Exception()

            a = self.ranks.index(self.rank)
            b = self.ranks.index(rank)
            if b>a:
                diff = abs(b-a)
                self.progress = self.progress + (diff ** 2 * 10)
            elif self.rank == rank:
                self.progress +=3
            elif a-1==b and a-1>=0:
                self.progress +=1
            
            if self.progress >=100 and self.rank !=8:
                try:
                    self.rank = self.ranks[self.ranks.index(self.rank)+(self.progress //100)]
                except:
                    self.rank = 8
                self.progress = self.progress%100
            if self.rank==8:
                self.progress = 0
        except ValueError:
            pass

                    