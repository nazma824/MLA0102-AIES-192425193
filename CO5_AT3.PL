% ============================================
% Agricultural Crop Disease Diagnosis - Expert System
% ============================================

% ---------- FACTS (sample field observation for crop1) ----------
leaf_colour(crop1, yellow).
leaf_spots(crop1, yes).
spot_colour(crop1, brown).
soil_condition(crop1, waterlogged).
humidity(crop1, high).

% Additional sample crops to demonstrate other diseases
leaf_coating(crop2, white_powdery).
humidity(crop2, high).

wilting(crop3, sudden).
soil_condition(crop3, waterlogged).

wilting(crop4, gradual).
soil_condition(crop4, waterlogged).
root_condition(crop4, soft_brown).

leaf_spots(crop5, yes).
spot_colour(crop5, orange).
humidity(crop5, high).

pest_observed(crop6, yes).
leaf_holes(crop6, yes).

% ---------- RULES ----------

disease(X, leaf_blight) :-
    leaf_colour(X, yellow),
    leaf_spots(X, yes),
    spot_colour(X, brown).

disease(X, powdery_mildew) :-
    leaf_coating(X, white_powdery),
    humidity(X, high).

disease(X, bacterial_wilt) :-
    wilting(X, sudden),
    soil_condition(X, waterlogged).

disease(X, root_rot) :-
    wilting(X, gradual),
    soil_condition(X, waterlogged),
    root_condition(X, soft_brown).

disease(X, rust) :-
    leaf_spots(X, yes),
    spot_colour(X, orange),
    humidity(X, high).

disease(X, pest_infestation) :-
    pest_observed(X, yes),
    leaf_holes(X, yes).

% ---------- RECOMMENDATIONS ----------

recommendation(X, apply_fungicide) :-
    disease(X, D),
    fungicide_disease(D).

fungicide_disease(leaf_blight).
fungicide_disease(powdery_mildew).
fungicide_disease(rust).

recommendation(X, improve_drainage) :-
    disease(X, D),
    drainage_disease(D).

drainage_disease(bacterial_wilt).
drainage_disease(root_rot).

recommendation(X, apply_pesticide) :-
    disease(X, pest_infestation).

% ---------- DEMO QUERIES (auto-run on load) ----------

:- initialization(main).

main :-
    nl, write('--- Crop Disease Diagnosis Results ---'), nl,
    forall(
        member(Crop, [crop1, crop2, crop3, crop4, crop5, crop6]),
        report(Crop)
    ),
    nl.

report(Crop) :-
    ( disease(Crop, D) ->
        format("~w -> Disease: ~w", [Crop, D]),
        ( recommendation(Crop, R) ->
            format(", Recommendation: ~w~n", [R])
        ;
            nl
        )
    ;
        format("~w -> No disease matched~n", [Crop])
    ).
