# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
from datetime import datetime
import sys
import fire
import questionary
from pathlib import Path

from qualifier.utils.fileio import load_csv, save_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value


def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """
    # It's better to use path function of the questionary module versus text function. It allows to interactively specify the right path to the target file. When it prompts a file path TAB can be used to navigate.
    csvpath = questionary.path("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


def get_applicant_info():
    """Initiates the dialog to gather the clien's financial information.

    Returns:
        Returns the applicant's financial information.
    """
    def get_correct_applicant_info(requested_integer_info):
        """Prompt dialog to get the applicant's financial information. Checks if the inputted data can be converted to an integer value. If yes, it breaks while cycle and retuns the integer value of the inputted data. If no, it catches a ValueError to print an error message and prompts user to enter a new data. This function will repeatedly prompt user to enter the data until getting the expected integer value.

        Args:
            requested_integer_info (String): The piece of the requested info to show a corresponding prompt
        
        Returns:
            Returns the applicant's financial information.
        """   
        while True:
            try:
                client_data = int(questionary.text(f"What's your {requested_integer_info}?").ask())
                break
            except ValueError:
                print("Opps! That was not valid inpud. It should be an integer value. Please try one more time!")
        return client_data
    
    credit_score = get_correct_applicant_info("credit score")  
    debt = get_correct_applicant_info("current amount of monthly debt")  
    income = get_correct_applicant_info("total monthly income")
    loan_amount = get_correct_applicant_info("desired loan amount")
    home_value = get_correct_applicant_info("home value")

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered


def save_qualifying_loans(qualifying_loans, data_header):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
        data_header (list): The list of the data headers
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!
    choice_to_save_data = questionary.confirm("Do you want to save the result to CSV file?").ask()
    if choice_to_save_data:
        # Using here the option to save qualifying loans of the user based on the user's data (first and last name), the current data and time. All results will be stored in data/Results folder. This approach allows to: 1. keep all results in one target folder that stores the results of Loan Qualifier work prepared for the particular user on the particular date 2. identify the user's file in the target folder based on user's data and date 3. get rid of a number of folders/files with custom names
        # This implementation replaces the following user story:
        #Given that I have a list of qualifying loans, when I choose to save the loans, the tool should prompt for a file path to save the file.
        
        csv_file_name = str(questionary.text("Please enter your first and last name").ask())
        name_parts = csv_file_name.lower().split(" ")
        file_name = ""
        for part in name_parts:
            file_name = file_name + part + "_"
        file_name = file_name + datetime.now().strftime("%m%d%y_%H%M") + ".csv"
        path_to_scv = Path("data/Results/" + file_name)
        save_csv(path_to_scv, qualifying_loans, data_header)
        print(f"The data about all qualifying loans was successfully saved in data/Results folder. The file name is {file_name}")
    else:
        # Modification - if user doesn't want to save the results to csv file the app will prompt to print the short readable version of the results on the screen
        choice_to_show_data = questionary.confirm("Do you want to show the results on the screen?").ask()
        if choice_to_show_data:
            break_line = "---------------------------------------------------------" # Just a break line to split the results on the screen
            print(break_line)
            for index, loan in enumerate(qualifying_loans): # Using enumerate class to access the index
                lender = loan[0]
                max_loan_amount = loan[1]
                interest_rate = loan[5]
                print(f"{index+1}. {lender}\n-Maximum loan amount: ${max_loan_amount}\n-Interest rate: {interest_rate}%\n{break_line}")

    

def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data_header, bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )
        
    # Save qualifying loans if the list is not empty
    # It doesn't make sense to prompt a user to save the results to file when there are no results - empty list returned by find_qualifying_loans function
    if len(qualifying_loans) != 0:
        save_qualifying_loans(qualifying_loans, bank_data_header)


if __name__ == "__main__":
    fire.Fire(run)
