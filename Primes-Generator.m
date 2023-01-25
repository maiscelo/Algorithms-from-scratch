indice = 1;
a = 800001;
delta = 800099 - 800001;
d = delta/2;
for i =1:5
z = randi([0, d]);
number(i) = a + 2*z +1;
end

%x = number(1);

for x = 3:2:number(1)
 y = 3; 
isprime = true;
while (y<=sqrt(x))
   %disp(x)
    %disp(y)
     %disp(mod(x,y))
   if (mod(x,y) == 0 || mod(x,2) == 0)
      isprime = false;
      break
   end
  y = y + 1;
end
if isprime == true
    primos(indice)= x;
    indice = indice + 1;
end
end
disp(primos)

i=1;
tamanho=size(primos);
%for j = 1:tamanho
resultado1=[];
resultado2=[];
n=1
%fori=1;
tamanho=size(primos);
%for j = 1:tamanho
j=tamanho(2);

%for r = 1:5
for j = tamanho(2):-1:1
while (primos(j)+primos(i)<=800044)
    disp(primos(j)+primos(i))
    if (primos(j)+primos(i))==800044
        resultado1(n) = primos(j); 
        resultado2(n)= primos(i);  
        n=n+1;
    end
     i=i+1;
     
end
%disp(i)
end
%end
