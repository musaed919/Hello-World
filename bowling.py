class Bowling(object):

    frame=0

    def __init__(self):
        self.score = []
        self.first_throw = True
        self.second_throw = True
        self.frame = 0

    def throw(self, knocked):
        if self.first_throw:
            self.score.append(knocked)
            if (knocked<10): #No Strike here
                self.first_throw = False
                self.second_throw = True
            else:#we have a Strike, so we don't need to go for a second throw
                self.score.append(0)
                self.inc_frame()

        elif (not self.first_throw) and self.second_throw:
            self.score.append(knocked)
            self.second_throw = False
            self.first_throw = True

    """to increment the frame by 1"""
    def inc_frame(self):
        self.frame+=1

    """We only use this when the next frames is done. To add the total to the spare frame."""
    def spare(self, frame_number):
        if ((self.score[frame_number*2]+self.score[(frame_number*2)+1])==10):
            total= self.score[(frame_number * 2) + 2] + self.score[(frame_number * 2) + 3]
            self.score[frame_number * 2] +=total

    """returns a frame's score"""
    def frame_score(self,frame_number):
        if (frame_number > self.frame):
            raise ValueError("out of range index")

        else:
            ret=self.score[frame_number*2]+self.score[(frame_number*2)+1]
        return ret

    """We only use this when the next two frames are done. To add the total to the strike frame."""
    def strike(self, frame_number):
       if(self.score[frame_number*2]==10):
           total = self.score[(frame_number * 2) + 2] + self.score[(frame_number * 2) + 3]
           total+= self.score[(frame_number * 2) + 4] + self.score[(frame_number * 2) + 5]
           self.score[frame_number*2]+=total

















