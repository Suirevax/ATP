def normalize(a,b,A,B,x):
    invalid_inputs = False
    if( a >= b ):
        invalid_inputs = True
        print('destination lower bound is higher than upper bound! Lower bound: ', a, '. Upper bound:', b, '.')
    if( A >= B ):
        invalid_inputs = True
        print('Source lower bound is higher than upper bound!  Lower bound: ', A, '. Upper bound:', B, '.')
    if ( A > x or B < x):
        invalid_inputs = True
        print('Value to be normalized does not ie within destination bounds! Lower bound: ', A, '. Upper bound:', B, '. Value: ', x, '.')
    if(invalid_inputs):
        return None
    return a + (x - A) * (b - a) / (B - A)