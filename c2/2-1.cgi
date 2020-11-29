#!C:/Perl64/bin/perl


#cgiヘッダーの出力
print "Content-Type: text/html\n\n";
#print "Content-Type: text/htmll;charset=utf-8\n\n";
#サイコロを振る

$n = int(rand 6) + 1;


print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01// EN\">\n";
print "<html>\n";
print "<body>\n";
print "<h1>サイコロの目は</h1>\n";
print "<h1>$nです</h1>\n";

#お言葉を出力
if($n == 4){
	print "<p>ふ、不吉....。４が出てしまいました</p>\n";
}

print "</body></html>\n";

# $nは1-4.cgiの 変数$r と$dをまとめたもの
# if文 条件がが真のときに{}内の処理を実行
