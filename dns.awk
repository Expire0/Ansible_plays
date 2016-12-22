#!/bin/awk
# checking out awk as a programming lang- always running dns query system
##run the file as awk -f dns.awk . then give is a domain name.  if you want to check a particular dns server
## give it the domain name plus the dns behind it yahoo.com ns.34fjjfc.com

{
	    domain = $1
	        server = $2

	#	printf( "host %s 8.8.8.8\n" , domain)
		system("host "domain " " server)

	}
