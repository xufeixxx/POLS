function result = LambertW(x)
min_diff = 1e-10;
if x == -1/exp(1)
    result = -1;
elseif x<0 && x>-1/exp(1)
    q = log(-x);
    p = 1;
    while abs(p-q) > min_diff
        p = (q * q + x / exp(q)) / (q + 1);
        q = (p * p + x / exp(p)) / (p + 1);
    end
    result = round(1000000*q)/1000000;
elseif x==0
    result = 0;
else
    result = 0;
end
end

