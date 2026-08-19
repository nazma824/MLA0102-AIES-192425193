% Planet Knowledge Representation

% Planet facts
planet(mercury, terrestrial).
planet(venus, terrestrial).
planet(earth, terrestrial).
planet(mars, terrestrial).
planet(jupiter, gas_giant).
planet(saturn, gas_giant).
planet(uranus, ice_giant).
planet(neptune, ice_giant).

% Additional facts
has_moon(earth, 1).
has_moon(mars, 2).
has_moon(jupiter, 95).
has_moon(saturn, 146).

% Rules for logical inference
terrestrial_planet(X) :-
    planet(X, terrestrial).

gas_giant_planet(X) :-
    planet(X, gas_giant).

ice_giant_planet(X) :-
    planet(X, ice_giant).

planet_with_moons(X) :-
    has_moon(X, N),
    N > 0.
