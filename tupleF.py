import logging
logging.basicConfig(filename="tupleFunctions.log",level=logging.DEBUG ,format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class tupleQuestions:
    #Constructor
    def __init__(self):
        self.ex3List = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

    # Exercise 3 5th Question
    def ex3Question5(self):
            logging.info("Exercise 3 Question 5: Try to extract all the tuples entities")
            try:
                a = []
                logging.info("Answer : ")
                for i in self.ex3List:
                    if type(i) == tuple:
                        logging.info(i)
            except Exception as e:
                logging.error(e)

tQ = tupleQuestions()
tQ.ex3Question5()
