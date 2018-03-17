from collections import Counter
import matplotlib.pyplot as plt
import webget
import gzip

# get URL and download the fil by webget
url = 'https://datasets.imdbws.com/title.basics.tsv.gz'
webget.download(url)

print('*********************************** Question 1 ********************************')

def question1(url):
    # created a new empty array
    startYears = []
    counter = 0
    # the opreator pointed to the fil without saving it
    with gzip.open(url.split('/')[-1],'rb') as gz_file:
        for line in gz_file:
            # check columns value are 'movie'
            if line.split(b'\t')[1].decode('ascii') == 'movie':
                # added year to the array
                # decode('ascii') decode line to string from binary object
                startYears.append(line.split(b'\t')[5].decode('ascii'))
                counter += 1
    # counted the array list, return a tuple object
    c_startYear = Counter(startYears)
    # given 3 most frequent elements saved in a new object
    most_3_year = c_startYear.most_common(4)
    # print top 1 of those year 
    print('The most movies released year was:')
    print(most_3_year[1])
    # print top 3 of those years
    print('The most 3 movies released year was:')
    print(most_3_year[1:])
    # print all years of movies
    print('Number of all years of movies:')
    print(counter)

# call the function    
question1(url)

print('*********************************** Question 2 ********************************')

def question2(url):
    # created a new empty array
    endYears = []
    counter = 0
    # the opreator pointed to the fil without saving it
    with gzip.open(url.split('/')[-1],'rb') as gz_file:
        for line in gz_file:
            # check columns value are 'tvSeries'
            if line.split(b'\t')[1].decode('ascii') == 'tvSeries':
                # added year to the array
                # decode('ascii') decode line to string from binary object
                endYears.append(line.split(b'\t')[6].decode('ascii'))
                counter += 1

    # counted the array list, return a tuple object
    c_endYear = Counter(endYears)
    # given 3 most frequent elements saved in a new object
    most_3_year = c_endYear.most_common(4)
    # print top 1 of those year 
    print('The most series ended year was:')
    print(most_3_year[1])
    # print top 3 of those years
    print('The most 3 series ended year was:')
    print(most_3_year[1:])
    # print all series years
    print('Number of all ended years of series:')
    print(counter)

question2(url)

print('*********************************** Question 3 ********************************')

def question3(url):
    # created a new empty array
    runtimes = []
    # the opreator pointed to the fil without saving it
    with gzip.open(url.split('/')[-1],'rb') as gz_file:
        for line in gz_file:
            # added year to the array
            # decode('ascii') decode line to string from binary object
            runtimes.append(line.split(b'\t')[7].decode('ascii'))
    
    # removed duplicates
    number_lst = list(set(runtimes))
    # clean up
    number_lst.remove('runtimeMinutes')
    number_lst.remove('\\N')
    # convered to a number list
    new_lst = list(map(int,number_lst))
    #new_lst.sort(reverse=True)
    print('The longest runtime per movies was:')
    print(max(new_lst))

question3(url)


print('*********************************** Question 4 ********************************')

def question4(url):
    # created a new empty array
    genres_lst = []
    # the opreator pointed to the fil without saving it
    with gzip.open(url.split('/')[-1],'rb') as gz_file:
        for line in gz_file:
            if line.split(b'\t')[1].decode('ascii') == 'movie':
                # added year to the array
                # decode('ascii') decode line to string from binary object
                genres_lst.append(line.split(b'\t')[8].decode('ascii'))
    # remove \n from the list
    lst = list(map(lambda x : x.strip(), genres_lst))
    # counted the array list, return a tuple object
    c_genres = Counter(lst)
    # given 3 most frequent elements saved in a new object
    most_3_genres = c_genres.most_common(3)
    # given 1 most frequent elements saved in a new object
    print('The genre covers the most movies was:')
    print(most_3_genres[0])

question4(url)

print('*********************************** Question 5 ********************************')

def question5(url):
    # created a new empty array
    runtimes = []
    # the opreator pointed to the fil without saving it
    with gzip.open(url.split('/')[-1],'rb') as gz_file:
        for line in gz_file:
            # added year to the array
            # decode('ascii') decode line to string from binary object
            runtimes.append(line.split(b'\t')[7].decode('ascii'))
    
    # removed duplicates
    number_lst = list(set(runtimes))
    # clean up
    number_lst.remove('runtimeMinutes')
    number_lst.remove('\\N')
    # convered to a number list
    new_lst = list(map(int,number_lst))
    # average
    average = int(sum(new_lst) / len(new_lst) + 1)
    print('The average runtime on adult films')
    print(average)

question5(url)

"""
# Set chart title and label axes. 
title = 'The most movies released year - {} to {}'
plt.title(title, fontsize =24)
plt.xlabel('Year', fontsize = 14)
plt.ylabel('Released movies', fontsize = 14)
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)
plt.show()"""