Program tinh_giai_thua;
Uses crt;
Var n,gt:integer;

function Giai_Thua(n:Integer):LongInt;
    begin
        gt:=1;
        For i:=1 to n do
        gt:=gt*i;
    end;

Begin
    Clrscr;
    Writeln('-------------------Tinh Giai Thua:---------------------------');
    Write('Nhap n ='); readln(n);
    
    while  (n  <  0) and (n >= 24)  do
        begin
            if n < 0 then  write('Nhap so n>=0');readln; 
            else  write('Nhap so < 25');readln; 
            Write('Nhap n ='); readln(n);
        end;

    WriteLn(n,'!=',giaithua(n));
    ReadLn;
End.