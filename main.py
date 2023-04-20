from stmpy import Driver, Machine

import ipywidgets as widgets
from IPython.display import display

class Student:
    def __init__(self):
        print("Init - Student")

        self.button = widgets.Button(description="Next task")
        self.button.on_click(self.on_button_press)

        display(self.button)

    def on_button_press(self, b):
        self.stm.send('next_task')

    #def ask_question(self):
        #print("What is 1+1?")
        #self.mqtt_client.publish("question", "What is 1+1?")

    #def send_mqtt_tock(self):
        #print("Tock! {}".format(self.tocks)) 
        #self.tocks = self.tocks + 1
        #self.mqtt_client.publish("group16 tock", self.ticks)



class TA:
    def on_init(self):
        print("Init - TA")

    def show_group_progress(self):
        print("Group progress")



#for student
s0 = {"source": "initial", "target": "student_display_tasks"}

s1 = {
    "trigger": "start_task",
    "source": "student_display_tasks",
    "target": "student_task",
}
s2 = {
    "trigger": "next_task",
    "source": "student_task",
    "target": "student_task",
}
s3 = {
    "trigger": "help",
    "source": "student_task",
    "target": "student_TA_assistance",
}
s4 = {
    "trigger": "t",
    "source": "student_task",
    "target": "student_TA_assistance",
}
s5 = {
    "trigger": "deliver",
    "source": "student_task",
    "target": "student_end", #what is end?
}
s6 = {
    "trigger": "back_to_waiting",
    "source": "student_task",
    "target": "student_display_tasks",
}
s7 = {
    "trigger": "help_finished",
    "source": "student_TA_assitance",
    "target": "student_task",
}


#for TA
t0 = {"source": "initial", "target": "TA_waiting"}
t1 = {
    "trigger": "help",
    "source": "waiting",
    "target": "TA_assist",
}
t2 = {
    "trigger": "notification",
    "source": "TA_waiting",
    "target": "TA_assist",
}
t3 = {
    "trigger": "help_finished",
    "source": "TA_assist",
    "target": "TA_waiting",
}

#student states
student_display_tasks = {'name': 'student_display_task',
      'entry': 'show_tasks'
      }
student_task = {'name': 'student_task',
      'entry': 'start_timer("t", 1000)'
      }
student_TA_assistance = {'name': 'student_TA_assistance',
      'entry': 'add_group_to_queue'
      }
student_end = {'name': 'student_end',
      'entry': 'finished'
      }

#TA states
TA_waiting = {'name': 'TA_waiting',
      'entry': 'show_group_progress'
      }
TA_assist = {'name': 'TA_assist',
      'entry': 'help_group'
      }


student = Student()
student_machine = Machine(name='stm_student', transitions=[s0, s1, s2, s3, s4, s5, s6, s7], obj=student, states=[student_display_tasks, student_task, student_TA_assistance, student_end])
student.stm = student_machine

ta = TA()
ta_machine = Machine(name='stm_ta', transitions=[t0, t1, t2, t3], obj=ta, states=[TA_waiting, TA_assist])
ta.stm = ta_machine

driver = Driver()
driver.add_machine(student_machine)
driver.add_machine(ta_machine)
driver.start()


driver.stop()