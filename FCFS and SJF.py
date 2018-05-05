def first_come_first_served():
	dictionary={}
	print("\n\tThis is First Come First Served Schedule\n\n")
	no_of_process=int(raw_input("How many process you want to run? : "))
	if no_of_process<0:
		print("Negative and zero values are not allowed")
	else:
#input
		for i in range(no_of_process):
			temporary_dictionary={}
			print("Process "+str(i+1)+" :")
			temporary_variable1=int(raw_input("Enter the Arival time : "))
			temporary_variable2=int(raw_input("Enter the Burst Time : "))
			temporary_dictionary["arival"]=temporary_variable1
			temporary_dictionary["burst"]=temporary_variable2
			dictionary[i]=temporary_dictionary
		print("Now check weather each input is correct or not.")
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
#insertion sort ends				
		for i in range (no_of_process):
			print("Process no "+str(i+1)+" "+str(dictionary[i]))
		pending_input=raw_input("Press Y if every thing is good : ")
		if pending_input=="Y" or pending_input=="y":
			i=dictionary[0]
			i=i["arival"]	#my clock
			j=0 #for dictionary processes
			while True:
				if j<no_of_process:
					process_dictionary=dictionary[j]
					process_arival=process_dictionary["arival"]
					process_burst=process_dictionary["burst"]
					j+=1
					for k in range (process_burst):
						i+=1
					print("\n\nProcess "+str(j)+" Finished\n")
					print("\nIts arrival time is: "+str(process_arival)+"\n\n And Burst time is: "+str(process_burst))
					print("\n\nAnd it terminated at time : "+str(i))
					pending_input2=raw_input("Press any key to continue")
				else:
					break
		else:
			print("Okay Run The program again and give good/proper input :)")
# End of First Come And First Served


def shortest_job_first():
	dictionary={}
	print("\n\tThis is Shortest Job First Schedule\n\n")
	no_of_process=int(raw_input("How many process you want to run? : "))
	if no_of_process<=0:
		print("Negative and zero values are not allowed")
	else:
		for i in range(no_of_process):
			temporary_dictionary={}
			print("Process "+str(i+1)+" :")
			temporary_variable1=int(raw_input("Enter the Arival time : "))
			temporary_variable2=int(raw_input("Enter the Burst Time : "))
			temporary_dictionary["arival"]=temporary_variable1
			temporary_dictionary["burst"]=temporary_variable2
			dictionary[i]=temporary_dictionary
#insertion sort (for arival time) starts
		n=len(dictionary)
		i=1
		for i in range(n):
			j=i
			while (j>0) and (dictionary[j].get("arival")<dictionary[j-1].get("arival")):
				temporary_value=dictionary[j]
				dictionary[j]=dictionary[j-1]
				dictionary[j-1]=temporary_value
				j-=1
#insertion sort ends

		n=len(dictionary)
		i=0
		for i in range (n):
			temp_burst=dictionary[i].get("burst")
			count=0
			j=i+1
			while j < n:
				if(dictionary[j].get("arival")<temp_burst):
					count+=1
					temp_burst=temp_burst-dictionary[j].get("arival")
				j+=1
			#print("count = "+str(count))
			k=i+1
			#print("k1 = "+str(k))
			while k<=count:
				if(k+1)>count:
					#print("k+1 break = "+str(k+1))
					break
				else:
					#print("k else = "+str(k))
					if(dictionary[k].get("burst")>dictionary[k+1].get("burst")):
						temporary_value=dictionary[k]
						dictionary[k]=dictionary[k+1]
						dictionary[k+1]=temporary_value
				k+=1
# running the process
		print("Now check weather each input is correct or not.")
		for i in range (no_of_process):
			print("Process no "+str(i+1)+" "+str(dictionary[i]))
		pending_input=raw_input("Press Y if every thing is good : ")
		if pending_input=="Y" or pending_input=="y":
			i=dictionary[0].get("arival")
			j=0
			while True:
				if j<no_of_process:
					process_dictionary=dictionary[j]
					process_arival=process_dictionary["arival"]
					process_burst=process_dictionary["burst"]
					j+=1
					for k in range(process_burst):
						i+=1
					print("\n\n Process "+str(j)+" ends\n\n")
					print("Its Arival Time is : "+str(process_arival))
					print("Its Burst Time is : "+str(process_burst))
					print("And it terminated at : "+str(i))
					pending_input2=raw_input("Press any key to continue")
				else:
					break
		else:
			print("Okay Run The program again and give good/proper input :)")
# End of Shortest Job First

	
#main
print("1- First Come First Served")
print("2- Shortest Job First")
print("3- Round Robbin")
input=int(input("Select the schedule mathod (1,2,3)? :"))
if input==1:
	first_come_first_served()
elif input==2:
	shortest_job_first()
elif input==3:
	round_robbin()
else:
	print("Wrong input")