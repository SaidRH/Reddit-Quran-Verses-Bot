from threading import Thread
import praw


cfile = open("Counter.txt")
all_lines_variable_cfile = cfile.readlines()
increamentedValue = int(all_lines_variable_cfile[0])

def func():
    #Visit the url to fill the informations below: https://praw.readthedocs.io/en/v3.6.2/pages/oauth.html
    reddit = praw.Reddit(client_id='',
                     client_secret='',
                     username='',
                     password='',
                     user_agent='')

    fileone = open("PostTitle.txt", encoding="utf8")
    filetwo = open("PostBodyAR.txt", encoding="utf8")
    filethree = open("PostBodyEN.txt", encoding="utf8")
    filefour = open("Links.txt", encoding="utf8")
    
    all_lines_variable_fileone = fileone.readlines()
    all_lines_variable_filetwo = filetwo.readlines()
    all_lines_variable_filethree = filethree.readlines()
    all_lines_variable_filefour = filefour.readlines()

    
    title = all_lines_variable_fileone[increamentedValue]
    
    selftext  = all_lines_variable_filetwo[increamentedValue]+\
                all_lines_variable_filethree[increamentedValue]+\
                all_lines_variable_filefour[increamentedValue]
    
    reddit.subreddit('PutTheSubredditNameHere').submit(title,selftext)
    reddit.message('PutTheSubredditNameHere').submit(title,selftext)

    
        
if __name__ == '__main__':
 Thread(target = func).start()   

increamentedValue+=1
Cfile = open("Counter.txt","w").write("%d" %increamentedValue)

