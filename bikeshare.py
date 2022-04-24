from itertools import combinations
from re import I
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('There are data for only 3 cities: Chicago, New york city and Washington')
    print('Valid month names are: All or January-June ')
    print('Valid date names are: All or Sunday-Saturday')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    cities = ['chicago','new york city', 'washington' ]
    correct_months=['january', 'february', 'march', 'april', 'may', 'june','all']
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

    '''Get User Input for City, Month and Day'''
    city=''
    month=''
    day=''
    x=True
    while x is True:
        city_input=(input('Which city would you like to investigate ?')).lower()
        if city_input in cities:
            city=city_input
            break
        else:    
            print('Your City input is not valid. Kindly input chicago,new york city or washington')
            x=True
        
    while x is True:   
        month_input=(input('Which month would you like to filter by ?')).lower()
        if month_input in correct_months:
            month=month_input
            break
        else:    
            print('Your Month input is not valid.')
            x=True
    while x is True:
        day_input=(input('Which day would you like to filter by ?')).lower()
        if day_input in days:
            day=day_input
            break
        else:    
            print('Your City input is not day.')
            x=True
        

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe !
    df = pd.read_csv(CITY_DATA[city])

    # convert the StartTime column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #extract hour from Start Time to create hour column
    df['hour'] =df['Start Time'].dt.hour

     # filter by month if applicable
    if month != 'all':

        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
    
        # filter by month to create the new dataframe
        df = df[df['month'] ==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] ==day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month!
    print('The Most common month:', df['month'].mode()[0])

    # TO DO: display the most common day of week!
    print('The Most common day:', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('The Most frequent month:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("Weldone")


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print(df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    
    df['combination']=df['Start Station'] +  ' || ' + df['End Station']
    print(df['combination'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time :', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('The mean travel time :', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print('The UserType count:', df['User Type'].value_counts())
    except KeyError:
        print('No UserType column found')



    # TO DO: Display counts of gender
    try:
        print("The Gender count:", df['Gender'].value_counts())
    except KeyError:
        print('No Gender column found')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The Earliest Birth year :', df['Birth Year'].min())
        print('The Most recent Birth year :', df['Birth Year'].max())
        print('The Most Occurred Birth year :', df['Birth Year'].mode()[0])

    except KeyError:
        print('No Birth year column found')
    



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays rows rows of individual trip data based on user input."""
    print('\ndisplaying individual trip data...\n')
    start_time = time.time()
    
    view_data = (input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')).lower()
    start_loc = 0
    while view_data != 'no':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
    print('you are done viewing individual trip data')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
