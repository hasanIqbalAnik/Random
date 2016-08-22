d = [25 27 27 28 28 30 100 105 105 107 107 108];

mu1 = 10;
mu2 = 50;
sigma1 = 10;
sigma2 = 10;

p1 = .5;
p2 = .5;

%until converges

v1 = p1 * normpdf(d, mu1, sigma1);
v2 = p2 * normpdf(d, mu2, sigma2);

temp1 = v1;
temp2 = v2;

v1 = temp1 ./ (temp1+ temp2)
v2 = temp2 ./ (temp1+ temp2)

n1 = sum(v1)
n2 = sum(v2)

mu1 = sum(v1 .* d) / n1
mu2 = sum(v2 .* d) / n2

sigma1 = (sum(d.^2) / 12) - mu1*mu1
sigma2 = (sum(d.^2) / 12) - mu2*mu2

p1 = n1 / 12
p2 = n2 / 12
