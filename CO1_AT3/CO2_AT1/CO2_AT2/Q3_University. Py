% University Examination Scheduling

slot(t1).
slot(t2).
slot(t3).
slot(t4).

% Conflict relationships
conflict(e1, e2).
conflict(e1, e3).
conflict(e2, e4).
conflict(e3, e5).
conflict(e4, e6).
conflict(e2, e5).

% Schedule all examinations
schedule([e1-E1, e2-E2, e3-E3, e4-E4, e5-E5, e6-E6]) :-

    slot(E1),
    slot(E2),
    slot(E3),
    slot(E4),
    slot(E5),
    slot(E6),

    E1 \= E2,
    E1 \= E3,
    E2 \= E4,
    E3 \= E5,
    E4 \= E6,
    E2 \= E5.
