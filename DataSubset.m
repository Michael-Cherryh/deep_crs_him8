%this is matlab, not python, sorry, It's what I had access to.
%extract the first 100 frames(of 973, and crops to 400*400 (out of 700 by
%400). I keep the first 100 frames to minimise file size
%only keep data sets B7, B9, B11, and B16
nccreate('H8_Flow_partial.nc','B7','Dimensions',{'lon',400,'lat',400,'time',100})
nccreate('H8_Flow_partial.nc','B9','Dimensions',{'lon',400,'lat',400,'time',100})
nccreate('H8_Flow_partial.nc','B11','Dimensions',{'lon',400,'lat',400,'time',100})
nccreate('H8_Flow_partial.nc','B16','Dimensions',{'lon',400,'lat',400,'time',100})
count  = [400, Inf, 100];
start = [151,1,1];
B7 = ncread('H8_Flow.nc','B7',startLoc,count);
ncwrite('H8_Flow_partial.nc','B7',B7);
B9 = ncread('H8_Flow.nc','B9',startLoc,count);
ncwrite('H8_Flow_partial.nc','B9',B9);
B11 = ncread('H8_Flow.nc','B11',startLoc,count);
ncwrite('H8_Flow_partial.nc','B11',B11);
B16 = ncread('H8_Flow.nc','B16',startLoc,count);
ncwrite('H8_Flow_partial.nc','B16',B16);