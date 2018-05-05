#27 Process Class in python

class Process:
	def __init__(self,slice,input_output,waiting,arrival,burst):
		self.slice=slice
		self.input_output=input_output
		self.waiting=waiting
		self.arrival=arrival
		self.burst=burst
		self.remainingQuantum=0
		self.comming_back_time=0
	def showProcess(self):
		print(str(self.slice)+" "+str(self.input_output)+" "+str(self.waiting)+" "+str(self.arrival)\
			+" "+str(self.burst))
	
	def change_burst(self,value):
		self.burst=self.bust-value
	def return_all(self):
		list=[self.slice,self.input_output,self.waiting,self.arrival,self.burst]
		return list

class Que:
	def __init__(self,s):
		if(s>0):
			self.size=s
			self.array={}
			self.inque=-1
			self.deque=-1
		else:
			print("Que of negative size or zero size is not allowed")
			exit(0)
	def IsEmpty(self):
		return (self.inque == -1)
		
	def IsFull(self):
		return ((self.inque == self.size-1 and self.deque == 0) or (self.inque == self.deque-1))
	
	def enque(self,value):
		if (self.IsFull()):
			print("You cannot enter more items in que because que is full.")
		else:
			if (self.IsEmpty()):
				self.deque=0
			self.inque=(self.inque+1)%self.size
			temp_list=[]
			temp_list.append(value)
			self.array[self.inque]=value
			
	def deeque(self):
		if(self.IsEmpty()):
			print("The que is already empty")
		else:
			if(self.deque!=self.inque):
				temporay=self.array[self.deque].return_all()
				self.deque = (self.deque+1)%self.size
				return temporay
			else:
				temporay=self.array[self.deque].return_all()
				self.inque=-1
				self.deque=-1
				return temporay

	def showQue(self):
		if self.IsEmpty():
			print("Que is empty")
		elif self.deque < self.inque:
			for i in range (self.deque,self.inque+1):
				print(self.array[i].return_all())
#				print("First")
		elif(self.inque < self.deque):
			i=self.deque
			while i!=self.inque:
				print(self.array[i].return_all())
#				print("Second")
				i=(i+1)%size
			print(self.array[i])
		else:
			print(self.array[self.inque].return_all())
			
	def clear(self):
		if (not self.IsEmpty()):
			self.inque=-1
			self.deque=-1			
	def get_deque_value(self):
		temporary=self.array[self.deque].return_all()
		return temporary

def convert_list_to_Process(list):
			process=Process(list[0],list[1],list[2],list[3],list[4])
			return process
def check_which_equal_values_tabelQue(i,Q):#this one is for tabel Que que
	while True:
			c=0
			Return_list=[]
			temp_list=Q.get_deque_value()
			if(i==temp_list[3]):
				c+=1
				Return_list.append(temp_list)
				garbage=Q.deeque()
				temp_list=Q.get_deque_value()
				if(i==temp_list[3]):
					continue
			else:
				break
	if(c!=0):
		R=[]
		R.append(c)
		R.append(Return_list)
		return R
	else:
		R=[-1]
		return R
		
def check_which_equal_values_of_waitingQue(i,Q):#this one is for waiting que
	while True:
			c=0
			Return_list=[]
			temp_list=Q.get_deque_value()
			if(i==temp_list[6]):
				c+=1
				Return_list.append(temp_list)
				garbage=Q.deeque()
				temp_list=Q.get_deque_value()
				if(i==temp_list[3]):
					continue
			else:
				break
	if(c!=0):
		R=[]
		R.append(c)
		R.append(Return_list)
		return R
	else:
		R=[-1]
		return R 

def check_and_change_all_ques(i,tabelQue,waitingQue,readyQue):
		receive=check_which_equal_values_tabelQue(i,tabelQue)
		if(receive[0]=-1):#checkinng is there any process arives. 
			count=receive[0]
			temp_list=receive[1]
			for k in range (count):
				temp=convert_list_to_Process(temp_list[i])
				readyQue.enque(temp)
	
		receive=check_which_equal_values_of_waitingQue(i,waitingQue)
		if(receive[0]=-1):#checkinng is there any process is ready to come from waiting Que.
			count=receive[0]
			temp_list=receive[1]
			for k in range (count):
				temp=convert_list_to_Process(temp_list[i])
				readyQue.enque(temp)
		
#Main

print("Main")
tabelQue=Que(1000)
readyQue=Que(1000)
waitingQue=Que(1000)
dictionary={}#for sorting purpose
no_of_inputs=int(raw_input("How Many processes you want to enter? : "))
if no_of_inputs<0:
	print("Sorry negative or zero number of processes are not allowed.")
	exit(0)
else:
	slice=int(raw_input("Enter the slice time : "))
	if slice<0:
		print("Zero or negative slice time is not allowed ")
		exit(0)
	else:
		input_output=int(raw_input("Enter Input/output time\nOR\nEnter the time after which"\
			" the process will go for inputs : "))
		waiting=int(raw_input("Enter the waiting time : \nOR\nEnter the time"\
			"for which a process will wait in waiting que: "))
		for i in range(no_of_inputs):
			temporary_dic2={}#for sorting purpose
			arrival=int(raw_input("Enter the Arrival time : "))
			burst=int(raw_input("Enter the burst time : "))
			temporary_dic2["arival"]=arrival
			temporary_dic2["burst"]=burst
			dictionary[i]=temporary_dic2
#insertion sort starts
		n=len(dictionary)
		i=1
		for i in range(n):
			j=i
			while (j>0) and (dictionary[j].get("arival")<dictionary[j-1].get("arival")):
				temporary_value=dictionary[j]
				dictionary[j]=dictionary[j-1]
				dictionary[j-1]=temporary_value
				j-=1
#tested
		i=0
		while True:
			if i<no_of_inputs:
				process=Process(slice,input_output,waiting,dictionary[i].get("arival"),\
					dictionary[i].get("burst"))
#tested				
				tabelQue.enque(process)
				i+=1;
			else:
				break
#tested
		i=0#universal time
		j=0
		w=0 #waiting counter
		k=0
		while True:
			if (readyQue.IsEmpty() and tabelQue.IsEmpty() and waitingQue.IsEmpty()):
				break 				#this condition tells that our all process are ended.
			else:
				check_and_change_all_ques(i,tabelQue,waitingQue,readyQue)
				list_temp=readyQue.deeque()
				while(i != list_temp[3]):
					i+=1
					check_and_change_all_ques(i,tabelQue,waitingQue,readyQue)
					continue
				slice=list[0]
				input_output=list[1]
				waiting=list[2]
				arrival=list[3]
				burst=list[4]
				remainingQuantum=list[5]
				j=0
				if(remainingQuantum>0):
					while j<remainingQuantum:
						j+=1
						i+=1
						list[5]-=1#Remaninig Quantum time
						list[4]=list[4]-1#burst
						list[1]=list[1]-1#input/output going time
						check_and_change_all_ques(i,tabelQue,waitingQue,readyQue)
						if(j!=input_output and j!=burst):
							continue
						else:
							if (j== input_output):
								list[6]=i+list[2]
								list=convert_list_to_Process(list)
								waitingQue.enque(list)
								break
							else:
								break
				else:
					list[5]=0
					while True:
						if(j!=input_output and j!= slice and j!=burst):
							list[5]-=1#Remaninig Quantum time
							list[4]=list[4]-1#burst
							list[1]=list[1]-1#input/output going time
							j+=1
							i+=1
							check_and_change_all_ques(i,tabelQue,waitingQue,readyQue)
						elif(i==burst):
							break
						elif(i==input_output):
							list[6]=i+list[2]
							list=convert_list_to_Process(list)
							readyQue.enque(list)
							break
						elif(i==slice):
							list=convert_list_to_Process(list)
							readyQue.enque(list)
							break						
							