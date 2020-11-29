#!C:/Perl64/bin/perl


#cgiヘッダーの出力
print "Content-Type: text/html\n\n";
#print "Content-Type: text/htmll;charset=utf-8\n\n";
#サイコロを振る

$r = rand 6;
$d = int($r) + 1;
print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01// EN\">\n";
print "<html>\n";
print "<body>\n";
print "<h1>サイコロの目は</h1>\n";
print "<h1>$dです</h1>\n";
print "</body>\n";
print "</html>\n";
exit; 


# rand 引数として数値を与えると乱数（小数点以下の単数のある）を戻り値として返す関数
# rand 6 だと1~6を返す
# $d = int($6) + 1は int関数を$rを引数にし呼び出している
# int関数は引数として受けた一つの数値を小数点以下切り捨てて整数にし、戻値として返す
# つまりこの式はrand関数で出た0以上6未満の数値を$rに代入し、
# $dにint関数で少数を切り捨てた$rに1を足して代入するという式
