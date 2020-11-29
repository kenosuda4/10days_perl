#!C:/Perl64/bin/perl



#サイコロを振る

$n = int(rand 6) + 1;

#お言葉を出力
if($n == 4){
	print "<p>ふ、不吉....。４が出てしまいました</p>\n";
}

if($n % 2 == 0){
	$mg = "丁です";
}else{
	$mg = "半です";
}

#cgiヘッダーの出力
print "Content-Type: text/html\n\n";
#print "Content-Type: text/htmll;charset=utf-8\n\n";

print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01// EN\">\n";
print "<html>\n";
print "<body>\n";
print "<h1>prelサイコロ</h1>\n";
print "<h1>サイコロの目は</h1>\n";
print "<h1>$n、$mg!</h1>\n";

print "</body></html>\n";

# if文の中身　$nを2で割ったときの余りが0だった場合　$msに丁代入
# elseはそれ以外の場合　$msに半が代入される

# 演算子によって処理が行われる対象のことをオペランドと呼ぶ