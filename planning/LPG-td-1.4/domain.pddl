(define
    (domain interaction_HR)
    (:requirements :strips :typing)
    (:types
        human
        emotion
    )
    (:constants 
    happiness - emotion
    sadness - emotion
    neutral - emotion
    trust - emotion
    )

    (:predicates
        (feels ?h - human ?e - emotion)
        (is-near ?h - human)
        (makes ?h - human ?e - emotion )
        
    )


    (:action MAKE-JOKES
        :parameters (?h - human ?e - emotion)
        :precondition (and
            (is-near ?h)
            (feels ?h sadness)
        )   
        :effect (and
            (feels ?h happiness) (makes ?h trust )
            
        )

    )
    (:action GO-TO
        :parameters (?h - human)
        :precondition (not
            (is-near ?h)
        )
        :effect (and
            (is-near ?h)
            
        )

    )
)
