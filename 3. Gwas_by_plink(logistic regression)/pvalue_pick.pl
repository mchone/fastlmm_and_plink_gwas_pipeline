#!/usr/bin/perl
use Statistics::Basic qw(:all);
my($sss,$ppp,$out)=@ARGV;
open OUT,">$out" or die ($!);
open SNP,"<$sss" or die ($!);
open PVA,"<$ppp" or die ($!);

my %snp;

while(<SNP>){
    chomp;
    next if /^[CW]/;
    my @arr=split/\t/;
    $snp{$arr[0]}=$_;
}

@pva=<PVA>;
chomp(@pva);

@got="";
$got[0] = shift(@pva);
print OUT "@got"."\n";

for $res(@pva){
$rsid = (split(/\t/,$res))[0];
for $ele(@got){
$goid = (split(/\t/,$ele))[0];
@v1=split(/\t/,$snp{$goid});
@v2=split(/\t/,$snp{$rsid});

$ck = 0;
@f1 = "";
@f2 = "";

for (1..533){
$ck++;
if ($v1[$ck] ne "NA" && $v2[$ck] ne "NA") {
push @f1,$v1[$ck];
push @f2,$v2[$ck];
}
}
#shift @f1;
#shift @f2;
print OUT @f1."\t";
print OUT @f2."\t";

$kk =0;
@t1="";
@t2="";

for (1..@f1){
$kk++;
if ($f1[$kk] eq $f1[1]){
push @t1,0;
}
else{
push @t1,2;
}
if ($f2[$kk] eq $f2[1]){
push @t2,0;
}
else{
push @t2,2;
}
}

shift @t1;
shift @t2;

print OUT @t1."\t";
print OUT @t2."\t";

my $c1 = vector(@t1);
my $c2 = vector(@t2);

my $cor = corr(@t1,@t2);
print OUT $cor."\n";
if ($cor < 0.7 and $cor > 0){
print OUT $res."\n";
push @got,$res;
}
last;
}
next;
}
close OUT;
close PVA;
close SNP;
