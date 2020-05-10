from nltk.tokenize import TreebankWordTokenizer
from collections import Counter
import csv


tokenizer = TreebankWordTokenizer()
cnt1 = Counter()
cnt2 = Counter()
cnt3 = Counter()

f1 = open('source_segment.txt', 'r').readlines()
f2 = open('target_segment.txt', 'r', encoding='utf-8').readlines()

l1 = open("english.txt", 'r').readlines()
L1 = [line.rstrip('\n') for line in l1]
l2 = open("french.txt", 'r').readlines()
L2 = [line.rstrip('\n') for line in l2]

C1 = 0
C2 = 0
C3 = 0

for line1, line2 in zip(f1, f2):        
    source_token = tokenizer.tokenize(line1)
    count_source_token = len(source_token)
    source_filtered_words = [w for w in source_token if not w in L1 and not w in [i.capitalize() for i in L1] ]
    count_source_filtered_words = len(source_filtered_words)
    function_words_source_segment = count_source_token - count_source_filtered_words
    N1 = count_source_token - function_words_source_segment

    target_token = tokenizer.tokenize(line2)
    count_target_token = len(target_token)
    target_filtered_words = [w for w in target_token if not w in L2 and not w in [i.capitalize() for i in L2]]
    count_target_filtered_words = len(target_filtered_words)
    function_words_target_segment = count_target_token - count_target_filtered_words
    N2 = count_target_token - function_words_target_segment

    count_bilingual_segments = sum(1 for lilne1, line2 in zip(f1, f2))

    print("\n##############################################")

    print("\nTokenized word of Source Segment: \n")
    print(source_token)
    print("\nSource segment token word count: ", count_source_token)
    print("\nTokenized word of target Segment: \n")
    print(target_token)
    print("\nTarget segment token word count: ", count_target_token)
    print("\n\nFilter of the tokenized word from source segment: ")
    print(source_filtered_words)
    print("\nWord count of source segment after filtering: ", count_source_filtered_words)
    print("\nFilter of the tokenized word from target segment: \n")
    print(target_filtered_words)
    print("\nWord count of target segment after filtering: ", count_target_filtered_words)

    print("\nNumber of function word in source segment: ", function_words_source_segment)
    print("\nNumber of function word in target segment: ", function_words_target_segment)
    
    print("\n\nNumerical value of content words for each of source segments, N1: ", N1)
    print("\nNumerical value of content words for each of target segments, N2: ", N2)

    if N1 == N2:
        print("\nNo meaning-based translation error")
        cnt1[line1,line2] += 1
        C1 = sum(1 for line1,line2 in cnt1)
    elif N1>N2:
        print("\nA potential omission has been detected.")
        cnt2[line1,line2] += 1
        C2 = sum(1 for line1,line2 in cnt2)
    else:
        print("\nA potential addition has been detected.")
        cnt3[line1,line2] += 1
        C3 = sum(1 for line1,line2 in cnt3)

        

print('\n\n##### STATISTICS ######')
print('\nNumber of analyzed bilingual segment pairs from both file: ', count_bilingual_segments, 'pairs')
print('\nNumber of potentially correct translations: ', C1)
print('\nNumber of potential omission: ', C2)
print('\nNumber of potential addition: ', C3)





        

    






