from stmpy import Driver, Machine

class Student:
    def on_init(self):
        print("Init - Student")

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



# for student
s0 = {"source": "initial", "target": "waiting"}
s1 = {
    "trigger": "start_task",
    "source": "waiting",
    "target": "task",
}
s2 = {
    "trigger": "next_task",
    "source": "task",
    "target": "task",
}
s3 = { #check multiple trigger
    "trigger": "help, t",
    "source": "task",
    "target": "TA_assistance",
}
s4 = {
    "trigger": "deliver",
    "source": "task",
    "target": "end", #what is end?
}
s5 = {
    "trigger": "back_to_waiting",
    "source": "task",
    "target": "waiting",
}
s6 = {
    "trigger": "help_finished",
    "source": "TA_assitance",
    "target": "task",
}



#for TA
t0 = {"source": "initial", "target": "waiting"}
t1 = {
    "trigger": "help",
    "source": "waiting",
    "target": "TA_assistance",
}
t2 = {
    "trigger": "notification",
    "source": "waiting",
    "target": "TA_assistance",
}
t3 = {
    "trigger": "help_finished",
    "source": "TA_assistance",
    "target": "waiting",
}