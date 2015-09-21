import re

class compute_query:
	def type1(self,runs,occurance,player_name,over,match_no):
		inning1="mydataset/"+str(match_no)+"_commentary_"+"inn1.txt"
		inning2="mydataset/"+str(match_no)+"_commentary_"+"inn2.txt"
		file1=open(inning1,'r')
		file2=open(inning2,'r')
		inning=0
		for f in file1:
			f=f[:-1]
			arr=f.split(",")
			bowl_bat=arr[0]
			bowl_bat=bowl_bat.split(" to ")
			if len(bowl_bat)>1 and len(bowl_bat)<3:
				bowler=bowl_bat[0]
				batsman=bowl_bat[1]
				bowler=bowler.strip()
				batsman=batsman.strip()
				if batsman==player_name:
					inning=inning1
					break
		if inning==0:
			inning=inning2
		
		file1.close()
		file2.close()
		file1=open(inning,'r')
		if over!=-1:
			next_over=str(over+1)+".1"
			raw_over=str(over)
			over=str(over)+".1"
			flag=0
			ans_array=[]
			for f in file1:
				f=f[:-1]
				arr=f.split(",")
				if len(arr)>1:
					bowl_bat=arr[0]
					runs_scored=arr[1]
					bowl_bat=bowl_bat.split(" to ")
					if len(bowl_bat)>1 and len(bowl_bat)<3:
						bowler=bowl_bat[0]
						batsman=bowl_bat[1]
						bowler=bowler.strip()
						batsman=batsman.strip()
						if batsman==player_name and flag==1 and runs_scored.find(str(runs))!=-1: #and runs_scored==runs and flag==1:
							ans_array.append(ball_no)
				if f==over:
					flag=1
				elif f==next_over:
					break
				if flag==1:
					ball_no=f 
			file1.close()
		else:
			ans_array=[]
			for f in file1:
				f=f[:-1]
				arr=f.split(",")
				if len(arr)>1:
					bowl_bat=arr[0]
					runs_scored=arr[1]
					bowl_bat=bowl_bat.split(" to ")
					if len(bowl_bat)>1 and len(bowl_bat)<3:
						bowler=bowl_bat[0]
						batsman=bowl_bat[1]
						bowler=bowler.strip()
						batsman=batsman.strip()
						if batsman==player_name and runs_scored.find(str(runs))!=-1: #and runs_scored==runs and flag==1:
							ans_array.append(ball_no)
				ball_no=f 
			file1.close()

		print ans_array
		return

	def type2(self,player_name,over,match_no):
		inning1="mydataset/"+str(match_no)+"_commentary_"+"inn1.txt"
		inning2="mydataset/"+str(match_no)+"_commentary_"+"inn2.txt"
		file1=open(inning1,'r')
		file2=open(inning2,'r')
		inning=0
		for f in file1:
			f=f[:-1]
			arr=f.split(",")
			bowl_bat=arr[0]
			bowl_bat=bowl_bat.split(" to ")
			if len(bowl_bat)>1 and len(bowl_bat)<3:
				bowler=bowl_bat[0]
				batsman=bowl_bat[1]
				bowler=bowler.strip()
				batsman=batsman.strip()
				if batsman==player_name:
					inning=inning1
					break
		if inning==0:
			inning=inning2
		
		file1.close()
		file2.close()
		file1=open(inning,'r')
		if over!=-1:
			next_over=str(over+1)+".1"
			raw_over=str(over)
			over=str(over)+".1"
			flag=0
			ans_array=[]
			for f in file1:
				f=f[:-1]
				arr=f.split(",")
				if len(arr)>1:
					bowl_bat=arr[0]
					runs_scored=arr[1]
					bowl_bat=bowl_bat.split(" to ")
					if len(bowl_bat)>1 and len(bowl_bat)<3:
						bowler=bowl_bat[0]
						batsman=bowl_bat[1]
						bowler=bowler.strip()
						batsman=batsman.strip()
						if batsman==player_name and flag==1 and runs_scored.find("OUT")!=-1: #and runs_scored==runs and flag==1:
							ans_array.append(ball_no)
				if f==over:
					flag=1
				elif f==next_over:
					break
				if flag==1:
					ball_no=f 
			file1.close()
		else:
			ans_array=[]
			for f in file1:
				f=f[:-1]
				arr=f.split(",")
				if len(arr)>1:
					bowl_bat=arr[0]
					runs_scored=arr[1]
					bowl_bat=bowl_bat.split(" to ")
					if len(bowl_bat)>1 and len(bowl_bat)<3:
						bowler=bowl_bat[0]
						batsman=bowl_bat[1]
						bowler=bowler.strip()
						batsman=batsman.strip()
						if batsman==player_name and runs_scored.find("OUT")!=-1: #and runs_scored==runs and flag==1:
							ans_array.append(ball_no)
				ball_no=f 
			file1.close()
		print ans_array
		return

	def type3(self,player_name,over,ball_type,match_no):
		inning1="mydataset/"+str(match_no)+"_commentary_"+"inn1.txt"
		inning2="mydataset/"+str(match_no)+"_commentary_"+"inn2.txt"
		file1=open(inning1,'r')
		file2=open(inning2,'r')
		inning=0
		for f in file1:
			f=f[:-1]
			arr=f.split(",")
			bowl_bat=arr[0]
			bowl_bat=bowl_bat.split(" to ")
			if len(bowl_bat)>1 and len(bowl_bat)<3:
				bowler=bowl_bat[0]
				batsman=bowl_bat[1]
				bowler=bowler.strip()
				batsman=batsman.strip()
				if bowler==player_name:
					inning=inning1
					break
		if inning==0:
			inning=inning2
		file1.close()
		file2.close()
		file1=open(inning,'r')
		if over!=-1:
			next_over=str(over+1)+".1"
			raw_over=str(over)
			over=str(over)+".1"
			flag=0
			ans_array=[]
			for f in file1:
				f=f[:-1]
				arr=f.split(",")
				if len(arr)>1:
					bowl_bat=arr[0]
					runs_scored=arr[1]
					bowl_bat=bowl_bat.split(" to ")
					if len(bowl_bat)>1 and len(bowl_bat)<3:
						bowler=bowl_bat[0]
						batsman=bowl_bat[1]
						bowler=bowler.strip()
						batsman=batsman.strip()
						if bowler==player_name and flag==1 and runs_scored.find(ball_type)!=-1: #and runs_scored==runs and flag==1:
							ans_array.append(ball_no)
				if f==over:
					flag=1
				elif f==next_over:
					break
				if flag==1:
					ball_no=f 
			file1.close()
		else:
			ans_array=[]
			for f in file1:
				f=f[:-1]
				arr=f.split(",")
				if len(arr)>1:
					bowl_bat=arr[0]
					runs_scored=arr[1]
					bowl_bat=bowl_bat.split(" to ")
					if len(bowl_bat)>1 and len(bowl_bat)<3:
						bowler=bowl_bat[0]
						batsman=bowl_bat[1]
						bowler=bowler.strip()
						batsman=batsman.strip()
						if bowler==player_name and runs_scored.find(ball_type)!=-1: #and runs_scored==runs and flag==1:
							ans_array.append(ball_no)
				ball_no=f 
			file1.close()
		print ans_array
		return

	def type4(self,runs,occurance,player_name,over,match_no):
		inning1="mydataset/"+str(match_no)+"_commentary_"+"inn1.txt"
		inning2="mydataset/"+str(match_no)+"_commentary_"+"inn2.txt"
		file1=open(inning1,'r')
		file2=open(inning2,'r')
		inning=0
		for f in file1:
			f=f[:-1]
			arr=f.split(",")
			bowl_bat=arr[0]
			bowl_bat=bowl_bat.split(" to ")
			if len(bowl_bat)>1 and len(bowl_bat)<3:
				bowler=bowl_bat[0]
				batsman=bowl_bat[1]
				bowler=bowler.strip()
				batsman=batsman.strip()
				if batsman==player_name:
					inning=inning1
					break
		if inning==0:
			inning=inning2
		file1.close()
		file2.close()
		file1=open(inning,'r')
		ans_array=[]
		for f in file1:
			f=f[:-1]
			arr=f.split(",")
			if len(arr)==1:
				over_num=arr[0]
				x=re.match("\d+",over_num)
				if x:
					over_num= x.group(0)
					#print over_num
			elif len(arr)>1:
					bowl_bat=arr[0]
					runs_scored=arr[1]
					bowl_bat=bowl_bat.split(" to ")
					if len(bowl_bat)>1 and len(bowl_bat)<3:
						bowler=bowl_bat[0]
						batsman=bowl_bat[1]
						bowler=bowler.strip()
						batsman=batsman.strip()
						if batsman==player_name and runs_scored.find(str(runs))!=-1: #and runs_scored==runs and flag==1:
							ans_array.append(over_num)
		file1.close()
		for i in range(len(ans_array)):
			ans_array[i]=int(ans_array[i])
		dict1={}
		for i in ans_array:
			if i in dict1:
				cnt=dict1[i]
				cnt+=1
				dict1[i]=cnt
			else:
				dict1[i]=1
		ans_array=[]
		if occurance=="max":
			max_num=-1
			for i in dict1:
				if dict1[i]>max_num:
					max_num=dict1[i]
					over_num=i
			print over_num
		elif occurance==0:
			for i in dict1:
				print "Overs-",i
		else:
			for i in dict1:
				if dict1[i]==occurance:
					ans_array.append(i)
			for i in ans_array:
				print "Overs-",i
		return

	def type5(self,player_name,over,match_no):
		inning1="mydataset/"+str(match_no)+"_commentary_"+"inn1.txt"
		inning2="mydataset/"+str(match_no)+"_commentary_"+"inn2.txt"
		file1=open(inning1,'r')
		file2=open(inning2,'r')
		inning=0
		for f in file1:
			f=f[:-1]
			arr=f.split(",")
			bowl_bat=arr[0]
			bowl_bat=bowl_bat.split(" to ")
			if len(bowl_bat)>1 and len(bowl_bat)<3:
				bowler=bowl_bat[0]
				batsman=bowl_bat[1]
				bowler=bowler.strip()
				batsman=batsman.strip()
				if batsman==player_name:
					inning=inning1
					break
		if inning==0:
			inning=inning2
		file1.close()
		file2.close()
		file1=open(inning,'r')
		ans_array=[]
		for f in file1:
			f=f[:-1]
			arr=f.split(",")
			if len(arr)==1:
				over_num=arr[0]
				x=re.match("\d+",over_num)
				if x:
					over_num= x.group(0)
					#print over_num
			elif len(arr)>1:
					bowl_bat=arr[0]
					runs_scored=arr[1]
					bowl_bat=bowl_bat.split(" to ")
					if len(bowl_bat)>1 and len(bowl_bat)<3:
						bowler=bowl_bat[0]
						batsman=bowl_bat[1]
						bowler=bowler.strip()
						batsman=batsman.strip()
						if batsman==player_name and runs_scored.find("OUT")!=-1: #and runs_scored==runs and flag==1:
							ans_array.append(over_num)
							break
		file1.close()
		for i in ans_array:
			print "Over-",i
		return

	
	def type6(self,player_name,over,ball_type,match_no,occurance):
		inning1="mydataset/"+str(match_no)+"_commentary_"+"inn1.txt"
		inning2="mydataset/"+str(match_no)+"_commentary_"+"inn2.txt"
		file1=open(inning1,'r')
		file2=open(inning2,'r')
		inning=0
		for f in file1:
			f=f[:-1]
			arr=f.split(",")
			bowl_bat=arr[0]
			bowl_bat=bowl_bat.split(" to ")
			if len(bowl_bat)>1 and len(bowl_bat)<3:
				bowler=bowl_bat[0]
				batsman=bowl_bat[1]
				bowler=bowler.strip()
				batsman=batsman.strip()
				if bowler==player_name:
					inning=inning1
					break
		if inning==0:
			inning=inning2
		file1.close()
		file2.close()
		file1=open(inning,'r')
		ans_array=[]
		for f in file1:
			f=f[:-1]
			arr=f.split(",")
			if len(arr)==1:
				over_num=arr[0]
				x=re.match("\d+",over_num)
				if x:
					over_num= x.group(0)
					#print over_num
			elif len(arr)>1:
					bowl_bat=arr[0]
					runs_scored=arr[1]
					bowl_bat=bowl_bat.split(" to ")
					if len(bowl_bat)>1 and len(bowl_bat)<3:
						bowler=bowl_bat[0]
						batsman=bowl_bat[1]
						bowler=bowler.strip()
						batsman=batsman.strip()
						if bowler==player_name and runs_scored.find(str(ball_type))!=-1: #and runs_scored==runs and flag==1:
							ans_array.append(over_num)
		file1.close()
		for i in range(len(ans_array)):
			ans_array[i]=int(ans_array[i])
		dict1={}
		for i in ans_array:
			if i in dict1:
				cnt=dict1[i]
				cnt+=1
				dict1[i]=cnt
			else:
				dict1[i]=1
		ans_array=[]
		if occurance=="max":
			max_num=-1
			for i in dict1:
				if dict1[i]>max_num:
					max_num=dict1[i]
					over_num=i
			print over_num
		elif occurance==0:
			for i in dict1:
				print "Overs-",i
		else:
			for i in dict1:
				if dict1[i]==occurance:
					ans_array.append(i)
			for i in ans_array:
				print "Overs-",i
		return


	def type7(self,runs,occurance,player_name,over,match_no):
		inning1="mydataset/"+str(match_no)+"_commentary_"+"inn1.txt"
		inning2="mydataset/"+str(match_no)+"_commentary_"+"inn2.txt"
		file1=open(inning1,'r')
		file2=open(inning2,'r')
		inning=0
		for f in file1:
			f=f[:-1]
			arr=f.split(",")
			bowl_bat=arr[0]
			bowl_bat=bowl_bat.split(" to ")
			if len(bowl_bat)>1 and len(bowl_bat)<3:
				bowler=bowl_bat[0]
				batsman=bowl_bat[1]
				bowler=bowler.strip()
				batsman=batsman.strip()
				if batsman==player_name:
					inning=inning1
					break
		if inning==0:
			inning=inning2
		file1.close()
		file2.close()
		file1=open(inning,'r')
		ans_array=[]
		for f in file1:
			f=f[:-1]
			arr=f.split(",")
			if len(arr)==1:
				over_num=arr[0]
				x=re.match("\d+",over_num)
				if x:
					over_num= x.group(0)
					#print over_num
			elif len(arr)>1:
					bowl_bat=arr[0]
					runs_scored=arr[1]
					bowl_bat=bowl_bat.split(" to ")
					if len(bowl_bat)>1 and len(bowl_bat)<3:
						bowler=bowl_bat[0]
						batsman=bowl_bat[1]
						bowler=bowler.strip()
						batsman=batsman.strip()
						if batsman==player_name and runs_scored.find(str(runs))!=-1: #and runs_scored==runs and flag==1:
							ans_array.append(bowler)
		file1.close()
		dict1={}
		for i in ans_array:
			if i in dict1:
				cnt=dict1[i]
				cnt+=1
				dict1[i]=cnt
			else:
				dict1[i]=1
		ans_array=[]
		if occurance=="max":
			max_num=-1
			for i in dict1:
				if dict1[i]>max_num:
					max_num=dict1[i]
					over_num=i
			print over_num
		elif occurance==0:
			for i in dict1:
				print "Bowler- ",i
		else:
			for i in dict1:
				if dict1[i]==occurance:
					ans_array.append(i)
			for i in ans_array:
				print "Bowler- ",i
		return

	def type8(self,player_name,over,match_no):
		inning1="mydataset/"+str(match_no)+"_commentary_"+"inn1.txt"
		inning2="mydataset/"+str(match_no)+"_commentary_"+"inn2.txt"
		file1=open(inning1,'r')
		file2=open(inning2,'r')
		inning=0
		for f in file1:
			f=f[:-1]
			arr=f.split(",")
			bowl_bat=arr[0]
			bowl_bat=bowl_bat.split(" to ")
			if len(bowl_bat)>1 and len(bowl_bat)<3:
				bowler=bowl_bat[0]
				batsman=bowl_bat[1]
				bowler=bowler.strip()
				batsman=batsman.strip()
				if batsman==player_name:
					inning=inning1
					break
		if inning==0:
			inning=inning2
		file1.close()
		file2.close()
		file1=open(inning,'r')
		ans_array=[]
		for f in file1:
			f=f[:-1]
			arr=f.split(",")
			if len(arr)==1:
				over_num=arr[0]
				x=re.match("\d+",over_num)
				if x:
					over_num= x.group(0)
					#print over_num
			elif len(arr)>1:
					bowl_bat=arr[0]
					runs_scored=arr[1]
					bowl_bat=bowl_bat.split(" to ")
					if len(bowl_bat)>1 and len(bowl_bat)<3:
						bowler=bowl_bat[0]
						batsman=bowl_bat[1]
						bowler=bowler.strip()
						batsman=batsman.strip()
						if batsman==player_name and runs_scored.find("OUT")!=-1: #and runs_scored==runs and flag==1:
							ans_array.append(bowler)
							break
		file1.close()
		for i in ans_array:
			print "Bowler -",i
		return
	
	def type10(self,player_name,match_no):
		inning1="mydataset/"+str(match_no)+"_commentary_"+"inn1.txt"
		inning2="mydataset/"+str(match_no)+"_commentary_"+"inn2.txt"
		file1=open(inning1,'r')
		file2=open(inning2,'r')
		inning=0
		for f in file1:
			f=f[:-1]
			arr=f.split(",")
			bowl_bat=arr[0]
			bowl_bat=bowl_bat.split(" to ")
			if len(bowl_bat)>1 and len(bowl_bat)<3:
				bowler=bowl_bat[0]
				batsman=bowl_bat[1]
				bowler=bowler.strip()
				batsman=batsman.strip()
				if batsman==player_name:
					inning=inning1
					break
		if inning==0:
			inning=inning2
		file1.close()
		file2.close()
		file1=open(inning,'r')
		ans_array=[]
		for f in file1:
			f=f[:-1]
			arr=f.split(",")
			if len(arr)==1:
				over_num=arr[0]
				x=re.match("\d+",over_num)
				if x:
					over_num= x.group(0)
					#print over_num
			elif len(arr)>1:
					bowl_bat=arr[0]
					runs_scored=arr[1]
					bowl_bat=bowl_bat.split(" to ")
					if len(bowl_bat)>1 and len(bowl_bat)<3:
						bowler=bowl_bat[0]
						batsman=bowl_bat[1]
						bowler=bowler.strip()
						batsman=batsman.strip()
						if batsman==player_name and runs_scored.find("OUT")!=-1: #and runs_scored==runs and flag==1:
							ans_array.append(bowler)
							break
		file1.close()
		for i in ans_array:
			print "Bowler-"+i
		return

	def foo(self,hit,out,bowl,player1_batsman,player1_bowler,hit_array,ball_array,question,over,match_no,player_name):
		#print hit,out,bowl,player1_batsman,player1_bowler,hit_array,ball_array,question,over,match_no,player_name
		if question.find("which")!=-1:
			#print "HERE"
			if question.find("ball")!=-1:
				if hit==1:
					runs=hit_array[0]
					if runs==4:
						runs="FOUR"
					elif runs==6:
						runs="SIX"
					else:
						runs=str(runs)+" run"
					occurance=hit_array[1]
					self.type1(runs,occurance,player_name,over,match_no)
				elif out==1:
					self.type2(player_name,over,match_no)
				elif bowl==1:
					ball_type=ball_array[0]
					self.type3(player_name,over,ball_type,match_no)
					pass

			elif question.find("over")!=-1:
				if hit==1:
					runs=hit_array[0]
					if runs==4:
						runs="FOUR"
					elif runs==6:
						runs="SIX"
					else:
						runs=str(runs)+" run"
					occurance=hit_array[1]
					self.type4(runs,occurance,player_name,over,match_no)
				elif out==1:
					self.type5(player_name,over,match_no)
				elif bowl==1:
					ball_type=ball_array[0]
					occurance=ball_array[1]
					self.type6(player_name,over,ball_type,match_no,occurance)
					pass

			elif question.find("bowler")!=-1:
				if hit==1:
					runs=hit_array[0]
					if runs==4:
						runs="FOUR"
					elif runs==6:
						runs="SIX"
					else:
						runs=str(runs)+" run"
					occurance=hit_array[1]
					self.type7(runs,occurance,player_name,over,match_no)
				elif out==1:
					self.type8(player_name,over,match_no)


		elif question.find(" who ")!=-1:
			if question.find("dissmissed")!=-1:
				if out==1:
					self.type10(player_name,match_no)

		elif question.find("whom")!=-1:
			#print "HERE"
			self.type10(player_name,match_no)
		
		return

	def understand_description(self,question,description,over,match_no):
		hit=0    # hit flag 
		out=0    # out flag
		bowl=0    # bowl flag
		player1_batsman=0   # player 1 is batsman 
		player1_bowler=0    # player 1 is bowler 
		hit_array=[]        # if hit then hit variables which is runs specified and num of occ of that runs is given in array
		ball_array=[]      # if bowl==1 then which ball wide/no specified and num of occ of wide / no given in array
		if description.find(" hit ")!=-1:
			hit=1
			runs=0
			player1_batsman=1
			if description.find("one")!=-1:
				runs=1
			elif description.find("two")!=-1:
				runs=2
			elif description.find("four")!=-1:
				runs=4
			elif description.find("six")!=-1:
				runs=6
			no_of_run_occ = re.search("\d+",description)
			if no_of_run_occ:
				no_of_run_occ = int(no_of_run_occ.group(0))
			else:
				no_of_run_occ = re.search("max",description)
				if no_of_run_occ:
					no_of_run_occ="max"
				else:
					no_of_run_occ=0                   
			# no_of_run_occ can be 0 is occ not mentioned , max if we need to find max occurance , else num we are intrested in is stored
			# runs can be 1,2,4,6
			hit_array.append(runs)  
			hit_array.append(no_of_run_occ)

		elif description.find(" out ")!=-1 or description.find(" dissmissed")!=-1:
			out=1
			player1_batsman=1
		
		elif description.find("bowl")!=-1:
			bowl=1
			player1_bowler=1
			ball_type=0
			no_of_ball_occ=0
			if description.find("no ball")!=-1:
				ball_type="no ball"
			elif description.find("wide")!=-1:
				ball_type="wide"
			no_of_ball_occ = re.search("\d+",description)
			if no_of_ball_occ:
				no_of_ball_occ = int(no_of_ball_occ.group(0))
			else:
				no_of_ball_occ = re.search("max",description)
				if no_of_ball_occ:
					no_of_ball_occ="max"
				else:
					no_of_ball_occ=0
			# ball_type can be "no" or "wide"
			# no_of_occ = max | num specified | or 0 if none is specified.
			ball_array.append(ball_type)
			ball_array.append(no_of_ball_occ)

		player=description.split(" ")
		player=player[0]
		self.foo(hit,out,bowl,player1_batsman,player1_bowler,hit_array,ball_array,question,over,match_no,player)
		return

	def __init__(self,string):
		a=string.find(",")
		match_no_details=string[:a]
		description=string[a+2:len(string)-1]
		#print match_no_details+"*"
		#print description
		if match_no_details.find("first")!=-1:
			match_no="odi1"
		elif match_no_details.find("second")!=-1:
			match_no="odi2"
		elif match_no_details.find("third")!=-1:
			match_no="odi3"
		elif match_no_details.find("fourth")!=-1:
			match_no="odi4"
		elif match_no_details.find("fifth")!=-1:
			match_no="odi5"

		a=description.find("which")
		if a!=-1:
			pass
		else:
			a=description.find(" who ")
			if a!=-1:
				pass
			else:
				#print "HERE"
				a=description.find(" by whom")
		question = description[a:]
		description = description[:a+1]
		a=description.find(" in ")
		over_specified = description[a:]
		description = description[:a]
		#print description
		#print question
		if over_specified.find("over"):
			over = re.search("\d+",over_specified)
			if over:
				over=int(over.group(0))
			else:
				over=-1
		else:
			over=-1

		self.understand_description(question,description,over,match_no)
		#print question
		#print description
		#print over
		#print match_no

while 1:
	a=raw_input()
	if a=="q":
		break
	l=compute_query(a)