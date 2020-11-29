#!C:/Perl64/bin/perl

print "Content-Type: text/htmll; charset=shift_jis\n\n";

#計算する

$n = 3;
$sum = 5 * $n;

print "<!DOCTYPE HTML PUBLIC \-//W3C//DTD HTML 4.01//EN\">\n";
print "<html>\n";
print "<body>\n";
print "<p>計算する</p>\n";
print "<p>計算結果は$sumです</p>\n";
print "</body>\n";
print "</html>\n";


exit;