(define 
    (domain ToM_dom)
    (:requirements :strips :derived-predicates :fluents :durative-actions)
    
    (:types 
        agent
        states
        chaining
    )
    
    (:constants 
    robot - agent
    isSad - states
    isHappy - states
    knows - states
    hasGoal - states
    start - chaining
    end - chaining
    i1 - chaining
    i2 - chaining
    )
    
    (:predicates 
        (ToM ?x - chaining  ?y - agent ?z - states ?w -chaining)
        (test-ok)
    )
    
    (:action works 
        :parameters ( ?x - chaining  ?y - agent ?z - states ?w - chaining)
        :precondition (and (ToM start, Robot, isSad, end))
        :effect (and (test-ok))
    )
    
    (:derived (ToM ?x - chaining  ?y - agent ?z - isSad ?w - chaining)
        (exists (?x - chaining)
            (and
                ( ToM start Robot knows ?x)
                ( ToM ?x ?y isSad end)
            )
        )
    )

)
