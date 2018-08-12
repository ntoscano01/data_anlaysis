# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 18:11:09 2018

@author: Nick
"""
import time
import pandas as pd
import numpy as np
import json

## Filenames
#chicago = 'chicago.csv'
#new_york_city = 'new_york_city.csv'
#washington = 'washington.csv'

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#-----------------------------------------------------------------------------------------------------------------------------------

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(str('\nWhich city would you like to see data on?\n'
                        '\nNew York City, Chicago, or Washington\n '))
        if city in('washington', 'chicago', 'new york city'):
            break
        elif city == 'new york':
            city += ' city'
            break
        else:
            print('\n\nYour answer does not match any of the above options, please try again!\n')    

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april','may', 'june', 'all']

    while True:
        month = input(str('\nWould you like to search by one of the following months?\nEnter January, February, March, April, May, June, or all?\n '))
        if month in months:
            break
        else:
            print ('Your answer does not match any of the above options, please try again!\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday, thursday, friday', 'saturday', 'sunday']

    while True:
        day = input(str('\nWould you like to search by one of the following days?\nSunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or all?\n' ).lower())
        if day in days:
            break
        else:
            print ('Your answer does not match any of the above options, please try again!\n')   
                      

    print('-'*40)
    return city, month, day  

#-----------------------------------------------------------------------------------------------------------------------------------

def load_data(city, month, day):

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
 
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
 
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
 
 
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april','may', 'june']
        month = months.index(month) + 1
 
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
 
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
  
    return df

#-----------------------------------------------------------------------------------------------------------------------------------

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
 
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
 
    # display the most common month
    popular_month = df['month'].mode()[0]
    print("The most common month of travel was " + str(popular_month) + ".\n")
 
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day of travel was " + popular_day + ".\n")
 
    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
 
    popular_hour = df['hour'].mode()[0]
    print("The most common hour of travel was " + str(popular_hour) + ".\n")
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
#-----------------------------------------------------------------------------------------------------------------------------------    
    
def station_stats(df):
      
    """Displays statistics on the most popular stations and trip."""
 
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()    
    
    row_length = df.shape[0]

    # iterate from 0 to the number of rows in steps of 5
    for i in range(0, row_length, 5):
        
        yes = input('\nWould you like to examine the particular user trip data? Type \'yes\' or \'no\'\n> ')
        if yes.lower() != 'yes':
            break
        
        # retrieve and convert data to json format
        # split each json row data 
        row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')
        for row in row_data:
            # pretty print each user data
            parsed_row = json.loads(row)
            json_row = json.dumps(parsed_row, indent=2)
            print(json_row)
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
#-----------------------------------------------------------------------------------------------------------------------------------

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
 
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
 
    # display total travel time
    m, s = divmod(int(df['Trip Duration'].sum()), 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print("Total bikeshare travel time: " + str(d) + " days, " + str(h) + " hours, " + str(m) + " minutes, " + str(s) + " seconds.")
 
    # display mean travel time
    m, s = divmod(int(df['Trip Duration'].mean()), 60)
    h, m = divmod(m, 60)
    print("Average bikeshare travel time: " + str(h) + " hours, " + str(m) + " minutes, " + str(s) + " seconds.")
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-----------------------------------------------------------------------------------------------------------------------------------    

def display_data(df, current_line):
    
    print('\nPreparing individual trip data...\n')
    start_time = time.time()
    
    display = input('\nWould you like to view individual trip data?'
                    ' Type \'yes\' or \'no\'.\n')
    display = display.lower(df)
    if display == 'yes' or display == 'y':
        print(df.iloc[current_line:current_line+5])
        current_line += 5
        return display_data(df, current_line)
        if display == 'no' or display == 'n':
            return
    else:
        print("\nI'm sorry, I'm not sure if you wanted to see more data or not. Let's try again.")
        return display_data(df, current_line)
                    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-----------------------------------------------------------------------------------------------------------------------------------
    
def user_stats(df, city):
    """Displays statistics on bikeshare users."""
 
    print('\nCalculating User Stats...\n')
    start_time = time.time()
 
    #  Display counts of user types
    print("Here's a breakdown of bikeshare user types...")
    print(df['User Type'].value_counts())
 
    # Display counts of gender
    if city in ('washington'):
        print("\nSorry, gender statistics for Washington are not available.")
    else:
        print("\nHere's a breakdown of gender among bikeshare users...")
        print(df['Gender'].value_counts())
 
    # Display earliest, most recent, and most common year of birth
    if city in ('washington'):
        print("\nSorry, birth year statistics for Washington are not available.")
    else:
        print("\nAnd lastly, some information on bikeshare users' birth years...")
        print("Earliest birth year among bikeshare users: " + str(int(df['Birth Year'].min())))
        print("Most recent birth year among bikeshare users: " + str(int(df['Birth Year'].max())))
        print("Most common birth year among bikeshare users: " + str(int(df['Birth Year'].mode()[0])))
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-----------------------------------------------------------------------------------------------------------------------------------

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()