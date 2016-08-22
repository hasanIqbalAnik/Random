A = [1 2 3;
    9 7 11; 
    15 2 3];

hold on

b = [2:9;4:11;9:16];
x = inv(A)*b;
for i = 1:cols(x)
    quiver3(0,0,0, x(1,i), x(2,i), x(3,i));
end
