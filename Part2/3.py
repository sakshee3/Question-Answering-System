import sys 
import nltk
from nltk.corpus import wordnet as wn 
import re

exceptions=['match','most','was','is','were','over','started','first','?','']


ans_list=[]

# lemmalist is to compute similiar words
def lemmalist(str): 
	syn_set = [] 
	for synset in wn.synsets(str): 
		for item in synset.lemma_names: 
			syn_set.append(item) 
	return syn_set

def match_details(word,line):
	if line.find(word)!=-1:
		#print "*********************   "+word+"        ***********************"
		return 1
	else:
		return 0

def compute_file(filename,final_list):
	file1=open(filename,'r')
	flag=0
	for f in file1:
		f=f[:-1]
		t=0
		for i in final_list:
			flag=0
			for j in i:
				cnt=match_details(j,f)
				if cnt==1:
					flag=1
			if flag==0:
				break
		if flag==1:
			ans_list.append(f)
	return



def search1(match_no,final_list):
	match1='mydataset/odi'+str(match_no)+'_commentary_inn1.txt'
	match2='mydataset/odi'+str(match_no)+'_commentary_inn2.txt'
	compute_file(match1,final_list)
	compute_file(match2,final_list)
	return


def search_all(final_list):
	str1=''
	for i in range(1,6):
		str1=''
		str1=str1+'mydataset/odi'+str(i)+'_commentary_inn'
		for j in range(1,3):
			str2=''
			str2=str1
			str2=str1+str(j)+'.txt'
			compute_file(str2,final_list)
	return

def do_something(string):
	search='.*\smatch\s\d+\s.*'
	mad=re.findall(search,string)
	if mad:
		list1=[]
		list1=string.split(" match ")
		list1=list1[1]
		list1=list1.split(" ")
		match_no=int(list1[0])
	else:
		match_no=-1
	list1=[]
	list1=string.split(' ')
	final_list=[]
	temp_dict={}
	for i in list1:
		if i not in exceptions:
			final_list.append(i)
	fig_of_speech=nltk.pos_tag(final_list)
	noun='NN'
	verb='VB'
	main_noun_list=[]
	main_verb_list=[]
	noun_list=[]
	verb_list=[]
	for i in fig_of_speech:
		if re.findall(noun,i[1]):
			noun_list.append(i[0])
			main_noun_list.append(noun_list)
		if re.findall(verb,i[1]):
			verb_list.append(i[0])
			main_verb_list.append(verb_list)
	#print noun_list
	#print verb_list
	final_list=[]
	for i in main_noun_list:
		final_list.append(i)
	for i in main_verb_list:
		final_list.append(lemmalist(i[0]))
	temp1=[]
	temp2=[]
	for i in final_list:
		temp1=[]
		for j in i:
			if j.find('_')!=-1:
				j=j.replace('_',' ')
				temp1.append(j)
			else:	
				j=' '+j+' '
				temp1.append(j)
		temp2.append(temp1)
	final_list=temp2
	#print final_list
	if match_no==-1:
		search_all(final_list)
	else:
		search1(match_no,final_list)
	return


while 1:
	str1=raw_input()
	ans_list=[]
	if str1=="q":
		break
	do_something(str1)
	if ans_list:
		print ans_list[0]
	else:
		print "NONE"

