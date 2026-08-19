""
AT2 - Question 4: Student Academic Advising - Logic Mapping & Resolution Proof
================================================================================
Scenario:
  Priya has attendance below 75% and has failed two courses.
  Rule 1: low attendance            -> requires attendance counseling
  Rule 2: failed two-or-more courses -> requires academic counseling
  Rule 3: both counseling needs      -> requires academic support

This script:
  (i)   lists the knowledge components
  (ii)  evaluates the propositional-logic rules for Priya
  (iii) evaluates the equivalent first-order-logic rules (generalised, x=Priya)
  (iv)  demonstrates unification / substitution theta = {x/Priya}
  (v)   proves NeedsAcademicSupport(Priya) with resolution refutation
  (vi)  prints the plain-language reasoning chain
"""


# ---------------------------------------------------------------------
# (i) KNOWLEDGE COMPONENTS
# ---------------------------------------------------------------------
def print_knowledge_components():
    print("--- (i) KNOWLEDGE COMPONENTS ---")
    print("Entity           : Priya")
    print("Attributes       : attendance < 75%,  failed courses = 2")
    print("Derived concepts : RequiresAttendanceCounseling, RequiresAcademicCounseling")
    print("Rules            : R1 (attendance->counseling), R2 (failures->counseling),")
    print("                   R3 (both counselings -> academic support)")
    print("Goal             : NeedsAcademicSupport(Priya) ?")


# ---------------------------------------------------------------------
# (ii) PROPOSITIONAL LOGIC   A,B given ; C,D,E derived
# ---------------------------------------------------------------------
def propositional_logic(A, B):
    print("\n--- (ii) PROPOSITIONAL LOGIC ---")
    print(f"A = LowAttendance(Priya)      = {A}")
    print(f"B = FailedTwoOrMore(Priya)    = {B}")

    C = A       # Rule 1 : A -> C
    D = B       # Rule 2 : B -> D
    E = C and D  # Rule 3 : (C ^ D) -> E

    print(f"Rule1 A->C : C = RequiresAttendanceCounseling(Priya) = {C}")
    print(f"Rule2 B->D : D = RequiresAcademicCounseling(Priya)   = {D}")
    print(f"Rule3 (C^D)->E : E = NeedsAcademicSupport(Priya)     = {E}")
    return C, D, E


# ---------------------------------------------------------------------
# (iii) FIRST-ORDER LOGIC   generalised rules applied to x = Priya
# ---------------------------------------------------------------------
FACTS = {
    "LowAttendance": {"Priya"},
    "FailedTwoOrMore": {"Priya"},
}
DERIVED = {"RequiresAttendanceCounseling": set(),
           "RequiresAcademicCounseling": set(),
           "NeedsAcademicSupport": set()}

RULES_FOL = [
    ("LowAttendance", "RequiresAttendanceCounseling"),          # Rule 1
    ("FailedTwoOrMore", "RequiresAcademicCounseling"),           # Rule 2
]


def first_order_logic(student):
    print("\n--- (iii) FIRST-ORDER LOGIC  (forall x rules, x/", student, ") ---")
    for pre, post in RULES_FOL:
        if student in FACTS.get(pre, set()):
            DERIVED[post].add(student)
            print(f"forall x [{pre}(x) -> {post}(x)]   with x={student}  =>  {post}({student}) derived")
    if student in DERIVED["RequiresAttendanceCounseling"] and student in DERIVED["RequiresAcademicCounseling"]:
        DERIVED["NeedsAcademicSupport"].add(student)
        print(f"forall x [(RequiresAttendanceCounseling(x) ^ RequiresAcademicCounseling(x)) -> "
              f"NeedsAcademicSupport(x)]  with x={student}  =>  NeedsAcademicSupport({student}) derived")
    return DERIVED


# ---------------------------------------------------------------------
# (iv) UNIFICATION / SUBSTITUTION
# ---------------------------------------------------------------------
def unify(term_with_var, ground_term, var="x"):
    """Very small unifier: term_with_var e.g. ('LowAttendance','x')"""
    pred_v, arg_v = term_with_var
    pred_g, arg_g = ground_term
    if pred_v != pred_g:
        return None
    if arg_v == var:
        return {var: arg_g}
    return {} if arg_v == arg_g else None


def demo_unification(student):
    print("\n--- (iv) UNIFICATION / SUBSTITUTION ---")
    pairs = [
        (("LowAttendance", "x"), ("LowAttendance", student)),
        (("FailedTwoOrMore", "x"), ("FailedTwoOrMore", student)),
        (("RequiresAttendanceCounseling", "x"), ("RequiresAttendanceCounseling", student)),
        (("RequiresAcademicCounseling", "x"), ("RequiresAcademicCounseling", student)),
    ]
    for var_term, ground_term in pairs:
        theta = unify(var_term, ground_term)
        print(f"unify{var_term} with {ground_term}  ->  theta = {theta}")


# ---------------------------------------------------------------------
# (v) RESOLUTION REFUTATION
# ---------------------------------------------------------------------
def resolution_proof(student):
    """
    Clauses (student already substituted in, i.e. rules grounded with x/student):
      C1 : ~LowAttendance(student)  v  RequiresAttendanceCounseling(student)
      C2 : ~FailedTwoOrMore(student) v RequiresAcademicCounseling(student)
      C3 : ~RequiresAttendanceCounseling(student) v ~RequiresAcademicCounseling(student)
           v NeedsAcademicSupport(student)
      C4 : LowAttendance(student)                         (fact)
      C5 : FailedTwoOrMore(student)                        (fact)
      C6 : ~NeedsAcademicSupport(student)                  (negated goal)
    """
    print("\n--- (v) RESOLUTION REFUTATION ---")
    L = lambda p: f"{p}({student})"          # positive literal string
    NL = lambda p: f"~{p}({student})"        # negative literal string

    C1 = {NL("LowAttendance"), L("RequiresAttendanceCounseling")}
    C2 = {NL("FailedTwoOrMore"), L("RequiresAcademicCounseling")}
    C3 = {NL("RequiresAttendanceCounseling"), NL("RequiresAcademicCounseling"), L("NeedsAcademicSupport")}
    C4 = {L("LowAttendance")}
    C5 = {L("FailedTwoOrMore")}
    C6 = {NL("NeedsAcademicSupport")}       # negated goal

    for tag, clause in zip("C1 C2 C3 C4 C5 C6".split(), [C1, C2, C3, C4, C5, C6]):
        print(f"{tag}: {clause}")

    def resolve(ca, cb, literal, neg_literal):
        return (ca - {literal}) | (cb - {neg_literal})

    print("\nStep 1: resolve C1, C4 on LowAttendance ->")
    C7 = resolve(C1, C4, NL("LowAttendance"), L("LowAttendance"))
    print("   C7 =", C7)

    print("Step 2: resolve C2, C5 on FailedTwoOrMore ->")
    C8 = resolve(C2, C5, NL("FailedTwoOrMore"), L("FailedTwoOrMore"))
    print("   C8 =", C8)

    print("Step 3: resolve C3, C7 on RequiresAttendanceCounseling ->")
    C9 = resolve(C3, C7, NL("RequiresAttendanceCounseling"), L("RequiresAttendanceCounseling"))
    print("   C9 =", C9)

    print("Step 4: resolve C9, C8 on RequiresAcademicCounseling ->")
    C10 = resolve(C9, C8, NL("RequiresAcademicCounseling"), L("RequiresAcademicCounseling"))
    print("   C10 =", C10)

    print("Step 5: resolve C10, C6 on NeedsAcademicSupport ->")
    C11 = resolve(C10, C6, L("NeedsAcademicSupport"), NL("NeedsAcademicSupport"))
    print("   C11 =", C11, "(empty clause -> contradiction)" if not C11 else "")

    proved = len(C11) == 0
    print(f"\nRESULT: NeedsAcademicSupport({student}) is", "PROVED TRUE" if proved else "NOT proved")
    return proved


# ---------------------------------------------------------------------
# (vi) PLAIN-LANGUAGE REASONING CHAIN
# ---------------------------------------------------------------------
def reasoning_chain(student):
    print("\n--- (vi) REASONING STEPS ---")
    print(f"1. {student}'s attendance is below 75%  =>  Rule 1 fires  =>  requires attendance counseling")
    print(f"2. {student} has failed two courses      =>  Rule 2 fires  =>  requires academic counseling")
    print("3. Both counseling requirements now hold  =>  Rule 3 premise satisfied")
    print(f"4. Rule 3 fires  =>  {student} needs academic support")


# ---------------------------------------------------------------------
# RUN EVERYTHING
# ---------------------------------------------------------------------
if __name__ == "__main__":
    STUDENT = "Priya"
    print("=" * 60)
    print("STUDENT ACADEMIC ADVISING - LOGIC MAPPING & RESOLUTION - AT2 Q4")
    print("=" * 60)

    print_knowledge_components()
    propositional_logic(A=True, B=True)
    first_order_logic(STUDENT)
    demo_unification(STUDENT)
    resolution_proof(STUDENT)
    reasoning_chain(STUDENT)

    print(f"\nCONCLUSION: {STUDENT} requires academic support.")
