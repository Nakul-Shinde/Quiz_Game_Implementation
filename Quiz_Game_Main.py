from Quiz_Game_Data import question_data
from Quiz_Question_Model import Question
from Quiz_Game_QuizBrain import QuizBrain


question_bank=[]

for i in question_data:
    question_bank.append(Question(i['text'],i['answer']))
    
    
    
qb=QuizBrain(question_bank)

qb.check_question_count()






    
    
    
    
    
    