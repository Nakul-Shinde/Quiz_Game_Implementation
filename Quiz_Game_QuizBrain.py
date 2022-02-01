#from Quiz_Game_Main import question_bank


class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        

    def next_question(self):
        
       # count=0
       # while count!=12:
            q_no= self.question_list.index(self.question_list[self.question_number])
            q_text=self.question_list[self.question_number]
           # print(q_text.text)
            print(f"\nQ.{q_no+1}: {q_text.text} (True/False)? ")
            u_answer=input()
            self.question_number+=1
            return(u_answer)
        
    def count_score(self,user_answer,data_answer):

         if user_answer==data_answer :
             answer='True'
             print("You got it right")
             print("The correct answer is:",data_answer)
            # print(f"Your current score is:{score}/{score}")
             return 1
         
         else:
             answer='False'
             print("You got it Wrong")
             print("The correct answer was:",data_answer)
             return 0
             #print(f"Your Final score is:{score}/{score+1}")

        
    def check_question_count(self):

        score=0
        repeat='True'
        while repeat=='True':
            user_answer=self.next_question() 
            if  self.question_number<13:
                print('question_number:',self.question_number)
                q_ans=self.question_list[self.question_number-1] 
                print(f"question_answer:{q_ans.answer}")
                val=self.count_score(user_answer, q_ans.answer)
                if val==1:
                    score+=1
                    print(f"Your current score is:{score}/{score}")
                    repeat='True'
                else:
                    print(f"Your Final score is:{score}/{score+1}")
                    repeat='False'
                    
            elif  self.question_number==12:
                print('question_number:',self.question_number)
                print("This is a last question")
                q_ans=self.question_list[self.question_number-1] 
                print(f"question_answer:{q_ans.answer}")
                val=self.count_score(user_answer, q_ans.answer)
                if val==1:
                    score+=1
                    print(f"Your current score is:{score}/{score}")
                    repeat='True'
                else:
                    print(f"Your Final score is:{score}/{score+1}")
                    repeat='False'
                
                print('Game is over')         
                break

