% Domains: available slots
slot(slot1).
slot(slot2).
slot(slot3).

% Conflicts between subjects
conflict(math, physics).
conflict(chemistry, cs).

% Assign subjects to slots
schedule(Schedule) :-
    Schedule = [ (math, MSlot),
                 (physics, PSlot),
                 (chemistry, CSlot),
                 (cs, CSlot2) ],

    slot(MSlot), slot(PSlot), slot(CSlot), slot(CSlot2),

    % Constraints: no conflicts in same slot
    (MSlot \= PSlot),
    (CSlot \= CSlot2).
