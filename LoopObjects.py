"""
This class provides a basic interface for implementing a While Loop Object. The class has four methods:
- isFinished: Returns False if there are still iterations left to be done.
- start: Runs the full loop. The user should implement their calculation in a subclass.
- step: Steps through one iteration of the loop. The user should implement their calculation in a subclass.
- clear: Clears the stored work unit/other data.

This class contains the following attributes:
- args: the iterable to iterate through
- i: The current iteration value
- first: The starting value of the loop
- end: The end value of the loop
- op: The operater used to do comparison if the loop should continue
- incr: The value by which the loop should increment/decrement
- calc: The calculated value of the current iteration
"""

class Loop:
    
    def __init__(self,*args,op="<",i=0,end=1,incr=1,func=lambda *arg : print(*arg)):
        self.i= i
        self.first= i
        self.end= end
        self.op= op
        self.incr= incr
        self.calc= 0
        self.func = func
        self.args = args
        self._result = None
        self.string_representation = str(f"i= {self.i}, condition= While {self.first} {self.op} {self.end} , increment: {self.incr}") 

    def getResult(self):
        return self._result

    def __str__(self):
        return self.string_representation 

    @property
    def i(self):
        return self._i

    @i.setter
    def i(self,i):
        if type(i) != int:
            raise TypeError("i Type must be int: override this in a subclass")
        else:
            self._i = i
         
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self,end):
        if type(end) != int:
            raise TypeError("end Type must be int: override this in a subclass")
        else:
            self._end = end
    
    @property
    def incr(self):
        return self._incr

    @incr.setter
    def incr(self,incr):
        if type(incr) != int:
            raise TypeError("increment Type must be int: override this in a subclass")
        else:
            self._incr = incr
    
    @property
    def op(self):
        return self._op

    @op.setter
    def op(self,op):
        if op == True:
            self._op = "True"
        elif op == False:
            self._op = "False"
        elif op not in ["<","<=",">",">=","==","True","False"]:
            raise ValueError("Incorrect Operator")
        else:   
            self._op = op
        
    #methods
    def isFinished(self):
        if self.op == "<":
            return self.i >= self.end
        elif self.op == "<=":
            return self.i > self.end
        elif self.op == ">":
            return self.i <= self.end
        elif self.op == ">=":
            return self.i < self.end
        elif self.op == "==":
            return self.i != self.end  
        elif self.op == "True":
            pass
        elif self.op == "False":
            pass  
        else:
            raise ValueError("Operator Changed to invalid value")


    def doFunction(self):
        self.func(self.args)

    def run(self):
        if self.op == "<" or self.op == "<=":
            while not self.isFinished():
                self.result = self.doFunction()
                self.i += self.incr
        elif self.op == ">" or self.op == ">=":
            while not self.isFinished():
                self.result = self.doFunction()
                self.i -= self.incr
        elif self.op == "True" or self.op == "==":
            while not self.isFinished():
                self.result = self.doFunction()
        elif self.op == "False":
            while not self.isFinished():
                self.result = self.doFunction()
            
        str(f"Completed. i= {self.i}, condition= While {self.first} {self.op} {self.end} , increment: {self.incr}")   
    
    def step(self):
        if self.op == "<" or self.op == "<=":
            if not self.isFinished():
                self.result = self.doFunction()
                self.i += self.incr
        elif self.op == ">" or self.op == ">=":
            if not self.isFinished():
                self.result = self.doFunction()
                self.i -= self.incr            
        return self.i

    def clear(self):
        del self.calc


