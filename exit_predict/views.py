from django.shortcuts import render
import pandas as pd
import pickle
import os


def attrition_rate_finder(request):
    if len(request.GET) > 0:
        age = request.GET['age']
        business_travel = request.GET['business_travel']
        daily_rate = request.GET['daily_rate']
        department = request.GET['department']
        distance_from_home = request.GET['distance_from_home']
        education = request.GET['education']
        education_field = request.GET['education_field']
        env_satisfaction = request.GET['env_satisfaction']
        gender = request.GET['gender']
        job_involvement = request.GET['job_involvement']
        job_level = request.GET['job_level']
        job_satisfaction = request.GET['job_satisfaction']
        job_role = request.GET['job_role']
        marital_status = request.GET['marital_status']
        monthly_income = request.GET['monthly_income']
        num_companies_worked = request.GET['num_companies_worked']
        overtime = request.GET['overtime']
        relationship_satisfaction = request.GET['relationship_satisfaction']
        stock_level = request.GET['stock_level']
        total_working_years = request.GET['total_working_years']
        training = request.GET['training']
        worklife_bal = request.GET['worklife_bal']
        years_at_company = request.GET['years_at_company']
        years_in_current = request.GET['years_in_current']
        years_since_last_promo = request.GET['years_since_last_promo']
        years_with_manager = request.GET['years_with_manager']

        results = exit_alert(age, business_travel, daily_rate, department, distance_from_home, education,
                             education_field, env_satisfaction, gender, job_involvement, job_level,
                             job_satisfaction, job_role, marital_status, monthly_income, num_companies_worked,
                             overtime, relationship_satisfaction, stock_level, total_working_years, training,
                             worklife_bal, years_at_company, years_in_current, years_since_last_promo,
                             years_with_manager)
        print(results)
        return render(request, "results.html", {'results': results})
    if request.method == 'POST':
        if request.POST.get('attrition_button'):
            age = request.POST['age']
            business_travel = request.POST['business_travel']
            daily_rate = request.POST['daily_rate']
            department = request.POST['department']
            distance_from_home = request.POST['distance_from_home']
            education = request.POST['education']
            education_field = request.POST['education_field']
            env_satisfaction = request.POST['env_satisfaction']
            gender = request.POST['gender']
            job_involvement = request.POST['job_involvement']
            job_level = request.POST['job_level']
            job_satisfaction = request.POST['job_satisfaction']
            job_role = request.POST['job_role']
            marital_status = request.POST['marital_status']
            monthly_income = request.POST['monthly_income']
            num_companies_worked = request.POST['num_companies_worked']
            overtime = request.POST['overtime']
            relationship_satisfaction = request.POST['relationship_satisfaction']
            stock_level = request.POST['stock_level']
            total_working_years = request.POST['total_working_years']
            training = request.POST['training']
            worklife_bal = request.POST['worklife_bal']
            years_at_company = request.POST['years_at_company']
            years_in_current = request.POST['years_in_current']
            years_since_last_promo = request.POST['years_since_last_promo']
            years_with_manager = request.POST['years_with_manager']

            results = exit_alert(age, business_travel, daily_rate, department, distance_from_home, education,
                                 education_field, env_satisfaction, gender, job_involvement, job_level,
                                 job_satisfaction, job_role, marital_status, monthly_income, num_companies_worked,
                                 overtime, relationship_satisfaction, stock_level, total_working_years, training,
                                 worklife_bal, years_at_company, years_in_current, years_since_last_promo,
                                 years_with_manager)
            print(results)
            results = str(results[0])
        else:
            print('Not Working')

    else:
        results = None

    return render(request, "index.html", {'result': results})


def exit_alert(age, business_travel, daily_rate, department, distance_from_home, education,
               education_field, env_satisfaction, gender, job_involvement, job_level, job_satisfaction,
               job_role, marital_status, monthly_income, num_companies_worked, overtime,
               relationship_satisfaction, stock_level, total_working_years, training, worklife_bal, years_at_company,
               years_in_current, years_since_last_promo, years_with_manager):
    if age != "":
        df = pd.DataFrame(data=[[float(age), int(business_travel), float(daily_rate), float(distance_from_home),
                                int(education), int(env_satisfaction), int(job_involvement), int(job_level),
                                int(job_satisfaction), float(monthly_income), int(num_companies_worked),
                                int(overtime), int(relationship_satisfaction), int(stock_level),
                                int(total_working_years), int(training), int(worklife_bal),
                                int(years_at_company), int(years_in_current), int(years_since_last_promo), int(years_with_manager)]],
                          columns=['Age', 'BusinessTravel', 'DailyRate', 'DistanceFromHome', 'Education',
                                   'EnvironmentSatisfaction', 'JobInvolvement', 'JobLevel', 'JobSatisfaction',
                                   'MonthlyIncome', 'NumCompaniesWorked', 'OverTime',
                                   'RelationshipSatisfaction',
                                   'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
                                   'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
                                   'YearsSinceLastPromotion', 'YearsWithCurrManager'])

        # feature engineering
        df['MonthlyIncome/Age'] = df['MonthlyIncome'] / df['Age']
        df["Age_risk"] = (df["Age"] < 34).astype(int)
        df["DailyRate_risk"] = (df["DailyRate"] < 700).astype(int)
        df["Distance_risk"] = (df["DistanceFromHome"] >= 20).astype(int)
        df["YearsAtCo_risk"] = (df["YearsAtCompany"] < 4).astype(int)
        df['NumCompaniesWorked'] = df['NumCompaniesWorked'].replace(0, 1)
        df['AverageTenure'] = df["TotalWorkingYears"] / df["NumCompaniesWorked"]
        df['JobHopper'] = ((df["NumCompaniesWorked"] > 2) & (df["AverageTenure"] < 2.0)).astype(int)
        df["AttritionRisk"] = df["Age_risk"] + df["DailyRate_risk"] + df["Distance_risk"] + df["YearsAtCo_risk"] + df['JobHopper']

        df.drop(['YearsInCurrentRole', 'YearsWithCurrManager'], axis=1, inplace=True)

        # encoding
        encode_department(df, department)
        encode_education(df, education_field)
        encode_gender(df, gender)
        encode_job_role(df, job_role)
        encode_marital(df, marital_status)

        # load the model from disk
        filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), r'exit_predict/finalized_model2.pickle')
        loaded_model = pickle.load(open(filename, 'rb'))
        res = loaded_model.predict_proba(df)
        res_perc = res.max()
        res_ind = res.argmax()
        if res_ind == 1:
            return f'There is {res_perc:.0%} chance that the employee is about to quit.'
        else:
            return f'There is {res_perc:.0%} chance that the employee will not quit in the nearest future.'

    else:
        return None


def encode_department(df, department):
    if department == 'Human Resources':
        df['Department_Human Resources'] = 1
        df['Department_Research & Development'] = 0
        df['Department_Sales'] = 0
    if department == 'Research & Development':
        df['Department_Human Resources'] = 0
        df['Department_Research & Development'] = 1
        df['Department_Sales'] = 0
    if department == 'Sales':
        df['Department_Human Resources'] = 0
        df['Department_Research & Development'] = 0
        df['Department_Sales'] = 1


def encode_education(df, education_field):
    if education_field == 'Human Resources':
        df['EducationField_Human Resources'] = 1
        df['EducationField_Life Sciences'] = 0
        df['EducationField_Marketing'] = 0
        df['EducationField_Medical'] = 0
        df['EducationField_Technical Degree'] = 0
    if education_field == 'Life Sciences':
        df['EducationField_Human Resources'] = 0
        df['EducationField_Life Sciences'] = 1
        df['EducationField_Marketing'] = 0
        df['EducationField_Medical'] = 0
        df['EducationField_Technical Degree'] = 0
    if education_field == 'Marketing':
        df['EducationField_Human Resources'] = 0
        df['EducationField_Life Sciences'] = 0
        df['EducationField_Marketing'] = 1
        df['EducationField_Medical'] = 0
        df['EducationField_Technical Degree'] = 0
    if education_field == 'Medical':
        df['EducationField_Human Resources'] = 0
        df['EducationField_Life Sciences'] = 0
        df['EducationField_Human Resources'] = 0
        df['EducationField_Marketing'] = 0
        df['EducationField_Medical'] = 1
        df['EducationField_Technical Degree'] = 0
    if education_field == 'Technical Degree':
        df['EducationField_Human Resources'] = 0
        df['EducationField_Life Sciences'] = 0
        df['EducationField_Human Resources'] = 0
        df['EducationField_Marketing'] = 0
        df['EducationField_Medical'] = 0
        df['EducationField_Technical Degree'] = 1
    else:
        df['EducationField_Human Resources'] = 0
        df['EducationField_Life Sciences'] = 0
        df['EducationField_Human Resources'] = 0
        df['EducationField_Marketing'] = 0
        df['EducationField_Medical'] = 0
        df['EducationField_Technical Degree'] = 0


def encode_gender(df, gender):
    if gender == 'Female':
        df['Gender_Female'] = 1
        df['Gender_Male'] = 0
    if gender == 'Male':
        df['Gender_Female'] = 0
        df['Gender_Male'] = 1


def encode_job_role(df, job_role):
    # JobRole_Human Resources and JobRole_Sales Executive and JobRole_Research Scientist dropped
    if job_role == 'Healthcare Representative':
        df['JobRole_Healthcare Representative'] = 1
        df['JobRole_Laboratory Technician'] = 0
        df['JobRole_Manager'] = 0
        df['JobRole_Manufacturing Director'] = 0
        df['JobRole_Research Director'] = 0
        df['JobRole_Sales Representative'] = 0
    if job_role == 'Laboratory Technician':
        df['JobRole_Healthcare Representative'] = 0
        df['JobRole_Laboratory Technician'] = 1
        df['JobRole_Manager'] = 0
        df['JobRole_Manufacturing Director'] = 0
        df['JobRole_Research Director'] = 0
        df['JobRole_Sales Representative'] = 0
    if job_role == 'Manager':
        df['JobRole_Healthcare Representative'] = 0
        df['JobRole_Laboratory Technician'] = 0
        df['JobRole_Manager'] = 1
        df['JobRole_Manufacturing Director'] = 0
        df['JobRole_Research Director'] = 0
        df['JobRole_Sales Representative'] = 0
    if job_role == 'Manufacturing Director':
        df['JobRole_Healthcare Representative'] = 0
        df['JobRole_Laboratory Technician'] = 0
        df['JobRole_Manager'] = 0
        df['JobRole_Manufacturing Director'] = 1
        df['JobRole_Research Director'] = 0
        df['JobRole_Sales Representative'] = 0
    if job_role == 'Research Director':
        df['JobRole_Healthcare Representative'] = 0
        df['JobRole_Laboratory Technician'] = 0
        df['JobRole_Manager'] = 0
        df['JobRole_Manufacturing Director'] = 0
        df['JobRole_Research Director'] = 1
        df['JobRole_Sales Representative'] = 0
    if job_role == 'Sales Representative':
        df['JobRole_Healthcare Representative'] = 0
        df['JobRole_Laboratory Technician'] = 0
        df['JobRole_Manager'] = 0
        df['JobRole_Manufacturing Director'] = 0
        df['JobRole_Research Director'] = 0
        df['JobRole_Sales Representative'] = 1
    else:
        df['JobRole_Healthcare Representative'] = 0
        df['JobRole_Laboratory Technician'] = 0
        df['JobRole_Manager'] = 0
        df['JobRole_Manufacturing Director'] = 0
        df['JobRole_Research Director'] = 0
        df['JobRole_Sales Representative'] = 0


def encode_marital(df, marital_status):
    if marital_status == 'Divorced':
        df['MaritalStatus_Divorced'] = 1
        df['MaritalStatus_Married'] = 0
        df['MaritalStatus_Single'] = 0
    if marital_status == 'Married':
        df['MaritalStatus_Divorced'] = 0
        df['MaritalStatus_Married'] = 1
        df['MaritalStatus_Single'] = 0
    if marital_status == 'Single':
        df['MaritalStatus_Divorced'] = 0
        df['MaritalStatus_Married'] = 0
        df['MaritalStatus_Single'] = 1

