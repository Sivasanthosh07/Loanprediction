def response(res, loan_amount, gross_monthly_income, rate_of_interest, loan_term, Total_Monthly_Debt_Payments):
    emi_value = loan_amount * rate_of_interest * (1 + rate_of_interest)^loan_term / ((1 + rate_of_interest)^loan_term - 1)
    if res['loan_status'] == 0:
        if res['cibil_score'] < 500:
            res['reason'] = "Your Cibil Score is low. Please refer the link 'https://www.bajajfinserv.in/insights/7-guaranteed-ways-to-boost-your-cibil-score' if you want to improve Cibil Score."
        if res['loan_term'] < 5 : 
            res['reason'] = "Sorry!, Bank doesn't provide loan for less than 5 year"
        if res['income_annum'] < loan_amount :
            if Total_Monthly_Debt_Payments:
                dti_ration = Total_Monthly_Debt_Payments / gross_monthly_income
                aaproved_loan_amount = res['income_annum'] * dti_ration
                if aaproved_loan_amount < loan_amount:
                    res['reason'] = "Sorry!, Bank can approve only Rs" + aaproved_loan_amount
            else:
                res['reason']="Sorry your Salary is not sufficient for getting Loan"
        if res['bank_asset_value'] < emi_value:
          res['reason'] = "Sorry!, Your bank asset Value is less than the monthly EMI"
    return res
