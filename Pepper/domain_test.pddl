(define 
    (domain test_dom)
    (:requirements :strips :derived-predicates :typing)
    
    (:types 
        person
    )
    
    (:constants
        Ilenia
    )

    (:predicates 
        (isIn ?person)
        
        
    )
    
    (:action recognize
        :parameters (?x - person)
        :precondition (and (isIn ?x))
        :effect (and (isIn Ilenia))
    )

    (:action say_something
        :parameters (?x - person)
        :precondition (and (isIn Ilenia))
        :effect (and (ok))
    )
)