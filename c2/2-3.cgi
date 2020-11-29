#!C:/Perl64/bin/perl

#おみくじを引く

$role = int(rand 6);

if($role == 0){
	$kuji = "大吉";
	$tips = "何をしても絶好調の一日、新しいことにチャレンジしてみましょう";
}elsif($role == 1){
	$kuji = "中吉";
	$tips = "いいことが起きるかもしれませんね、散歩するのがよさそうです";
}elsif($role == 2){
	$kuji = "吉";
	$tips = "ちょっとしたうれしいことがありそうな予感";
}elsif($role == 3){
	$kuji = "小吉";
	$tips = "心の平安あり、トイレで読書すると吉";
}else{
	$kuji = "凶";
	$tips = "あんまついてなさそうです";
}

	
#cgiヘッダーの出力
print "Content-Type: text/html\n\n";
#print "Content-Type: text/htmll;charset=utf-8\n\n";

print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01// EN\">\n";
print "<html>\n";
print "<body>\n";
print "<h1>prelおみくじ</h1>\n";
print "<h1>今日の運勢は</h1>\n";
print "<h1>$kuji、$tips</h1>\n";

print "</body></html>\n";

#$roleに0から5までの整数の乱数値を代入
#elsifでroleに代入された数値ごとに出力する内容を変更
