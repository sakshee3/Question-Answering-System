import sys
import nltk
from nltk.corpus import wordnet as wn
import re
from pattern.en import singularize
import math
from text.blob import TextBlob as tb

def tf(word, blob):
	a= blob.words.count(word)*1.0
	return a / len(blob.words)

def n_containing(word, bloblist):
    	return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    	return math.log(len(bloblist) * 1.0/ (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    	return tf(word, blob) * idf(word, bloblist)

exceptions=['I','i','wa','match','most','was','is','were','over','started','first','?','']


ans_list={}
prev_lines=[]
after_ans=[]

# lemmalist is to compute similiar words
def lemmalist(str): 
	syn_set = [] 
	for synset in wn.synsets(str): 
		for item in synset.lemma_names: 
			syn_set.append(item) 
	return syn_set

def match_details(word,line):
	if line.find(word)!=-1 or line.lower().find(word)!=-1:
		#print "*********************   "+word+"        ***********************"
		return 1
	else:
		return 0

def compute_file(filename,final_list):
	file1=open(filename,'r')
	flag=0
	temp_list=[]
	for f in file1:
		f=f[:-1]
		t=0
		temp_list=[]
		for i in final_list:
			flag=0
			for j in i:
				cnt=match_details(j,f)
				if cnt==1:
					temp_list.append(j)
					flag=1
			if flag==0:
				break
		if flag==1:
			ans_list[f]=temp_list
	file1.close()
	return



def search1(match_no,final_list):
	match1='../dataset/odi'+str(match_no)+'_commentary_inn1.txt'
	match2='../dataset/odi'+str(match_no)+'_commentary_inn2.txt'
	compute_file(match1,final_list)
	compute_file(match2,final_list)
	return


def search_all(final_list):
	str1=''
	for i in range(1,6):
		str1=''
		str1=str1+'../dataset/odi'+str(i)+'_commentary_inn'
		for j in range(1,3):
			str2=''
			str2=str1
			str2=str1+str(j)+'.txt'
			compute_file(str2,final_list)
	return


main_noun_list=[]
main_verb_list=[]


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
	#print fig_of_speech
	noun='NN'
	verb='VB'
	adject='JJ'
	
	noun_list=[]
	verb_list=[]
	for i in fig_of_speech:
		noun_list=[]
		verb_list=[]
		if re.findall(noun,i[1]):
			noun_list.append(isplural(i[0]))
			main_noun_list.append(noun_list)
		if re.findall(verb,i[1]) or re.findall(adject,i[1]):
			#print i[0]
			verb_list.append(i[0])
			main_verb_list.append(verb_list)
	
	#print noun_list
	#print verb_list
	#print main_noun_list
	#print main_verb_list

	final_list=[]
	list1=[]
	for i in main_noun_list:
		list1=[]
		list1.append(i[0])
		p=lemmalist(i[0])
		for o in p:
			list1.append(o)
		final_list.append(list1)

	for i in main_verb_list:
		list1=[]
		list1.append(i[0])
		p=lemmalist(i[0])
		for o in p:
			list1.append(o)
		final_list.append(list1)

	#for i in main_verb_list:
	#	final_list.append(lemmalist(i[0]))
	#print final_list
	temp1=[]
	temp2=[]
	for i in final_list:
		temp1=[]
		for j in i:
			if j.find('_')!=-1:
				j=j.replace('_',' ')
				p = j.split(' ')
				for o in p:
					o=' '+o
					#o=' '+o+' '
					temp1.append(o)
			else:
				j=' '+j
				#j=' '+j+' '
				temp1.append(j)
		temp2.append(temp1)
	final_list=temp2
	#print final_list
	temp_list=[]
	for i in final_list:
		temp_list2=[]
		for j in i:
			if j not in temp_list2:
				temp_list2.append(j)
		temp_list.append(temp_list2)

	final_list=temp_list

	#print final_list
	if match_no==-1:
		search_all(final_list)
	else:
		search1(match_no,final_list)
	return


def isplural(pluralForm):
     singularForm = singularize(pluralForm)
     return singularForm

while 1:
	str1=raw_input()
	#list1=str1.split(' ')
	#list2=[]
	#for i in list1:
	#	list2.append(isplural(i))
	#str1=(' ').join(list2)
	#print str1
	ans_list={}
	if str1=="q":
		break
	do_something(str1)
	temp_dict={}
	common_cric={}
	common_cric['dismissed']=[' out']
	common_cric['signalled']=['taken']
	common_cric['boundary']=['four','six']
	common_cric['weather']=['sunny','windy','rainy','cold']
	#for i in ans_list:
	#	flag=0
	#	for j in main_noun_list:
	#		for o in j:
	#			for p in ans_list[i]:
	#				if j.find(p)!=-1:
	#					flag=1
	#					break
	#	if flag==1:
	#		temp_dict[i]=ans_list[i]
	compare_list=[]
	for i in common_cric:
		if str1.find(i)!=-1:
			compare_list.append(common_cric[i])

	common_list=[]
	for i in compare_list:
		for j in i:
			common_list.append(j)

	for i in main_noun_list:
		for j in i:
			common_list.append(j)

	for i in ans_list:
		print i
		print 
		print "*********************************************************" 
		print

	#ans_list=temp_dict
	#print ans_list
	#len_list=-1
	#for i in ans_list:
	#	if len(ans_list[i])>len_list:
	#		ans=i
	#		len_list=len(ans_list[i])
	#print ans
	
	#print main_noun_list
	#print main_verb_list 
	#for i in ans_list:
	#	document1=tb(i)
	#	bloblist=[document1]
	#	for j, blob in enumerate(bloblist):
    			#print("Top words in document {}".format(j + 1))
    #			scores = {word: tfidf(word, blob, bloblist) for word in ans_list[i]}
    			#print scores
	#if ans_list:
	#	print ans_list[0]
	#else:
	#	print "NONE"


