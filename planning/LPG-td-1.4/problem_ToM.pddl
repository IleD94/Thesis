(define
    (problem ToM_prob)
    (:domain ToM_dom)
    (:objects
        robot - agent
        Antonio - agent
        knows - states
        start - chaining
        isSad - states
        end - chaining
        i1 - chaining
    )
    (:init
        (ToM start, Robot knows i1)
        (ToM i1 Antonio isSad end)
        
    )

    (:goal (test-ok)
    )
)
