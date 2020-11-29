#!C:/Perl64/bin/perl

#おみくじを引く

$role = int(rand 6);

@kuji = ('大吉', '中吉'.'吉','小吉','末吉','凶','大凶');
@tips = ('絶好調', '良い一日', 'ちょっとしたいいこと', '悪くない', '普通', '微妙', 'ダメダメ');
	
#cgiヘッダーの出力
print "Content-Type: text/html\n\n";
#print "Content-Type: text/htmll;charset=utf-8\n\n";

print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01// EN\">\n";
print "<html>\n";
print "<body>\n";
print "<h1>prelおみくじ</h1>\n";
print "<h1>今日の運勢は</h1>\n";
print "<h1>$kuji[$role]</h1>\n";
print "<h1>$tips[$role]</h1>\n";

print "</body></html>\n";

#くじと文を配列にそれぞれ格納
# $roleをそれぞれの配列のインデックス番号として扱う