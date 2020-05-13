# builder pattern
from abc import ABC
from datetime import datetime
from enum import Enum, auto


class State(Enum):
    IN_PROGRESS = auto()
    END = auto()
    PENDING = auto()


class Task:
    def __init__(self):
        # general information
        self.name_task = None
        self.person_assign = None
        self.person_incharge = None
        self.start_date = None
        self.end_date = None
        # state task
        self.task_state = None
        self.diary = []

    def __str__(self):
        diary = '\n'.join(self.diary)
        if self.task_state == State.IN_PROGRESS:
            self.task_state = 'In progress'
        elif self.task_state == State.END:
            self.task_state = 'Finish'
        elif self.task_state == State.PENDING:
            self.task_state = 'Hold back'
        return f'task {self.name_task} is assigned by {self.person_assign} for {self.person_incharge} from ' \
               f'{self.start_date} to {self.end_date}: \nProgress: {self.task_state}\nDiary:\n{diary}'


class Diary:
    def __init__(self, time, str_diary):
        self.str_diary = str_diary
        self.time = time

    def __str__(self):
        return f'{self.time}, note: {self.str_diary}'


class TaskBuilder:
    def __init__(self, task=None):
        if task is None:
            self.task = Task()
        else:
            self.task = task

    @property
    def info(self):
        return InputInfor(self.task)

    @property
    def update(self):
        return StateDiary(self.task)

    def build(self):
        return self.task


class InputInfor(TaskBuilder):
    def __init__(self, task):
        super().__init__(task)

    def name(self, name_task):
        self.task.name_task = name_task
        return self

    def assignedby(self, name_person):
        self.task.person_assign = name_person
        return self

    def assignedto(self, name_person):
        self.task.person_incharge = name_person
        return self

    def start_date(self, start_date):
        self.task.start_date = start_date
        return self

    def end_date(self, end_date):
        self.task.end_date = end_date
        return self


class StateDiary(TaskBuilder):
    def __init__(self, task):
        super().__init__(task)

    def state(self, state):
        if isinstance(state, State):
            self.task.task_state = state
        else:
            raise Exception('wrong state')
        return self

    def diary(self, str_diary):
        time = datetime.now()
        self.task.diary.append(Diary(time=time, str_diary=str_diary).__str__())
        return self


class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print('how many did the init run')

database1 = Database()
database2 = Database()
print(database1 == database2)

pii_in_the_cloud = TaskBuilder().info \
                                    .name(name_task='"PII in the cloud"') \
                                    .assignedby(name_person='Matthieu') \
                                    .assignedto(name_person='Long') \
                                    .start_date(start_date=datetime.now()) \
                                    .end_date(end_date='until die')\
                                .update \
                                    .state(state=State.IN_PROGRESS) \
                                    .diary(str_diary='hoc AWS') \
                                    .diary(str_diary='wrong concept of builder ?') \
                                    .diary(str_diary='wrong concept of design pattern') \
                                .build()


print(pii_in_the_cloud)










