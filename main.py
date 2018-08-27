import problem5b
import sys
import re
import pickle
import time
import copy
import astropy.table
import datetime


class Task_manager():

    def __init__(self, id=None, name=None, creation_date=None, completion_date='Pending', due_date=None, priority=1, complete = False, age = None):
        self.id = id
        self.name = name
        self.creation_date = creation_date
        self.completion_date = completion_date
        self.due_date = due_date
        self.priority = priority
        self.complete = complete
        self.age = age

    @staticmethod
    def assign_ID():
        '''#Returns a valid ID for the new task by reading
        the current Pickle and adding 1 to the current max'''

        list_of_IDs = []
        database_open = open('.todo.pickle', 'rb')

        while True:
            try:
                a = pickle.load(database_open)
                if a == '':
                    break
                else:
                    list_of_IDs.append(int(a[0]))
            except EOFError:
                break
        database_open.close()
        if list_of_IDs == []:
            return 1
        else:
            return max(list_of_IDs) + 1

    @staticmethod
    def rewrite_delete():
        list_of_pickle_objects = []
        database_open = open('.todo.pickle', 'rb')
        while True:
            try:
                a = pickle.load(database_open)
                if int(a[0]) == int(id_to_delete):
                    continue
                else:
                    list_of_pickle_objects.append(list(a))
            except EOFError:
                break
        database_open.close()
        return list_of_pickle_objects

    @staticmethod
    def rewrite_complete():
        list_of_pickle_objects2 = []
        database_open = open('.todo.pickle', 'rb')
        while True:
            try:
                a = pickle.load(database_open)
                list_of_pickle_objects2.append(list(a))
            except EOFError:
                break
        database_open.close()
        return list_of_pickle_objects2

    @staticmethod
    def load_data():
        '''To read and write back to the Nodes'''
        database_open= open('.todo.pickle', 'rb')

        while True:
            try:
                b = pickle.load(database_open)
                loader.add(b)
            except EOFError:
                break
        database_open.close()


    @staticmethod
    def age(x):
        y = datetime.datetime.strptime(x, '%m/%d/%Y')
        start = datetime.datetime(y.year,y.month,y.day)
        return (datetime.datetime.now() - start).days

    @staticmethod
    def list():
        '''Currently active tasks'''
        list_of_IDs = [i[0] for i in loader.__str__() if i[6] == False]
        list_of_ages = ['{}d'.format(Task_manager.age(i[2])) for i in loader.__str__() if i[6] == False]
        list_of_due_dates = [i[4] for i in loader.__str__() if i[6] == False]
        list_of_Priorities = [i[5] for i in loader.__str__() if i[6] == False]
        list_of_Tasks = [i[1] for i in loader.__str__() if i[6] == False]
        table = astropy.table.Table([list_of_IDs, list_of_ages, list_of_due_dates, list_of_Priorities, list_of_Tasks]
                                    ,names=('ID', 'Age', 'Due Date', 'Priority', 'Task'))
        return table
    @staticmethod
    def filtered_list():
        '''Currently active tasks filtered'''
        list_of_IDs = [i[0] for i in loader.__str__() if i[6] == False and (re.search(pattern, i[1]))]
        list_of_ages = ['{}d'.format(Task_manager.age(i[2])) for i in loader.__str__() if i[6] == False and (re.search(pattern, i[1]))]
        list_of_due_dates = [i[4] for i in loader.__str__() if i[6] == False and (re.search(pattern, i[1]))]
        list_of_Priorities = [i[5] for i in loader.__str__() if i[6] == False and (re.search(pattern, i[1]))]
        list_of_Tasks = [i[1] for i in loader.__str__() if (i[6] == False) and (re.search(pattern, i[1]))]
        table = astropy.table.Table([list_of_IDs, list_of_ages, list_of_due_dates, list_of_Priorities, list_of_Tasks]
                                    ,names=('ID', 'Age', 'Due Date', 'Priority', 'Task'))
        return table

    @staticmethod
    def report():
        '''Tasks since inception'''
        list_of_IDs = [i[0] for i in loader.__str__()]
        list_of_ages = ['{}d'.format(Task_manager.age(i[2])) for i in loader.__str__()]
        list_of_due_dates = [i[4] for i in loader.__str__()]
        list_of_Priorities = [i[5] for i in loader.__str__()]
        list_of_Tasks = [i[1] for i in loader.__str__()]
        list_of_created= [i[2] for i in loader.__str__()]
        list_of_completed = [i[3] for i in loader.__str__()]
        table = astropy.table.Table([list_of_IDs, list_of_ages, list_of_due_dates, list_of_Priorities, list_of_Tasks, list_of_created,
                                     list_of_completed],names=('ID', 'Age', 'Due Date', 'Priority', 'Task', 'Created', 'Completed'))
        return table

    def set_data(self, completion_date = 'Pending', complete = False):
        '''This is to write to the pickle file and add a new ID to each task.'''
        self.id = Task_manager.assign_ID()
        self.name = initial_input[1]
        self.creation_date = time.strftime("%m/%d/%Y")
        self.completion_date = completion_date
        self.due_date = initial_input[2]
        self.priority = initial_input[3]
        self.complete = complete
        self.age = '{}d'.format(Task_manager.age(self.creation_date))

    def delete_data(self):
        global id_to_delete
        id_to_delete = initial_input[1]
        copy_of_list = copy.deepcopy(Task_manager.rewrite_delete())
        if Task_manager.rewrite_delete() == []:
            pickle.dump('', open('.todo.pickle', 'wb'))
        else:
            open('.todo.pickle', 'wb')
            for i in copy_of_list:
                # print('this is i: ', i)
                pickle.dump(i, open('.todo.pickle', 'ab'))
        print('Deleted task {}'.format(id_to_delete))

    def add_data_pickle(self):
        database_open = open('.todo.pickle', 'ab')
        pickle.dump([self.id,self.name,self.creation_date,self.completion_date, self.due_date,self.priority,self.complete, self.age],database_open)
        database_open.close()
        print('Created task {}'.format(self.id))

    def complete_assignment(self):
        id_to_delete = initial_input[1]
        copy_of_list = copy.deepcopy(Task_manager.rewrite_complete())
        for i in copy_of_list:
            if int(i[0]) == int(id_to_delete):
                i[6] = True
                i[3] = time.strftime("%m/%d/%Y")
        if Task_manager.rewrite_complete() == []:
            pickle.dump('', open('.todo.pickle', 'wb'))
        else:
            open('.todo.pickle', 'wb')
            for i in copy_of_list:
                pickle.dump(i, open('.todo.pickle', 'ab'))
        print('Completed task {}'.format(id_to_delete))


def main():

    regex_strip = r'[a-z]*(:)'
    if len(initial_input) > 2:
        initial_input[2] = re.sub(regex_strip,'', initial_input[2])
        initial_input[3] = re.sub(regex_strip,'', initial_input[3])

    "Format needs to be: python filename.py <command> <ID number or 'task in quotes'> <mm/dd/yyyy> <1,2 or 3>"
    entry = Task_manager()

    if initial_input[0] == 'add':
        '''Add to the pickle'''
        entry.set_data()
        entry.add_data_pickle()

    if initial_input[0] == 'delete':
        '''delete from the pickle permanently'''
        entry.delete_data()

    if initial_input[0] == 'done':
        '''tag as complete, will not show in list'''
        entry.complete_assignment()

    '''load pickle into the Node'''

    Task_manager.load_data()

    try:
        if initial_input[0] == 'list':
            global pattern
            pattern = '\\+'
            if re.match(pattern, initial_input[1]):
                pattern = re.sub(pattern, '', initial_input[1])
                print(Task_manager.filtered_list())
            else:
                print(Task_manager.list())
    except IndexError:
        print(Task_manager.list())

    if initial_input[0] == 'report':
        print(Task_manager.report())

if __name__ == '__main__':
    initial_input = sys.argv[1:]
    loader = problem5b.Ordered_list()
    main()
