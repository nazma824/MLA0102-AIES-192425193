% Fruit Color Classification using Production Rules

fruit(apple, red).
fruit(banana, yellow).
fruit(orange, orange).
fruit(grape, purple).
fruit(lime, green).

% Production Rules
classify(Fruit, red_fruit) :-
    fruit(Fruit, red).

classify(Fruit, yellow_fruit) :-
    fruit(Fruit, yellow).

classify(Fruit, orange_fruit) :-
    fruit(Fruit, orange).

classify(Fruit, purple_fruit) :-
    fruit(Fruit, purple).

classify(Fruit, green_fruit) :-
    fruit(Fruit, green).
