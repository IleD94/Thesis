from pddlpy import pddlParser

# Parse a PDDL domain file
with open("domain.pddl", "r") as domain_file:
    domain_text = domain_file.read()
    domain = pddlParser.parse_pddl_domain(domain_text)
    print(domain)

# Parse a PDDL problem file
with open("problem.pddl", "r") as problem_file:
    problem_text = problem_file.read()
    problem = pddlParser.parse_pddl_problem(problem_text)
    print(problem)
