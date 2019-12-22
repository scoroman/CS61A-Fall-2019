; Lab 14: Final Review

(define (compose-all funcs)
    (define (helper func arg)
      (if (null? func) 
        arg 
        (helper (cdr func) ((car func) arg))
      )
    )
    (lambda (x) (helper funcs x))
)

(define (contains? lst s)
  (if (null? lst) 
  #f
  
  (if (eq? (car lst) s) #t 
      (contains? (cdr-stream lst) s)
  ))
)


(define (has-cycle? s)
  (define (helper s prev)
    (if (null? s)
      #f
      (if (contains? prev (car s))
          #t

        (helper 
          (cdr-stream s) 
          (cons-stream (car s) prev))))
      )
      (helper s nil)
    )

 
  