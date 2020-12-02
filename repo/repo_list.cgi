#!C:/Perl64/bin/perl



	
#cgiヘッダーの出力
print "Content-Type: text/html;charset=utf-8\n\n";

open(FILE, "repo.html");
my @html = <FILE>;
close(FILE);

for $html (@html){
	print $html;
}

exit;