#!C:\Strawberry/perl/bin/perl
use Smart::Comments;
#リファレンス、デリファレンスの練習
my @array1 = (a, b, c);
#$ref_array1は配列@array1のリファレンス
my $ref_array1 = \@array1;
### $ref_array1
my @array2 = (d, e, f, g);
#同じく$ref_array2は配列@array2のリファレンス

my $ref_array2 = \@array2;
### $ref_array2
my %hash = {};
#$hash{1},{2}をkeyにして$ref_array1,2をセット
$hash{1} = $ref_array1;
$hash{2} = $ref_array2;
### %hash
### arrayname: $hash{1}
for my $key(keys %hash){
    #ハッシュのリファレンスを取り出すときは@{$リファレンス変数名}
    foreach my $s(@{$hash{$key}}){
        print "$s\n";
    }
}

