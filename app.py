import datetime
from flask import Flask, request, jsonify
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

# from app import routes

#welcome route
# @app.route('/', methods=['GET'])
# def api_welcome():
#     return jsonify({'message': 'Welcome to the API!'}), 200

# @app.route('/shout', methods=['GET'])
# def shout():
#     name = request.args.get('name',"")
#     uppercase_name= name.upper()
#     return jsonify({'message': f'Hello, {uppercase_name}!'}), 200


# #route to get full name
# @app.route('/name', methods=['GET'])
# def get_full_name():
#     first_name = request.args.get('first_name',"")
#     last_name = request.args.get('last_name',"")
#     full_name = f"{first_name} {last_name}"
#     return jsonify({'message': f'Hello, {full_name}!'}), 200


# #formate date and month

# @app.route('/date', methods=['GET'])
# def format_date():
    
#     month = request.args.get('month',"")
#     year = request.args.get('year',"")
#     formatted_date = f"{month} {year}"
#     return jsonify({'message': f'Hello, {formatted_date}!'}), 200

##greet

# @app.route('/greet', methods=['GET'])
# def greet():
#     name = request.args.get('name',"")
#     return jsonify({'message': f'Hello, {name}!'}), 200


##address
# @app.route("/address", methods=["GET"])
# def get_address():
#     address = request.args.get('address',"")
#     return jsonify({'message': f'Hello, {address}!'}), 200

# @app.route("/whisper", methods=['GET'])
# def whisper():
#     name= request.args.get("name","")
#     whisper=f'{name}, you are whispering!'
#     return name, 200


# @app.route('/productname', methods=['GET'])
# def productname():
#     companyName = request.args.get('companyName')
#     productName = request.args.get('productName')
#     fullProductName = companyName + ' ' + productName
#     return fullProductName


# @app.route('/date', methods=['GET'])
# def date():
#     month = request.args.get('month')
#     year = request.args.get('year')
#     formattedDate = month + '/' + year
#     return formattedDate

# @app.route('/greet', methods=['GET'])
# def greet():
#     city = request.args.get('city')
#     greeting = 'You live in ' + city
#     return greeting

# @app.route('/capital', methods=['GET'])
# def capital():
#     capital = request.args.get('capital')
#     country = request.args.get('country')
#     countryCapital = capital + ' is the capital of ' + country
#     return countryCapital

# @app.route('/email', methods=['GET'])
# def email():
#     firstName = request.args.get('firstName')
#     lastName = request.args.get('lastName')
#     domain = request.args.get('domain')
#     email=f"{firstName}@{lastName}.{domain}"
#     return email


# @app.route('/custom-commit', methods=['GET'])
# def custom_commit():
#     commit_type = request.args.get('type')
#     message = request.args.get('message')
#     custom_commit_message = f"{commit_type}: {message}"
#     return custom_commit_message

# @app.route('/certificate', methods=['GET'])
# def certificate():
#     first_name = request.args.get('firstName')
#     last_name = request.args.get('lastName')
#     course_name = request.args.get('courseName')
#     certificate_message = f"This certification is awarded to {first_name} {last_name} for completing the course {course_name}"
#     return certificate_message

# @app.route('/autoreply', methods=['GET'])
# def autoreply():
#     start_month = request.args.get('startMonth')
#     end_month = request.args.get('endMonth')
#     autoreply_message = f"Dear customer, thank you for reaching out to me. Unfortunately, I'm out of office from {start_month} till {end_month}. Your enquiry will be resolved by another colleague."
#     return autoreply_message


# @app.route('/secureurl', methods=['GET'])
# def secureurl():
#     domain = request.args.get('domain')
#     secure_url = f"https://{domain}"
#     return secure_url


# @app.route('/sendotp', methods=['GET'])
# def sendotp():
#     otp_code = request.args.get('otpCode')
#     otp_message = f"Your OTP for account verification is {otp_code}. Do not share this with anyone."
#     return otp_message


# @app.route('/welcome', methods=['GET'])
# def welcome():
#     first_name = request.args.get('firstName')
#     email = request.args.get('email')
#     welcome_message = f"Hey {first_name}. We're excited to have you here, we'll send future notifications to your registered mail ({email})"
#     return welcome_message


# @app.route('/github-profile', methods=['GET'])
# def github_profile():
#     username = request.args.get('userName')
#     github_url = f"https://github.com/{username}"
#     return github_url

# @app.route('/text-to-csv', methods=['GET'])
# def text_to_csv():
#     id_value = request.args.get('id')
#     email = request.args.get('email')
#     roll_number = request.args.get('rollNumber')
#     csv_row = f"{id_value}, {email}, {roll_number}"
#     return csv_row



###############operators ###

# @app.route("/total-distance", methods=['GET'])
# def total_distance():
#     distance1 =float(request.args.get('distance1', 0))
#     distance2 =float(request.args.get('distance2', 0))
#     total_distance = distance1 + distance2
#     return str(total_distance)

################################PY 1.2 - HW1

# http://127.0.0.1:5000/total-marks?marks1=70&marks2=80

# @app.route('/total-marks', methods=['GET'])
# def total_marks():
#     marks1 = int(request.args.get('marks1'))
#     marks2 = int(request.args.get('marks2'))
#     totalMarks = marks1 + marks2
#     return str(totalMarks)


# # http://127.0.0.1:5000/total-weight?weight1=3&weight2=3&weight3=5

# @app.route('/total-weight', methods=['GET'])
# def total_weight():
#     weight1 = float(request.args.get('weight1', 0))
#     weight2 = float(request.args.get('weight2', 0))
#     weight3 = float(request.args.get('weight3', 0))
#     totalWeight = weight1 + weight2 + weight3
#     return str(totalWeight)

# http://127.0.0.1:5000/monthly-salary?annualSalary=1200000

# @app.route('/monthly-salary', methods=['GET'])
# def monthly_salary():
#     annualSalary = float(request.args.get('annualSalary', 0))
#     monthlySalary = annualSalary / 12
#     return str(monthlySalary)


#http://127.0.0.1:5000/total-pages?pagesPerDay=20&days=6

# @app.route('/total-pages', methods=['GET'])
# def total_pages():
#     pagesPerDay = float(request.args.get('pagesPerDay', 0))
#     days = float(request.args.get('days', 0))
#     totalPages = pagesPerDay * days
#     return str(totalPages)


# # http://127.0.0.1:5000/currency-conversion?amount=2000&exchangeRate=0.0125

# @app.route('/currency-conversion', methods=['GET'])
# def currency_conversion():
#     amount = float(request.args.get('amount', 0))
#     exchangeRate = float(request.args.get('exchangeRate', 0))
#     convertedAmount = amount * exchangeRate
#     return str(convertedAmount)

# #http://127.0.0.1:5000/average-sales?sales1=30&sales2=35&sales3=50

# @app.route('/average-sales', methods=['GET'])
# def average_sales():
#     sales1 = float(request.args.get('sales1', 0))
#     sales2 = float(request.args.get('sales2', 0))
#     sales3 = float(request.args.get('sales3', 0))
#     averageSales = (sales1 + sales2 + sales3) / 3
#     return str(averageSales)


#PY1.2 - HW2

# # http://127.0.0.1:5000/bmi?weight=70&height=1.75

# @app.route('/bmi', methods=['GET'])
# def bmi():
#     weight = float(request.args.get('weight', 0))
#     height = float(request.args.get('height', 0))
#     bmi = weight / (height * height)
#     return f"Your BMI is {bmi:.2f}"

#  # http://127.0.0.1:5000/checkout?product=Fuse&units=2&price=40

# @app.route('/checkout', methods=['GET'])
# def checkout():
#     product = request.args.get('product')
#     units = int(request.args.get('units', 0))
#     price = float(request.args.get('price', 0))
#     totalCost = units * price
#     return f"You have bought {units} units of {product} for a total cost of {totalCost}"

# # http://127.0.0.1:5000/grade?maths=70&science=82&english=75

# @app.route('/grade', methods=['GET'])
# def grade():
#     maths = int(request.args.get('maths', 0))
#     science = int(request.args.get('science', 0))
#     english = int(request.args.get('english', 0))
#     totalMarks = maths + science + english
#     averageMarks = totalMarks / 3
#     return f"Your average marks is {averageMarks:.2f}%"



# #http://127.0.0.1:5000/discounted-price?cartTotal=150&discount=5

# @app.route('/discounted-price', methods=['GET'])
# def discounted_price():
#     cartTotal = float(request.args.get('cartTotal', 0))
#     discount = float(request.args.get('discount', 0))
#     discountedPrice = cartTotal * (1 - discount / 100)
#     return f"The discounted price is {discountedPrice:.2f}"

# #http://127.0.0.1:5000/split-bill?billAmount=150&numberOfFriends=3

# @app.route('/split-bill', methods=['GET'])
# def split_bill():
#     billAmount = float(request.args.get('billAmount', 0))
#     numberOfFriends = int(request.args.get('numberOfFriends', 0))
#     splitAmount = billAmount / numberOfFriends
#     return f"Each friend should pay {splitAmount:.2f}"


# # http://127.0.0.1:5000/celsius-to-fahrenheit?temperature=20

# @app.route('/celsius-to-fahrenheit', methods=['GET'])
# def celsius_to_fahrenheit():
#     celsius = float(request.args.get('temperature', 0))
#     fahrenheit = (celsius * 9/5) + 32
#     return f"{celsius} degrees Celsius is {fahrenheit:.2f} degrees Fahrenheit"


# #http://127.0.0.1:5000/monthly-salary?hourlyWage=2000&totalHours=160


# @app.route('/monthly-salary', methods=['GET'])
# def monthly_salary():
#     hourlyWage = float(request.args.get('hourlyWage', 0))
#     totalHours = float(request.args.get('totalHours', 0))
#     monthlySalary = hourlyWage * totalHours
#     return f"Your monthly salary is {monthlySalary:.2f}"

### if else in python


##PY1.3 - HW1

# http://127.0.0.1:5000/check-whole-number?number=10

# @app.route('/check-whole-number', methods=['GET'])
# def check_whole_number():
#     number = float(request.args.get('number', 0))
#     if number.is_integer():
#         return f"{number} is a whole number"
#     else:
#         return f"{number} is not a whole number"
    



# ### http://127.0.0.1:5000/check-equal?num1=40&num2=45


# @app.route('/check-equal', methods=['GET'])
# def check_equal():
#     num1 = float(request.args.get('num1', 0))
#     num2 = float(request.args.get('num2', 0))
#     if num1 == num2:
#         return f"{num1} and {num2} are equal"
#     else:
#         return f"{num1} and {num2} are not equal"
    


# # http://127.0.0.1:5000/check-active?isActive=true


# @app.route('/check-active', methods=['GET'])
# def check_active():
#     is_active = request.args.get('isActive').lower() == 'true'
#     result = "User is Active" if is_active else "User is not Active"
#     return result


# # http://127.0.0.1:5000/check-discount?cost=1700


# @app.route('/check-discount', methods=['GET'])
# def check_discount():
#     cost = float(request.args.get('cost'))
#     if cost >= 1000:
#         return "User is eligible for a discount"
#     else:
#         return "User is not eligible for a discount"
    


# # http://127.0.0.1:5000/check-experience?years=5


# @app.route('/check-experience', methods=['GET'])
# def check_experience():
#     years = int(request.args.get('years'))
#     if years >= 5:
#         return "Person is experienced"
#     else:
#         return "Person is not experienced"

# # http://127.0.0.1:5000/check-attendance?attendance=95


# @app.route('/check-attendance', methods=['GET'])
# def check_attendance():
#     attendance = int(request.args.get('attendance'))
#     if attendance < 50:
#         result = "Attendance is low"
#     elif attendance < 90:
#         result = "Attendance is moderate"
#     else:
#         result = "Attendance is high"
#     return result

# # http://127.0.0.1:5000/check-rating?stars=4

# @app.route('/check-rating', methods=['GET'])
# def check_rating():
#     stars = int(request.args.get('stars'))
#     if stars < 3:
#         result = "Restaurant rating is low"
#     elif stars <= 4:
#         result = "Restaurant rating is medium"
#     else:
#         result = "Restaurant rating is high"
#     return result

## PY1.3 - HW2

# http://127.0.0.1:5000/check-bmi?weight=70&height=1.75

# @app.route('/check-bmi', methods=['GET'])
# def check_bmi():
#     weight = float(request.args.get('weight', 0))
#     height = float(request.args.get('height', 0))
#     bmi = weight / (height * height)
#     if bmi < 18.5:
#         result = "Underweight"
#     elif bmi < 25:
#         result = "Normal weight"
#     else:
#         result = "Overweight"
#     return result


# # http://127.0.0.1:5000/check-performance?grade=91

# @app.route('/check-performance', methods=['GET'])
# def check_performance():
#     grade = float(request.args.get('grade'))

#     if grade >= 90:
#         performance = "excellent"
#     elif grade >= 75:
#         performance = "good"
#     elif grade >= 50:
#         performance = "average"
#     else:
#         performance = "poor"
    
#     return f"Academic performance is {performance}"



# # http://127.0.0.1:5000/check-age-group?age=25

# @app.route('/check-age-group', methods=['GET'])
# def check_age_group():
#     age = int(request.args.get('age'))

#     if age <= 12:
#         age_group = "child"
#     elif age <= 17:
#         age_group = "teenager"
#     elif age <= 64:
#         age_group = "adult"
#     else:
#         age_group = "senior"
    
#     return f"Age group is {age_group}"


# ## http://127.0.0.1:5000/check-loan-eligibility?creditScore=670

# @app.route('/check-loan-eligibility', methods=['GET'])
# def check_loan_eligibility():
#     credit_score = int(request.args.get('creditScore'))

#     if credit_score >= 750:
#         eligibility = "high"
#     elif credit_score >= 650:
#         eligibility = "medium"
#     else:
#         eligibility = "low"
    
#     return f"Loan eligibility is {eligibility}"



# #  http://127.0.0.1:5000/check-tax-bracket?income=720000

# @app.route("/check-tax-bracket", methods=["GET"])
# def check_tax_bracket():
#     income = float(request.args.get('income'))

#     if income <= 500000:
#         tax_bracket = '10% tax bracket'
#     elif income <= 1000000:
#         tax_bracket = '15% tax bracket'
#     elif income <= 1500000:
#         tax_bracket = '20% tax bracket'
#     else:
#         tax_bracket = '30% tax bracket'
    
#     return f"You fall under the {tax_bracket}"

   
# ## http://127.0.0.1:5000/check-experience?yearsOfExperience=8

# @app.route("/check-experience", methods=["GET"])
# def check_experience():
#      years_of_experience = int(request.args.get('yearsOfExperience'))

#      if years_of_experience > 5:
#         experience_level = "expert"
#      else:
#         experience_level = "beginner"
#      return f"Experience level is {experience_level}"


# PY 1.4 - HW1


# def getWelcomeMessage():
#     return "We will now learn functions!"

# @app.route('/welcome', methods=['GET'])
# def welcome():
#     return getWelcomeMessage()


# def getGreetingMessage(username):
#         return f"Hey, {username}! Are you ready to learn functions with us?"

# @app.route('/greet', methods=['GET'])
# def greet():
#     username = request.args.get('username')
    
#     return getGreetingMessage(username)
    


# def checkYearsOfExp(years_of_exp):
#         if years_of_exp > 0:
#             return "You have some experience with functions. Great!"
#         else:
#             return "No worries. You will start writing functions in no time!"
        

# @app.route('/message', methods=['GET'])
# def message():
#     years_of_exp = int(request.args.get('yearsOfExp'))
    
#     return checkYearsOfExp(years_of_exp)    
    

# @app.route('/hours', methods=['GET'])
# def hours():
#     days = int(request.args.get('days'))
#     hours = int(request.args.get('hours'))
    
#     def getTime(days, hours):
#         return days * hours
    
#     return str(getTime(days, hours))    
    
# def getModuleCompletion(username, has_completed):
#         if has_completed:
#             return f"{username} has completed the modules"
#         else:
#             return f"{username} has not completed the modules"
        
# @app.route('/module-completion-status', methods=['GET'])
# def module_completion_status():
#     username = request.args.get('username')
#     has_completed = request.args.get('hasCompleted') == 'true'  # convert to boolean
    
    
    
#     return getModuleCompletion(username, has_completed)

# def getPersonalizedGreeting(city, name):
#         return f"Hey, {name}! What's famous about {city}?"


# @app.route('/personalized-greeting', methods=['GET'])
# def personalized_greeting():
#     city = request.args.get('city')
#     name = request.args.get('name')
    
#     return getPersonalizedGreeting(city, name)

# def findAge(birthyear):
#         current_year = datetime.datetime.now().year
             
#         return current_year - birthyear
# @app.route('/find-age', methods=['GET'])
# def find_age():
#     birthyear = int(request.args.get('birthyear'))
    
#     return str(findAge(birthyear))  


# def findRequiredTime(days, hours):
#         return days * hours
# @app.route('/is-time-sufficient', methods=['GET'])
# def is_time_sufficient():
#     days = int(request.args.get('days'))
#     hours = int(request.args.get('hours'))
    
   
    
#     total_time = findRequiredTime(days, hours)
    
#     if total_time >= 30:
#         return "The time being dedicated is sufficient for learning functions"
#     else:
#         return "The time being dedicated is not sufficient for learning functions"  
    
###PY 1.4 - HW2


#http://127.0.0.1:5000/github-profile?username=ankitkumar123

def generateProfileUrl(username):
    print(username)
    return f"https://github.com/{username}"
@app.route('/github-profile', methods=['GET'])
def github_profile():
    username = request.args.get('username', "").strip()

    print(username)

    if not username:
        return "Please provide a GitHub username."
    

    return generateProfileUrl(username)


# http://127.0.0.1:5000/certificate?firstName=Amit&lastName=Ranjan&courseName=NodeJS
def generateCertificate(first_name, last_name, course_name):
    return f"This certification is awarded to {first_name} {last_name} for completing the course {course_name}"

@app.route('/certificate', methods=['GET'])
def certificate():
    first_name = request.args.get('firstName')
    last_name = request.args.get('lastName')
    course_name = request.args.get('courseName')
    return generateCertificate(first_name, last_name, course_name)




def calculateGrade(maths, science, english):
        total_marks = maths + science + english
        percentage = (total_marks / 300) * 100
        return f"Your grade in percentage is {int(percentage)}%"

@app.route('/grade', methods=['GET'])
def grade():
    maths = int(request.args.get('maths'))
    science = int(request.args.get('science'))
    english = int(request.args.get('english'))
    return calculateGrade(maths, science, english)

def splitBill(bill_amount, number_of_friends):
    split_amount = bill_amount / number_of_friends
    return f"Result: Each friend owes Rs. {split_amount:.2f} against the bill"

@app.route('/split-bill', methods=['GET'])
def split_bill():
    bill_amount = float(request.args.get('billAmount'))
    number_of_friends = int(request.args.get('numberOfFriends'))
    return splitBill(bill_amount, number_of_friends)

def calculateSalary(hourly_wage, total_hours):
    monthly_salary = hourly_wage * total_hours
    return f"Result: Your monthly salary is ₹{monthly_salary:.2f}"

@app.route('/monthly-salary', methods=['GET'])
def monthly_salary():
    hourly_wage = float(request.args.get('hourlyWage'))
    total_hours = int(request.args.get('totalHours'))
    return calculateSalary(hourly_wage, total_hours)



if __name__ == '__main__':
    app.run(debug=True)

