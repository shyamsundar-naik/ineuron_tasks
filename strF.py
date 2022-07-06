import logging
logging.basicConfig(filename="stringFunctions.log",level=logging.DEBUG ,format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class strQuestions:
    #Constructor
    def __init__(self):
        self.statement = "this is My First Python Programming class and i am learNINGpython string and its function"
        self.ex3List = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

    #Exercise 1 1st Question
    def ex1Question1(self):
        logging.info("Exercise 1 Question 1: try to extract data from index one to index 30 with a jump of 3")
        try:
            ans = self.statement[1:30:3]
            logging.info("Answer:")
            logging.info(ans)
        except Exception as e:
            logging.error(e)

        # Exercise 1 2nd Question
    def ex1Question2(self):
            logging.info("Exercise 1 Question 2: Try to reverse a string without using reverse string function")
            try:
                ans = self.statement[::-1]
                logging.info("Answer:")
                logging.info(ans)
            except Exception as e:
                logging.error(e)

        # Exercise 1 3rd Question
    def ex1Question3(self):
            logging.info("Exercise 1 Question 3: Try to split a string after conversion of entire string in upper case")
            try:
                statUpper = self.statement.upper()
                listAftSplit = statUpper.split()
                logging.info("Answer:")
                logging.info(listAftSplit)
            except Exception as e:
                logging.error(e)

        # Exercise 1 4th Question
    def ex1Question4(self):
            logging.info("Exercise 1 Question 4: Try to convert the whole string into lower case")
            try:
                logging.info("Answer:")
                logging.info(self.statement.upper())
            except Exception as e:
                logging.error(e)

        # Exercise 1 5th Question
    def ex1Question5(self):
            logging.info("Exercise 1 Question 5: Try to capitalize the whole string")
            try:
                logging.info("Answer:")
                logging.info(self.statement.capitalize())
            except Exception as e:
                logging.error(e)

        # Exercise 1 7th Question
    def ex1Question7(self):
            logging.info("Exercise 1 Question 7: Try to give an example of expandtab")
            try:
                example = "Good \tMorning \tStudents"
                logging.info("Answer:")
                logging.info(example.expandtabs())
            except Exception as e:
                logging.error(e)

        # Exercise 1 8th Question
    def ex1Question8(self):
            logging.info("Exercise 1 Question 8: Give an example of strip, lstrip and rstrip")
            try:
                logging.info("Answer:")
                example = "       iNeuron        "
                logging.info("String after applying strip : "+ example.strip())
                logging.info("String after applying lstrip: "+ example.lstrip())
                logging.info("String after applying rstrip: "+ example.rstrip())
            except Exception as e:
                logging.error(e)

        # Exercise 1 9th Question
    def ex1Question9(self):
            logging.info("Exercise 1 Question 9: Replace a string character by another character by taking your own example")
            try:
                logging.info("Answer:")
                rep = "I am looking at moon"
                aftRep = rep.replace('o', 'u')
                logging.info(aftRep)
            except Exception as e:
                logging.error(e)

        # Exercise 3 12th Question
    def ex3Question12(self):
            logging.info("Exercise 3 Question 12: Try to filter out all the string data")
            try:
                logging.info("Answer:")
                stringData = []
                for i in self.ex3List:
                    if type(i) == tuple or type(i) == list or type(i) == set:
                        for j in i:
                            if type(j) == str:
                                stringData.append(j)
                    elif type(i) == dict:
                        d = i
                        for k, v in d.items():
                            if type(k) == str:
                                stringData.append(k)
                            if type(v) == str:
                                stringData.append(v)

                logging.info(stringData)
            except Exception as e:
                logging.error(e)


sQ = strQuestions()
sQ.ex1Question1()
sQ.ex1Question2()
sQ.ex1Question3()
sQ.ex1Question4()
sQ.ex1Question5()
sQ.ex1Question7()
sQ.ex1Question8()
sQ.ex1Question9()
sQ.ex3Question12()
