bird(eagle).
bird(sparrow).
bird(penguin).

cannot_fly(penguin).

fly(X) :-
    bird(X),
    \+ cannot_fly(X).
