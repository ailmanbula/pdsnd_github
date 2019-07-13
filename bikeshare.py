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
    print('Hello!, I am Aliyu  Let\'s explore some US bikeshare data!\n')
    print('here are the names of the cities you can explore:\n Chicago\n new york city\n Washington ')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input ('please enter the name of the city you would like to analize\n\n')
        city = city.lower()
        if city not in ['chicago','new york city','washington']:
            print ('Ooops, we dont have a city named {}'.format(city))
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('please enter the month you want to view by typiny: january, february, march, april, may, june \n or type all if you want no filter\n\n' )
        month = month.lower()
        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('Ooops; it appers you have made a wrong input, kindly check and re-enter a valid month')
            continue
        else:
            break



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('please enter a day of the week to filter by\n\n')
        day = day.capitalize()
        if day not in ['all','Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',]:
            print('Ooops, {} is not a valid day'.format(day))
            continue
        else:
            break

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
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #to load city DataFrame
    df = pd.read_csv(CITY_DATA[city])

    #converting start_time column to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #To extract a column for months from the start_time columnn
    df['month'] = df['Start Time'].dt.month

    #to extract a day_of_week column from start_time columnn
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #to extract an hour column from the start_time columnn
    df['hour'] = df['Start Time'].dt.hour

    # filtering by month if applicable
    if month != 'all':

        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = month.capitalize()
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filtering by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_popular_month = df['month'].mode()[0]
    print('the most common month is ',most_popular_month )


    # TO DO: display the most common day of week
    most_popular_day = df['day_of_week'].mode()[0]
    print('the most popular day of the week is ',most_popular_day)


    # TO DO: display the most common start hour
    most_popular_start_hour = df['hour'].mode()[0]
    print('the most popular starting hour is ',most_popular_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().reset_index()['index'][0]
    print ('the most commonly used start station is ',start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().reset_index()['index'][0]
    print('the most commonly used end station is ',end_station)


    # TO DO: display most frequent combination of start station and end station trip
    station_combo = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(station_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #this displays total travel time; this converts the total time traveled
    #in days by deviding the total time in seconds by 86400.

    total_time_traveled = sum(df['Trip Duration'])
    print('Total travel time (in days):', total_time_traveled/86400, " Days")



    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('we have the following categories of users:\n', user_types)

    # TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print('\nGender Types:\n', genders)
    except:
        print('\nfor user destribution according to gender \nno gender data available for this city.')

        # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('\nthe earliest year of birth is ',earliest_year)
    except:
        print('\nfor earliest birth year \nno birth data available for this city.')

    try:
        most_recent_year = df['Birth Year'].max()
        print('\nthe most recent birth year is ', most_recent_year)
    except:
        print('\nfor most recent birth year \nno birth data available for this city.')

    try:
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('\nthe most common birth year is ', most_common_year)
    except:
        print('\nfor most common birth year  \nno birth data available for this city.')




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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
