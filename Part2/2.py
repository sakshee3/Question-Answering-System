import sys
import re

class make_query:
	def handleifthen(self,string,query_string):
		a=string.split(" if ")
		a=a[1]
		pred1=a.split(" then ")
		pred2=pred1[1]
		pred1=pred1[0]
		pred1=pred1.split(" ")
		pred2=pred2.split(" ")
		string1=''
		string2=''
		for i in pred1:
			if i:
				string1+=i[0]
		for i in pred2:
			if i:
				string2+=i[0]
		string1+="(x)"
		string2+="(x)"
		query_string+="( "+string1+" -> "+string2+" ) )"
		print query_string
		return

	def handleand(self,string,query_string):
		a=string.split(" and ")
		pred2=a[1]
		pred1=a[0]
		pred1=pred1.split(" ")
		pred2=pred2.split(" ")
		string1=''
		string2=''
		for i in pred1:
			if i:
				string1+=i[0]
		for i in pred2:
			if i:
				string2+=i[0]
		string1+="(x)"
		string2+="(x)"
		query_string+="( "+string1+" & "+string2+" ) )"
		print query_string
		return

	def handleconsistof(self,string,query_string):
		a=string.split(" consists of ")
		pred2=a[1]
		pred1=a[0]
		pred1=pred1.split(" ")
		pred2=pred2.split(" ")
		string1=''
		string2=''
		for i in pred1:
			if i:
				string1+=i[0]
		for i in pred2:
			if i:
				string2+=i[0]
		string1+="(x)"
		string2+="(x)"
		query_string+="( "+string1+" & "+string2+" ) )"
		print query_string
		return

	def handlecontains(self,string,query_string):
		a=string.split(" contains ")
		pred2=a[1]
		pred1=a[0]
		pred1=pred1.split(" ")
		pred2=pred2.split(" ")
		string1=''
		string2=''
		for i in pred1:
			if i:
				string1+=i[0]
		for i in pred2:
			if i:
				string2+=i[0]
		string1+="(x)"
		string2+="(x)"
		query_string+="( "+string1+" & "+string2+" ) )"
		print query_string
		return

	def handleisgivento(self,string,query_string):
		a=string.split(" is given to ")
		pred2=a[1]
		pred1=a[0]
		pred1=pred1.split(" ")
		pred2=pred2.split(" ")
		string1=''
		string2=''
		for i in pred1:
			if i:
				string1+=i[0]
		for i in pred2:
			if i:
				string2+=i[0]
		string1+="(x)"
		string2+="(x)"
		query_string+="( "+string1+" -> "+string2+" ) )"
		print query_string
		return

	def play_with_string(self,string,query_string):
		search1='.*\sif\s.*\sthen\s.*'
		search2='.*\sand\s.*'
		search3='.*\sconsists\sof\s.*'
		search4='.*\scontains\s.*'
		search5='.*\sis\sgiven\sto\s.*'
		mad1=re.findall(search1,string)
		mad2=re.findall(search2,string)
		mad3=re.findall(search3,string)
		mad4=re.findall(search4,string)
		mad5=re.findall(search5,string)
		#print mad3
		if mad1:
			self.handleifthen(string,query_string)
		elif mad2:
			self.handleand(string,query_string)
		elif mad3:
			self.handleconsistof(string,query_string)
		elif mad4:
			self.handlecontains(string,query_string)
		elif mad5:
			self.handleisgivento(string,query_string)
		return

	def __init__(self,string):
		parse_input=string.split(",")
		pred1=parse_input[0]
		query_string=''
		if pred1.find("For all")!=-1:
			query_string+="all x.( "
			if pred1.find("match")!=-1:
				query_string+="match(x) -> "
			elif pred1.find("inning")!=-1:
				query_string+="inning(x) -> "
			elif pred1.find("player")!=-1:
				query_string+="player(x) -> "
		
		elif pred1.find("There exist")!=-1:
			query_string+="exists x.( "
			if pred1.find("match")!=-1:
				query_string+="match(x) & "
			elif pred1.find("inning")!=-1:
				query_string+="inning(x) & "
			elif pred1.find("player")!=-1:
				query_string+="player(x) & "
		
		self.play_with_string(parse_input[1],query_string)
		return

while 1:
	string = raw_input()
	if string=="q":
		break
	a=make_query(string)


