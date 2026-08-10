color(red).
color(green).
color(blue).
mapcolor(A, B, C, D) :-
    color(A),
    color(B),
    color(C),
    color(D),
    A \= B,
    A \= C,
    B \= C,
    C \= D,
    B \= D.
