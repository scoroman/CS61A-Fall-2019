
; Tail recursion

(define (replicate x n)
  (define (helper lst sofar) 
    (if (= lst n) sofar 
       (helper (+ lst 1) (cons x sofar))
    )
  )
  (helper 0 nil)
)

(define (accumulate combiner start n term)
  (if (< n 1) start 
    (combiner (term n) (accumulate combiner start(- n 1) term))
  )
)

(define (accumulate-tail combiner start n term)
  (if (< n 1)  start
    (accumulate-tail combiner (combiner (term n) start) (- n 1) term)
  )
)

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  (cons-stream 3 (map-stream (lambda(x) (+ x 3)) multiples-of-three))
)


(define (nondecreastream s)
    (define (make-list lst input-stream previous)
        (if (or (null? input-stream) (> previous (car input-stream)))
            (make-stream lst input-stream)
            (make-list (append lst (list (car input-stream)))
                (cdr-stream input-stream) 
                (car input-stream))))
 
    (define (make-stream item stream-rest)
        (if (null? stream-rest)
        (cons-stream item nil)
        (cons-stream item
            (nondecreastream stream-rest))))

    (make-list (list (car s)) (cdr-stream s) (car s)))





(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))