def for_chain(rules, facts, goals):
    inferred = set(facts)

    while True:
        applied = False
        for rule in rules:
            prem, conc = rule
            if all(p in inferred for p in prem):
                if conc not in inferred:
                    print(f"Inferred : {conc} from {prem}")
                    inferred.add(conc)
                    applied = True
                    if conc == goal:
                        return True, inferred
        if not applied:
            break
    return False, inferred


rules = [
    (["A","B"], "C"),
    (["C"], "D"),
    (["D"], "E"),
]

facts = ["A", "B"]

goal = "E"

success, inferred_facts = for_chain(rules, facts, goal)
print("\nFinal Faces: ", inferred_facts)

if success:
    print(f"Goal {goal} was successfully infereed!")
else:
    print(f"Goal {goal} could NOT be inferred.")