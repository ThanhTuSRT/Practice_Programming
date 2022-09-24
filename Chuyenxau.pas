program Chuyenxau; 
uses
  crt;
var
  s, r: String;
  i, k, j: Integer;
begin
  r := '';
  write('Nhap xau: ');
  readln(s);
  write('Nhap k: ');
  readln(k);
  for i := k + 1 to Length(s) do 
    {vi du nhu k=3 thi nhap SENDONGTHAP k=3 la SE_N_DONGTHAP (o chu N)}
    {vi vay phai cho i = k+1 de chon tu chu DONGTHAP tro di}    
       r:=r+s[i];
    {r nay la string trống (vi co dau '')}
    {nen khi r =r+s[i] thi r se bang s[i] (s[i] là tung chu cai cua string)}
    {vi du tu i= k+1 la 4 den Length(s) (Length(s) cua SENDONGTHAP la 11)}
    {la tu 4 den 11 (Chu DONGTHAP) thi r lan luot se bang chu D + O + N + G + T + H + A + P la DONGTHAP}
    
  for j:=1 to k do
      r:=r+s[j];
     {ta cho j = 1 den k la tu 1 den 3 la chu SEN}
     {sau khi r la chu DONGTHAP, r se cong them s[j] lan luot la chu S + E + N la chu SEN}
     {vay suy ra r luc nay bang chu DONGTHAPSEN}
      write(r);
     {Viet chu DONGTHAPSEN ra man hinh}
  readln;

end.
