import logging
logging.basicConfig(filename="dictionaryFunctions.log",level=logging.DEBUG ,format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class dicQuestions:
    #Constructor
    def __init__(self):
        self.ex2List = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
        self.ex3List = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

    #Exercise 2 6th Question
    def ex2Question6(self):
        logging.info("Exercise 2 Question 6: Try to list all the key in dict element avaible in list")
        try:
            dict = self.ex2List[8]
            keys1 = list(dict.keys())
            logging.info("Answer : ")
            logging.info(keys1)
        except Exception as e:
            logging.error(e)

    #Exercise 2 7th Question
    def ex2Question7(self):
        logging.info("Exercise 2 Question 7: Try to extract all the value element form dict available in list")
        try:
            dict = self.ex2List[8]
            values = list(dict.values())
            logging.info("Answer : ")
            logging.info(values)
        except Exception as e:
            logging.error(e)

    #Exercise 3  4th Question
    def ex3Question4(self):
        logging.info("Exercise 3 Question 4: Try to extract all the dict entities")
        try:
            logging.info("Answer : ")
            for i in self.ex3List:
                if type(i) == dict:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

    #Exercise 3  11th Question
    def ex3Question11(self):
        logging.info("Exercise 3 Question 4: Try to find out number of keys in dict element")
        try:
            logging.info("Answer : ")
            logging.info(len(self.ex3List[4]))
        except Exception as e:
            logging.error(e)

dQ = dicQuestions()
dQ.ex2Question6()
dQ.ex2Question7()
dQ.ex3Question4()
dQ.ex3Question11()
