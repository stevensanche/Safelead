'''
CIS 122 Spring 2022 Project 3-1
Author(s): Steven Sanchez-Jimenez
Credit: CIS 122 Resources only
Description: Safelead
'''
def safe_lead(lead, possession, time):
    '''
    This function will be the determant of what is a safe lead and what isn't
    safe_lead(7, True, 20)
    This is a safe lead.
    safe_lead(7, False, 20)
    This lead is not safe!
    safe_lead(2, True, 10)
    This lead is not safe!
    '''
    lead = lead - 3
    if (possession==True): #This is looking to see if the winning team has the ball
        lead = lead + 0.5
    else:
        lead = lead - 0.5
    lead = lead**2 #This input is to ^2 the points
    if (lead > time):
        print ('This is a safe lead')
    else: #This input here is to print if the lead is either safe or not
        print ('This lead is not safe')
    return

def main():
    '''
    This will be the main function, which will be doing all of the computing
    '''
    lead = input('How many points is the team ahead:')
    lead = int(lead) #This will change the input string to a integer
    possession = input('Does the team have the ball? (Yes / No):')
    if possession == 'Yes':
        ball_carrier = True
    else:
        ball_carrier = False
    time = input('How much time is there left in the game?')
    time = int(time) #We have converted another input into an integer
    
    safe_lead(lead, possession, time)
    return

    
    



