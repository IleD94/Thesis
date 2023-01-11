(define (domain annsallyaction_domain)

(:requirements :adl :derived-predicates :strips :typing :conditional-effects :negative-preconditions :equality)

(:types
    entity
    agent - entity 
    place - entity
    cosa - entity 

    phase
    id
)


(:predicates 
        (disjuncted ?a ?b - entity)     
        (Know ?x1 - id ?a - agent ?x2 - id ?v - phase)
        (See ?x1 - id  ?a - agent ?x2 - id ?v - phase)
        (hasStartId ?a - agent ?x - id)
        (isIn ?x1 - id ?e - entity ?p - entity ?v - phase) 
        (isPutting ?x2 - id ?a2 - agent ?o ?p - entity  ?v - phase)
        (isGoing ?x1 - id ?a - agent ?p1 ?p2 - entity ?v - phase)
        (follow ?v2 ?v1 - phase)
        (isHappy ?x1 - id ?a - agent ?x2 - id ?v - phase) 
        (ok) 
)


;--- Red

;-- Rule 1
(:action see_infer_know
    :parameters (?x1 - id ?a - agent ?x2 - id ?v - phase)
    :precondition (and 
            (See ?x1 ?a ?x2 ?v)
    )
    :effect (and 
            (Know ?x1 ?a ?x2 ?v)
    )
)



;--- Green

;-- Rule 2
(:action know_another_isIn
    :parameters (?x1 - id ?a2 - agent ?x2 - id ?v - phase ?a1 - agent ?p - entity)
    :precondition (and 
            (Know ?x1 ?a1 ?x2 ?v)
            (isIn ?x2 ?a2 ?p ?v)
            (hasStartId ?a1 ?x1)
    )
    :effect (and 
            (Know ?x1 ?a2 ?x2 ?v)
    )
)

;-- Rule 3
(:action one_see_another
    :parameters (?x1 - id ?a2 - agent ?x3 - id ?v - phase ?a1 - agent ?x2 - id ?p - entity ?e - entity)
    :precondition (and 
            (Know ?x1 ?a1 ?x2 ?v)
            (isIn ?x2 ?a2 ?p ?v)

            (Know ?x1 ?a1 ?x3 ?v)
            (isIn ?x3 ?e ?p ?v)

            (hasStartId ?a1 ?x1)

            (disjuncted ?a2 ?e)
    )
    :effect (and 
            (See ?x1 ?a2 ?x3 ?v)
    )
)


;--- Blue

;-- Rule 4
(:action agent_know_isPutting
    :parameters (?x1 - id ?a2 - agent ?x2 - id ?v - phase ?a1 - agent ?o ?p - entity)
    :precondition (and 
            (Know ?x1 ?a1 ?x2 ?v)
            (isPutting ?x2 ?a2 ?o ?p ?v)
            (hasStartId ?a1 ?x1)
    )
    :effect (and 
            (Know ?x1 ?a2 ?x2 ?v)
    )
)

;-- Rule 5
(:action isPutting_infer_See
    :parameters (?x1 - id ?a3 - agent ?x4 - id ?v - phase ?a1 ?a2 - agent ?x2 ?x3 - id ?p1 ?p2 ?o - entity)
    :precondition (and 
            (Know ?x1 ?a1 ?x2 ?v)
            (isIn ?x2 ?a2 ?p1 ?v)

            (Know ?x1 ?a1 ?x3 ?v)
            (isIn ?x3 ?a3 ?p1 ?v)

            (Know ?x1 ?a1 ?x4 ?v)
            (isPutting ?x4 ?a2 ?o ?p2 ?v)

            (hasStartId ?a3 ?x1)
            (disjuncted ?a2 ?a3)
    )
    :effect (and 
            (See ?x1 ?a3 ?x4 ?v)
    )
)

;-- Rule 6
(:action know_isPutting_infer_know_isIn
    :parameters (?x1 - id ?a1 - agent ?x2 - id ?v2 - phase ?o ?p - entity ?a2 - agent ?v1 - phase)
    :precondition (and 
            (Know ?x1 ?a1 ?x2 ?v1)
            (isPutting ?x2 ?a2 ?o ?p ?v1)

            (hasStartId ?a1 ?x1)
            (follow ?v2 ?v1)
            (disjuncted ?a1 ?a2)
    )
    :effect (and 
            (Know ?x1 ?a1 ?x2 ?v2)
            (isIn ?x2 ?o ?p ?v2)
    )
)

;-- Rule 7
(:action know_iamPutting_infer_know_isIn
    :parameters (?x1 - id ?a1 - agent ?x2 - id ?v2 - phase ?o ?p - entity ?v1 - phase )
    :precondition (and 
            (Know ?x1 ?a1 ?x2 ?v1)
            (isPutting ?x2 ?a1 ?o ?p ?v1)
            (hasStartId ?a1 ?x1)
            (follow ?v2 ?v1)
    )
    :effect (and 
            (Know ?x1 ?a1 ?x2 ?v2)
            (isIn ?x2 ?o ?p ?v2)
    )
)

; ;--- White 

;--Rule 8
(:action know_isGoing_infer_know
    :parameters (?x1 - id ?a2 - agent ?x2 - id ?v - phase ?a1 - agent ?p1 ?p2 - entity)
    :precondition (and 
            (Know ?x1 ?a1 ?x2 ?v)
            (isGoing ?x2 ?a2 ?p1 ?p2 ?v)
            (hasStartId ?a1 ?x1)
    )
    :effect (and 
            (Know ?x1 ?a2 ?x2 ?v)
    )
)

;-- Rule 9
(:action know_isIn_infer_know_isGoing
    :parameters (?x1 - id ?a3 - agent ?x4 - id ?v - phase ?x2 ?x3 - id ?a1 ?a2 - agent ?p1 ?p2 - entity)
    :precondition (and 
            (Know ?x1 ?a1 ?x2 ?v)
            (isIn ?x2 ?a2 ?p1 ?v)

            (Know ?x1 ?a1 ?x3 ?v)
            (isIn ?x3 ?a3 ?p1 ?v)

            (Know ?x1 ?a1 ?x4 ?v)
            (isGoing ?x4 ?a2 ?p1 ?p2 ?v)

            (hasStartId ?a1 ?x1)
            (disjuncted ?a2 ?a3) 
    )
    :effect (and 
            (See ?x1 ?a3 ?x4 ?v)
    )
)

;-- Rule 10
(:action know_isGoing_afterphase
    :parameters (?x1 - id ?a1 - agent ?x2 - id ?v2 - phase ?v1 - phase ?a2 - agent ?p1 ?p2 - entity)
    :precondition (and 
            (Know ?x1 ?a1 ?x2 ?v1)
            (isGoing ?x2 ?a2 ?p1 ?p2 ?v1)
            (hasStartId ?a1 ?x1)
            (disjuncted ?a1 ?a2)
            (follow ?v2 ?v1)
    )
    :effect (and 
            (Know ?x1 ?a1 ?x2 ?v2)
            (isIn ?x2 ?a2 ?p2 ?v2)
    )
)

;-- Rule 11
(:action know_iamGoing_afterphase
    :parameters (?x1 - id ?a - agent ?x2 - id ?v2 - phase ?v1 - phase ?p1 ?p2 - entity)
    :precondition (and 
            (Know ?x1 ?a ?x2 ?v1)
            (isGoing ?x2 ?a ?p1 ?p2 ?v1)
            (hasStartId ?a ?x1)
            (follow ?v2 ?v1)
    )
    :effect (and 
            (Know ?x1 ?a ?x2 ?v2)
            (isIn ?x2 ?a ?p2 ?v2) 
    )
)



(:action test
    :parameters (?x1 - id ?a2 - agent ?x2 - id ?v - phase ?p - entity ?o - entity)
    :precondition (and 
                (Know start sally twentythree fourth)
                (isIn twentythree sally elsewhere fourth)
                (Know start anne twentynine fifth)
                (See ?x1 ?a2 ?x2 ?v)  
                (Know ?x1 ?a2 ?x2 ?v)
                (isIn ?x2 ?o ?p ?v)  
        )
    :effect (and 
                (ok)
        )
)

)

