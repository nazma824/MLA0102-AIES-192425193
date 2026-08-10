% --- Gender Facts ---
female(pam).
female(liz).
female(ann).
female(pat).
male(tom).
male(bob).
male(jim).
% --- Parent Facts ---
parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(pat, liz).
parent(bob, ann).
parent(liz, ann).
parent(bob, jim).
parent(liz, jim).
% --- Mother Relation ---
mother(X, Y) :-
    female(X),
    parent(X, Y).
% --- Father Relation ---
father(X, Y) :-
    male(X),
    parent(X, Y).
% --- Grandfather Relation ---
grandfather(X, Y) :-
    male(X),
    parent(X, Z),
    parent(Z, Y).
% --- Grandmother Relation ---
grandmother(X, Y) :-
    female(X),
    parent(X, Z),
    parent(Z, Y).
% --- Sister Relation ---
sister(X, Y) :-
    female(X),
    parent(P, X),
    parent(P, Y),
    X \= Y.
% --- Brother Relation ---
brother(X, Y) :-
    male(X),
    parent(P, X),
    parent(P, Y),
    X \= Y.
