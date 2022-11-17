(define 
    (domain family)
    (:requirements :strips :derived-predicates :fluents)
    
    (:types 
        person
    )
    
    (:predicates 
        (dad ?x - person ?y - person)
        (granpa ?x - person ?y - person)
        (test-ok)
    )
    
    (:action works 
        :parameters (?x - person ?y - person)
        :precondition (and (granpa ?x ?y))
        :effect (and (test-ok))
    )
    
    (:derived (granpa ?x - person ?z - person)
        (exists (?y - person)
            (and
                ( dad ?x  ?y )
                ( dad ?y  ?z )
            )
        )
    )

)
