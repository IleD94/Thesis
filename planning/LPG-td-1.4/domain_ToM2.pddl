(define 
    (domain ToM_dom)
    (:requirements :strips :derived-predicates :fluents :durative-actions)
    
    (:types 
        agent
        states
        chaining
    )
    
    (:constants 
    ;robot - agent
    ;isSad - states
    ;isHappy - states
    
    ;hasGoal - states
    ;start - chaining
    ;end - chaining
    ;i1 - chaining
    ;i2 - chaining
    ;i3 - chaining
    ;i4 - chaining
    )
    
    (:predicates 
        (ToM ?x - chaining  ?y - agent ?z - states ?w -chaining)
        (test-ok)
    )
    
    (:action works 
        :parameters ( ?x - chaining  ?y - agent ?z - states ?w - chaining)
        :precondition (and (ToM start, robot, isSad, end))
        :effect (and (test-ok))
    )
    
    (:derived (ToM ?x - chaining ?y - agent ?r - states ?g - chaining )
        (exists (?z - states)
            (exists (?w - chaining)
                (exists (?f - agent)
                    (and
                        ( ToM ?x ?y ?z ?w)
                        ( ToM ?w ?f ?r ?g )
                    )
                )
            )    
        )
    )

)

