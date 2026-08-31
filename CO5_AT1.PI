% ============================================================
% CYBERSECURITY THREAT DIAGNOSIS EXPERT SYSTEM
% Tool: SWI-Prolog
% ============================================================

% -------------------------
% FACTS
% -------------------------

event(repeated_login_failures).
event(unusual_network_traffic).
event(suspicious_file_activity).
event(unauthorized_access).
event(privilege_escalation).
event(unusual_login_location).
event(abnormal_data_transfer).

% -------------------------
% PRODUCTION RULES
% -------------------------

% Rule 1: Brute Force Attack
threat(brute_force_attack) :-
    event(repeated_login_failures).

% Rule 2: Network Intrusion
threat(network_intrusion) :-
    event(unusual_network_traffic),
    event(unauthorized_access).

% Rule 3: Malware Activity
threat(malware_activity) :-
    event(suspicious_file_activity),
    event(abnormal_data_transfer).

% Rule 4: Account Compromise
threat(account_compromise) :-
    event(unusual_login_location),
    event(repeated_login_failures).

% Rule 5: Privilege Escalation Attack
threat(privilege_escalation_attack) :-
    event(privilege_escalation),
    event(unauthorized_access).

% Rule 6: Insider Threat
threat(insider_threat) :-
    event(privilege_escalation),
    event(suspicious_file_activity).

% -------------------------
% RECOMMENDED ACTIONS
% -------------------------

action(brute_force_attack,
       "Lock the affected account and enable multi-factor authentication.").

action(network_intrusion,
       "Block suspicious traffic and investigate unauthorized access.").

action(malware_activity,
       "Isolate the affected system and perform malware analysis.").

action(account_compromise,
       "Reset user credentials and enable multi-factor authentication.").

action(privilege_escalation_attack,
       "Revoke unauthorized privileges and review access permissions.").

action(insider_threat,
       "Investigate user activity and review privileged access logs.").

% -------------------------
% DIAGNOSIS
% -------------------------

diagnose :-
    write('=============================================='), nl,
    write(' CYBERSECURITY THREAT DIAGNOSIS SYSTEM'), nl,
    write('=============================================='), nl,
    findall(T, threat(T), Threats),
    write('Detected Threats: '), nl,
    display_threats(Threats).

display_threats([]) :-
    write('No known threats detected.'), nl.

display_threats([H|T]) :-
    write('- '),
    write(H), nl,
    action(H, A),
    write('  Recommended Action: '),
    write(A), nl,
    display_threats(T).

% -------------------------
% FORWARD CHAINING
% -------------------------

forward_chaining :-
    write('=============================================='), nl,
    write(' FORWARD CHAINING'), nl,
    write('=============================================='), nl,
    write('Initial facts are examined.'), nl,
    write('Applying matching production rules...'), nl,
    diagnose.

% -------------------------
% BACKWARD CHAINING
% -------------------------

backward_chaining(Threat) :-
    write('=============================================='), nl,
    write(' BACKWARD CHAINING'), nl,
    write('=============================================='), nl,
    write('Goal: '),
    write(Threat), nl,
    write('Checking whether the required conditions are true...'), nl,
    threat(Threat),
    write('Conclusion: '),
    write(Threat),
    write(' is detected.'), nl,
    action(Threat, Action),
    write('Recommended Action: '),
    write(Action), nl.
