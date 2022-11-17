(define
    (problem mission-happiness)
    (:domain interaction_HR)
   
    (:objects 
        h1 - human 
        h2 - human 
    )
    (:init
        (feels h1 sadness)
        (feels h2 neutral)

    )
    (:goal (and
            (feels h1 happiness)
            (makes h1 trust) 
            
        )
    )
)
