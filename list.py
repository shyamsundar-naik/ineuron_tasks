#
import logging
logging.basicConfig(filename="listFunctions.log",level=logging.DEBUG ,format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class listQuestions:
    #creating the constructor
    def __init__(l1):
        logging.info("**************************************We are having new list formed*************************************")
        l1.ex2List = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
        l1.ex3list = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3": "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
    #Exercise 2 1st Question
    def ex2Question1(l1):
        logging.info("Exercise 2 Question 1: Try to reverse a list")
        try:
            reverse = l1.ex2List[::-1]
            logging.info("Answer : ")
            logging.info(reverse)
        except Exception as e:
            logging.error(e)

    # Exercise 2 3rd Question
    def ex2Question3(l1):
        logging.info("Exercise 2 Question 3: try to access 456")
        try:
            access256 = l1.ex2List[5][1]
            logging.info("Answer : " )
            logging.info(access256)
        except Exception as e:
            logging.error(e)

    # Exercise 2 4th Question
    def ex2Question4(l1):
        logging.info("Exercise 2 Question 4: try to extract only a list collection form list l")
        try:
            logging.info("Answer:")
            for i in l1.ex2List:
                if type(i) == list:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

    # Exercise 2 5th Question
    def ex2Question5(l1):
        logging.info("Exercise 2 Question 5: Try to extract \"sudh\"")
        try:
           val = l1.ex2List[8]['key1']
           logging.info("Answer : " + val)
        except Exception as e:
            logging.error(e)

    # Exercise 3 5th Question
    def ex3Question5(l2):
        logging.info("Exercise 3 Question 5: Try to extract all the list entity")
        try:
            a = []
            for i in l2.ex3list:
                if type(i) == list:
                    a.append(i)
            logging.info("Answer : ")
            logging.info(a)
        except Exception as e:
            logging.error(e)

# Exercise 5 3rd Question
    def appendEnd(l1,data, element):
        logging.info("Exercise 5 Question 3: Try to write a function which is a replica of list append")
        try:
            data = data + [element]
        except Exception as e:
            logging.error(e)
        return data

lQ = listQuestions()
lQ.ex2Question1()
lQ.ex2Question3()
lQ.ex2Question4()
lQ.ex2Question5()
lQ.ex3Question5()
try:
    dat = lQ.appendEnd([4,5,6])
    logging.info("Answer : " + dat)
except Exception as e:
    logging.error(e)

try:
    dat = lQ.appendEnd([4,5,6],12)
    logging.info("Answer : ")
    logging.info(dat)
except Exception as e:
    logging.error(e)

