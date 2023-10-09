class ToDoApp:
    def __init__(self,task_list=[]) -> None:
        self.task_dict={}
        for i in task_list:
            self.task_dict[i]='Not Done Yet'
        
    def add_task(self,tasks: list):
        for i in tasks:
            self.task_dict[i]='Not done yet'
    def done(self,task):
        self.task_dict[task]='Done'
    def discard_task(self,tasks: list):
        for i in tasks:
            del self.task_dict[i]
    def show_status(self):
        res = ''
        for t,s in self.task_dict.items():
            res+=f'{t}\'s status is : {s}\n'
        print(res)
    def list(self):
        res=''
        for i in self.task_dict.keys():
            res+=f'{i}\n'
        return res
if __name__=='__main__':
    a=ToDoApp(['walking','jogging'])
    a.list()
    a.add_task(['math','english'])
    a.show_status()
    a.done('math')
    a.show_status()
    a.add_task(['shopping','Going to the gym'])
    a.list()
    a.discard_task(['walking'])
    a.list()
    a.show_status()