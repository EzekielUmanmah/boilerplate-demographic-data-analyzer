import pandas as pd
#import '//adult.data.csv'

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()#.values.tolist()

    # What is the average age of men?
    average_age_men = float('{:,.1f}'.format(df.loc[df['sex'] == 'Male','age'].mean()))

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = float('{:,.1f}'.format((df.loc[df['education'] == 'Bachelors', 'education'].value_counts().values / len(df) * 100)[0]))

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]

    lower_education = df.loc[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]

    # percentage with salary >50K
    x = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'), ['salary']] == '>50K'
    a = x[x['salary'] == True]
    higher_education_rich = float('{:,.1f}'.format(len(a) / len(x) * 100))

    x = df.loc[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')), ['salary']] == '>50K'
    a = x[x['salary'] == True]
    lower_education_rich = float('{:,.1f}'.format(len(a) / len(x) * 100))

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == df['hours-per-week'].min()]

    rich_percentage = int(len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers) * 100)

    # What country has the highest percentage of people that earn >50K?
    total_over_50k = df.loc[df['salary'] == '>50K', 'native-country'].value_counts()
    total = df.loc[df['native-country'].isin(total_over_50k.index), 'native-country'].value_counts()
    percentages = total_over_50k / total * 100
    percentages[percentages == percentages.max()]

    highest_earning_country = percentages[percentages == percentages.max()].index[0]
    highest_earning_country_percentage = float('{:,.1f}'.format(percentages[percentages == percentages.max()][0]))

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K'), 'occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
