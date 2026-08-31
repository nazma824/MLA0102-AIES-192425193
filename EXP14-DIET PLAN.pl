% Diet Recommendation Expert System

diet(Age, BMI, diabetes, Plan) :-
    Age >= 18, BMI >= 25,
    Plan = 'Low sugar and low calorie diet'.

diet(Age, BMI, hypertension, Plan) :-
    Age >= 18, BMI >= 25,
    Plan = 'Low salt and low fat diet'.

diet(Age, BMI, none, Plan) :-
    Age >= 18, BMI >= 18.5, BMI < 25,
    Plan = 'Balanced healthy diet'.

diet(Age, BMI, none, Plan) :-
    Age >= 18, BMI < 18.5,
    Plan = 'High calorie nutritious diet'.

diet(Age, BMI, none, Plan) :-
    Age >= 18, BMI >= 25,
    Plan = 'Low calorie high fiber diet'.
