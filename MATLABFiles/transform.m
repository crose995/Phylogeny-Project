data2 = zeros(91,80);
for i = (1:91)
    for j = (1:80)
        if data(i+1,j+1) == "+"
            data2(i,j) = 1;
        elseif data(i+1,j+1) == "-"
            data2(i,j) = 0;
        else
            data2(i,j) = -1;
        end
    end
end
data2 = data2.';
       
