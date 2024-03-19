class Loop:
    def __init__(self,iterations,func,arg=None):
        self.func = func
        self.iterations = iterations
        self.current = 0
        self._arg = arg

    @property
    def arg(self):
        return self._arg
    
    @arg.setter
    def arg(self,arg):
        self._arg = arg

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.iterations:
            if self.arg != None:
                result = self.func(self.arg)
            else:
                result = self.func()
            self.current += 1
        else:
            raise StopIteration
        return result
        
    def manual_next(self):
        if self.current < self.iterations:
            if self.arg != None:
                result = self.func(self.arg)
            else:
                result = self.func()
            self.current += 1
        else:
            raise StopIteration
        return result
    
    async def async_manual_next(self):
        if self.current < self.iterations:
            if self.arg != None:
                result = self.func(self.arg)
            else:
                result = self.func()
            self.current += 1
        else:
            raise StopIteration
        return result