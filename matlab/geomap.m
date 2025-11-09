[A, R] = readgeoraster("geo8.tiff", OutputType="double");
Agray = rgb2gray(A); % konwersja RGB → grayscale
format long
latlim = R.LatitudeLimits;
lonlim = R.LongitudeLimits;

figure;
usamap(latlim, lonlim);
geoshow(A, R, "DisplayType", "texturemap");
colormap(gray);
%colorbar;

file="A.xlsx";
lat0 = readmatrix(file,'Sheet', "Arkusz1", 'Range', 'C2:C29');
lon0 = readmatrix(file,'Sheet',  "Arkusz1", 'Range', 'D2:D29');

lat1 = readmatrix(file,'Sheet', "Arkusz2", 'Range', 'H69:H114');
lon1 = readmatrix(file,'Sheet',  "Arkusz2", 'Range', 'I69:I114');

lat2 = readmatrix(file,'Sheet', "Arkusz2", 'Range', 'K69:K114');
lon2= readmatrix(file,'Sheet',  "Arkusz2", 'Range', 'L69:L114');

lat3 = readmatrix(file,'Sheet', "Arkusz2", 'Range', 'N69:N114');
lon3 = readmatrix(file,'Sheet',  "Arkusz2", 'Range', 'O69:O114');

id1 = readmatrix(file,'Sheet', "Arkusz2", 'Range', 'C69:C114');
id2 = readmatrix(file,'Sheet',  "Arkusz2", 'Range', 'D69:D114');

height = [46,5];
for i=1:1:28
    [row, col] = geographicToDiscrete(R, lat0(i), lon0(i));
    intensity0 = A(row, col);
    height(i,4) = intensity0*2000;
end 

for i=1:1:46
    
   [row, col] = geographicToDiscrete(R, lat1(i), lon1(i));
   intensity1 = A(row, col);
   height(i,1) = intensity1*2000;

   [row, col] = geographicToDiscrete(R, lat2(i), lon2(i));
   intensity2 = A(row, col);
   height(i,2) = intensity2*2000;

   [row, col] = geographicToDiscrete(R, lat3(i), lon3(i));
   intensity3 = A(row, col);
   height(i,3) = intensity3*2000;

  height(i,5) = abs(height(id1(i),4)-height(i,1))+ abs(height(i,1)-height(i,2))+abs(height(i,2)-height(i,3))+abs(height(i,3)-height(id2(i),4));

 
   lat=[lon1 lon2 lon3];
   lon=[lon1 lon2 lon3];
   hold on;
   
   
   plotm([lat0(id1(i)),lat0(id2(i))], [lon0(id1(i)),lon0(id2(i))], 'or', 'MarkerFaceColor','r', 'MarkerSize',6);
   plotm([lat0(id1(i)),lat1(i)], [lon0(id1(i)),lon1(i)], '-r', 'MarkerFaceColor','r', 'MarkerSize',6,'LineWidth',2);
   plotm([lat1(i),lat2(i)], [lon1(i),lon2(i)], '-r', 'MarkerFaceColor','r', 'MarkerSize',6,'LineWidth',2);
   plotm([lat2(i),lat3(i)], [lon2(i),lon3(i)], '-r', 'MarkerFaceColor','r', 'MarkerSize',6,'LineWidth',2);
   plotm([lat3(i),lat0(id2(i))], [lon3(i),lon0(id2(i))], '-r', 'MarkerFaceColor','r', 'MarkerSize',6,'LineWidth',2); 

end

tras = [2,1,6,5,4,17,16,15];
transl = [39,45,43,41,12,16,5];
for i=1:1:7
    plotm(lat0(tras(i)), lon0(tras(i)), 'og', 'MarkerFaceColor','g', 'MarkerSize',6,'LineWidth',3);
    plotm([lat0(id1(transl(i))),lat1(transl(i))], [lon0(id1(transl(i))),lon1(transl(i))], '-g', 'MarkerFaceColor','g', 'MarkerSize',6,'LineWidth',3);
    plotm([lat1(transl(i)),lat2(transl(i))], [lon1(transl(i)),lon2(transl(i))], '-g', 'MarkerFaceColor','g', 'MarkerSize',6,'LineWidth',3);
    plotm([lat2(transl(i)),lat3(transl(i))], [lon2(transl(i)),lon3(transl(i))], '-g', 'MarkerFaceColor','g', 'MarkerSize',6,'LineWidth',3);
    plotm([lat3(transl(i)),lat0(id2(transl(i)))], [lon3(transl(i)),lon0(id2(transl(i)))], '-g', 'MarkerFaceColor','g', 'MarkerSize',6,'LineWidth',3);

end
plotm(lat0(tras(8)), lon0(tras(8)), 'og', 'MarkerFaceColor','g', 'MarkerSize',6);
%plotm([lat0(12),lat0(13)], [lon0(12),lon0(13)], 'ob', 'MarkerFaceColor','b', 'MarkerSize',6);

