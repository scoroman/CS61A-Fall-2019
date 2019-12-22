(define (partial-sums stream)

(let ((first (stream-car stream)))
  (cons-stream first 
    (stream-map (lambda (x) (+ x first)) (partial-sums(stream-cdr stream)))
  )
)  

)