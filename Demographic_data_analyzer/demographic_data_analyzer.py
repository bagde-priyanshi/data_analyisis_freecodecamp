import pandas as pd

def calculate_demographic_data(print_data=True):

    columns = [
        "age",
        "workclass",
        "fnlwgt",
        "education",
        "education-num",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "capital-gain",
        "capital-loss",
        "hours-per-week",
        "native-country",
        "salary"
    ]

    df = pd.read_csv(
        "adult.data.csv",
        names=columns,
        sep=",",
        skipinitialspace=True
    )

    print(df.head())
    print(df.columns)

    race_count = df["race"].value_counts()

    print(race_count)
    race_count = df["race"].value_counts()
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    advanced_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_education = df[advanced_education]
    lower_education = df[~advanced_education]

    higher_education_rich = round((higher_education["salary"] == ">50K").mean() * 100, 1)
    lower_education_rich = round((lower_education["salary"] == ">50K").mean() * 100, 1)

    min_work_hours = df["hours-per-week"].min()
    num_min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round((num_min_workers["salary"] == ">50K").mean() * 100, 1)

    country_salary = df[df["salary"] == ">50K"]["native-country"].value_counts()
    country_total = df["native-country"].value_counts()
    highest_earning_country = (country_salary / country_total * 100).idxmax()
    highest_earning_country_percentage = round((country_salary / country_total * 100).max(), 1)

    india_rich = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print(f"Country with highest percentage of rich: {highest_earning_country}")
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print(f"Top occupations in India among those who earn >50K: {top_IN_occupation}")

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }