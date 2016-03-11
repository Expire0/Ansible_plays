#!/usr/bin/perl
 
$input = $ARGV[0];
 
if ($input =~ /^([0-9a-z]{2})([0-9a-z]{2})([0-9a-z]{2})([0-9a-z]{2})([0-9a-z]{2})([0-9a-z]{2})$/){
   $mac = "$1:$2:$3:$4:$5:$6";
}elsif ($input =~ /^([0-9a-z]{2})([0-9a-z]{2})\.([0-9a-z]{2})([0-9a-z]{2})\.([0-9a-z]{2})([0-9a-z]{2})$/){
   $mac = "$1:$2:$3:$4:$5:$6";
}elsif ($input =~ /^[0-9a-z]{2}:[0-9a-z]{2}:[0-9a-z]{2}:[0-9a-z]{2}:[0-9a-z]{2}:[0-9a-z]{2}$/){
   $mac = $input;
}else{
   print "$input is not a valid mac!!\n";
   exit;
}
 
print $mac."\n";
