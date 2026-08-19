% Initial Facts
fact(computer_not_starting).
fact(dim_headlights).

% Rules
rule(battery_problem, [computer_not_starting, dim_headlights]).
rule(battery_inspection, [battery_problem]).
rule(marked_for_service, [battery_inspection]).

% Forward Chaining
forward_chain(Goal) :-
    write('Goal: '), write(Goal), nl,
    findall(X, fact(X), Facts),
    forward(Facts, Goal).

% Goal already available
forward(Known, Goal) :-
    member(Goal, Known),
    write('Fact/Conclusion found: '), write(Goal), nl,
    !.

% Apply a rule and continue forward
forward(Known, Goal) :-
    rule(NewFact, Conditions),
    \+ member(NewFact, Known),
    all_known(Conditions, Known),
    write('Rule applied: '), write(NewFact), nl,
    append(Known, [NewFact], Updated),
    forward(Updated, Goal),
    !.

% If no rule can derive the goal
forward(_, Goal) :-
    write('Cannot derive: '), write(Goal), nl,
    fail.

% Check all conditions
all_known([], _).

all_known([H|T], Known) :-
    member(H, Known),
    all_known(T, Known).
