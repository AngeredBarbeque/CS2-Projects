
def find_time():
    #imports specialized functions from time
    from time import strftime, gmtime
    #Returns the time formatted correctly using % to tell where each piece should slot in
    #Uses strftime to format the return of gmtime
    #used https://docs.python.org/3.3/library/time.html?highlight=time.strftime#time.strftime to find specific % needed
    return strftime('%Y-%m-%d %H:%M', gmtime())