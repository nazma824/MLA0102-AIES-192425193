% Facts
symptom(fever).
symptom(cough).
symptom(body_pain).

% Rules
disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(body_pain).

disease(cold) :-
    symptom(cough),
    symptom(sneezing).

% Backward chaining predicate
backward_chain(Goal) :-
    prove(Goal).

% If the goal is already a fact, it is proved
prove(Goal) :-
    symptom(Goal).

% If the goal can be derived using a rule,
% prove all its sub-goals
prove(flu) :-
    prove(fever),
    prove(cough),
    prove(body_pain).

prove(cold) :-
    prove(cough),
    prove(sneezing).
