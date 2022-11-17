(define
    (problem family_prob)
    (:domain family)
    (:objects
        Antonio - person
        Giuseppe - person
        Maria - person
    )
    (:init
        (dad Antonio Giuseppe)
        (dad Giuseppe Maria)
    )

    (:goal (test-ok)
    )
)
